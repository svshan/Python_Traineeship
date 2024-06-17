from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index_view():
    """
    Default endpoint, it is public and can be accessed by anyone
    """
    return jsonify(msg="Hello world!")


@app.route("/user")
def user_view():
    """
    User endpoint, can only be accessed by an authorized user
    """
    return jsonify(msg="Hello user!")


@app.route("/admin")
def admin_view():
    """
    Admin endpoint, can only be accessed by an admin
    """
    return jsonify(msg="Hello admin!")
