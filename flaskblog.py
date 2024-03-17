from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)