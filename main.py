from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def signup():
    User_Name = request.form['userName']
    password = request.form['pass_word']
    verifiedpw = request.form['password_verify']
    email = request.form['email_opt']
    
    nameUser_error = ' '

    return render_template('landingPage.html')




app.run()



