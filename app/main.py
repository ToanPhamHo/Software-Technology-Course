import flask
from flask import render_template, redirect, request
from flask_login import login_user, login_required, current_user
from app import app, login, dao, utils
from app.models import *
import hashlib


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    kw = request.args.get("keyword")

    if kw:
        return render_template("lookUp.html", product_1=dao.read_products(keyword=kw))
    else:
        return render_template("main.html", product_1=dao.read_products())


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route("/login-admin", methods=['post', 'get'])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())

        user = User.query.filter(User.username == username.strip(), User.password == password).first()

        if user:
            login_user(user=user)
            if user.is_active == 1:
                if user.username == "ThuThu":
                    flask.flash('Logged in successfully ! Hello %s' % user.username)
                    return redirect("/admin")
                else:
                    flask.flash('Logged in successfully ! Hello %s' % user.username)
                    return redirect("/admin")
            else:
                return redirect("/main")
        else:
            error = "Invalid username or password. Please try again!"

    return render_template("admin/login.html", error=error)


@app.route("/register", methods=['post', 'get'])
def register():
    err = ""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        email = str(email).strip()
        username = request.form.get("username")
        is_active = 0
        pw = request.form.get("password")
        pw2 = request.form.get("confirm")

        if str(pw).strip() != str(pw2).strip():
            err = "Something is wrong, please sign up again !"
        elif dao.read_user(email):
            err = "Something is wrong with your fill-up email, please try again !"
        else:
            pw = str(pw)
            password = str(hashlib.md5(pw.strip().encode("utf-8")).hexdigest())
            dao.add_user(name, email, is_active, username, password)
            err = "Register successfully !"

    return render_template("admin/login.html", err=err)


if __name__ == "__main__":
    app.run(debug=True)

