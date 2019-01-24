from flask import Flask ,render_template, url_for, redirect, request
app = Flask(__name__)
from flask import session as login_session
from database import *
from datetime import *
app.secret_key = 'super secret key'
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        print ("get method")
        return render_template('sign-up.html')
    else:
        print("post method 1")
        username = request.form['user_name']
        password= request.form['password']
        family= request.form['family']
        add_user(username,password,family)
        print ("post method 2")
        return redirect (url_for("home"))


@app.route('/login',methods=['GET', 'POST'])
def login_route():
    global service, calendar
    if request.method== 'GET':
        return render_template("log-in.html")
    else:
        user_name = request.form['user_name']
        password= request.form['password']
        user = login(user_name, password)
        if user == False:
            print("Unable to initiate session")
            return render_template("log-in.html",message="Your username or password is incorrect")
        else:
            store = file.Storage('token.json')
            creds = store.get()
            #creds = None
            if not creds or creds.invalid:
                flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
                creds = tools.run_flow(flow, store)
            print("connecting to calendar")
            service = build('calendar', 'v3', http=creds.authorize(Http()))

            calendar = service.calendars().get(calendarId='primary').execute()
            print(calendar['timeZone'])

            family=get_events_by_family(user.family)

            for family_event in family:
                    event = {}
                    event['start'] = {'dateTime':family_event.date.isoformat(), 'timeZone':calendar['timeZone']}
                    event['end'] = {'dateTime': (family_event.date + timedelta(hours=1)).isoformat(),'timeZone':calendar['timeZone']}
                    event['summary'] = family_event.name
                    service.events().insert(calendarId='primary', body=event).execute()
            
            login_session['username']=user.username
            return redirect (url_for("home"))

@app.route('/add-event',methods=['GET', 'POST'])
def add():
    global service, calendar
    if request.method == 'GET':
        print ("get method")
        return render_template('add-event.html')
    else:
        print(request.form)
        print("post method 1")
        name = request.form['name']
        date= request.form['date']
        date=datetime.strptime(date,'%Y-%m-%dT%H:%M')
        family= request.form['family']
        #service = build('calendar', 'v3', http=creds.authorize(Http()))
        #calendar = service.calendars().get(calendarId='primary').execute()
        #print(calendar['timeZone'])
        
        event = {}
        event['start'] = {'dateTime':date.isoformat(), 'timeZone':calendar['timeZone']}
        event['end'] = {'dateTime': (date + timedelta(hours=1)).isoformat(),'timeZone':calendar['timeZone']}
        event['summary'] = name
        service.events().insert(calendarId='primary', body=event).execute()
        print ("post method 2")
        return redirect (url_for("home"))

@app.route('/logout', methods=['GET'])
def logout():
    del login_session['username']
    return redirect (url_for("home"))




if __name__ == '__main__':
    app.run(debug=True)

