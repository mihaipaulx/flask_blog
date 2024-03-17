from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '691883cfbcd9db070fb6d4a1c1204165'

posts = [
    {
        "title": "Blog post 1",
        "author": "Mihai",
        "content": "This is the first blog post",
        "date_posted": "March 16, 2024"
    },
    {
        "title": "Blog post 2",
        "author": "Bob",
        "content": "This is the second blog post",
        "date_posted": "March 15, 2024"
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password": 
            flash(f"You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Login unsuccessful, wrong email or password.", "danger")
    return render_template("login.html", title="login", form=form)

if __name__ == "__main__":
    app.run(debug=True)