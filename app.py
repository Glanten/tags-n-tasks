from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")