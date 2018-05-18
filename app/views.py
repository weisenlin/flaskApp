# cong:utf-8

from flask import jsonify
from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=['GET', ])
def hello():
    return jsonify(msg="hello world!")


@app.route("/login", methods=["GET",])
def login():
    return """
        <form action="" method="POST">
        username:<input type="text" name="username" ></br>
        password:<input type="password" name="password">
        <input type="submit" value="go" >
        </form>
        """
