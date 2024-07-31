from flask import Flask, render_template
import requests
import pprint

blogs = requests.get('https://api.npoint.io/c3a80236a09977004744').json()
pprint.pprint(blogs)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs = blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/index/<int:index>")
def blogPost(index):
    requestedBlog = None

    for blog in blogs:
        if blog["id"] == index:
            requestedBlog = blog

    return render_template("post.html", post=requestedBlog)

if __name__ == "__main__":
    app.run(debug=True)

