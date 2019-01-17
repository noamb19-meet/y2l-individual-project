from flask import Flask ,render_template, url_for, redirect, request
app = Flask(__name__)
from flask import session as login_session
from database import add_user, get_all_users, login

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
        
        add_user(username,password,family)
        print ("post method 2")
        return redirect (url_for("home"))


@app.route('/login',methods=['GET', 'POST'])
def login_route():
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
            login_session['username']=user.user_name
            return redirect (url_for("home"))





if __name__ == '__main__':
    app.run(debug=True)

