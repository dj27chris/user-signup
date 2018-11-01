from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template

@app.route("/")
def index():
     return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup():
    User_Name = request.form['userName']
    password = request.form['pass_word']
    verifiedpw = request.form['password_verify']
    email = request.form['email_opt']
    



@app.route('/validate-time')
def display_time_form():
    template = jinja_env.get_template('time_form.html')
    return template.render()
     


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False



@app.route('/validate-time', methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error= 'Hour is out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        return "Success"
    else: 
        template = jinja_env.get_template('time_form.html')
        return template.render(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)



tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        

    template = jinja_env.get_template('todos.html')
    return template.render(title="To Do", tasks=tasks)




app.run()



