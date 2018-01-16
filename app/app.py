""" import Flask class from flask module/package
"""
from flask import Flask, render_template, url_for, redirect, request, flash, session
from functools import wraps
from wtfeg1_form import RegistrationForm, LoginForm, EventsForm
from models import Events


app = Flask(__name__)
app.config['SECRET_KEY'] = "this is secret"  # Flask-WTF: Needed for CSRF
USERS = {}





@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if form.validate_on_submit():
            if username and email and password:
                USERS[username] = username
                USERS[email] = email
                USERS[password] = password
            # Save the comment here.
                flash('Thanks for registering, ' + username)
                return redirect(url_for('signin'))
        else:
            flash('Error: All the form fields are required. ')


    return render_template("signup.html", form=form)


@app.route("/signin", methods=['GET', 'POST'])
def signin():

        form = LoginForm()  # Construct an instance of LoginForm
        if request.method == 'POST':
              username = request.form['username']
              password = request.form['password']
              if form.validate_on_submit():  # POST request with valid input
                  # Verify username and password
                  if request.form['username'] not in USERS.values() or request.form['password'] not in USERS.values():
                      flash('Wrong username or password')
                    

                  else:
                      session['username'] = request.form['username']
                      # Using Flask's flash to output login message
                      flash('You have logged in succssfully')
                      return redirect(url_for('view'))

        # For the initial GET request, and subsequent invalid POST request,
        # render an login page, with the login form instance created

        return render_template("signin.html", form=form)
def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('username'):
            flash('Login to continue', 'warning')
            return redirect(url_for('signin', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

@app.route("/view")
@login_required
def view():

    # return render_template("view.html", event_lists=USERS[session['username']].event_lists)
    return render_template("view.html")


@app.route("/create", methods=['GET', 'POST'])
# @login_required
def create():
    form = EventsForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        title = request.form['title']
        location = request.form['location']
        category = request.form['category']
        description = request.form['description']

        res = Events(title, location, category, description).create(request.form['title'], request.form['location'], request.form['category'], request.form['description'])
        
        if res == True:
            flash("event created successfuly")
            return redirect(url_for('view'))
        else:
            flash("event not created")

    return render_template("create.html", form=form)
  


@app.route("/update")
def update():

    return render_template("update.html")


@app.route("/delete")
def delete():

    return render_template("create.html")


@app.route("/logout")
def logout():

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
