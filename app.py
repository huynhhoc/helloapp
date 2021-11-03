from flask import Flask, render_template

huynhapp = Flask(__name__)
# Replace the existing home function with the one below
@huynhapp.route("/")
def home():
    return render_template("home.html")

# New functions
@huynhapp.route("/about/")
def about():
    return render_template("about.html")

@huynhapp.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
     huynhapp.run()