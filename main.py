from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

def name_verif(x):
    if len(x) <= 3:
        return False
    else:
        return True


@app.route("/")
def index():
    return render_template('signup.html')


@app.route("/", methods=['POST'])
def signup():
    user_Name = request.form['userName']
    password = request.form['pass_word']
    verifiedpw = request.form['password_verify']
    email = request.form['email_opt']
    
    passw_error = ' '

    if name_verif(user_Name) == False:
        return "UserName is too short"
    if ' ' in user_Name:
        return "Your user name should be one word, no spaces"

    if password != verifiedpw:
        passw_error = "passwords do not match"

    result = "You have entereted " + user_Name + " for the user name"

    return render_template('landingPage.html', passw_error=passw_error)


app.run()



