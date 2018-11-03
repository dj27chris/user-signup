from flask import Flask, request, redirect, render_template, url_for

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

@app.route("/welcome")
def welcome():
    message= request.args.get('message', 'empty')
    return render_template('landingPage.html', message=message)


@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['username']
    password = request.form['password']
    verifiedpw = request.form['password_verify']
    email = request.form['email_opt']
    

    if name_verif(user_name) == False:
        return render_template('signup.html', username_error="User name is too short")
    if ' ' in user_name:
        return render_template('signup.html', username_error="Your user name should be one word, no spaces.")

    if password != verifiedpw:
        return render_template('signup.html', password_error="Passwords do not match.")

    result = "You have entereted " + user_Name + " for the user name"

    return redirect(url_for('welcome', message=result))


app.run()



