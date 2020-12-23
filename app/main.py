import flask
from flask import render_template, redirect, request, url_for, jsonify, session
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


@app.route("/admin")
def admin():
    if current_user.is_authenticated:
        return render_template("admin/index.html", product_1=dao.read_products())
    else:
        return render_template("main.html")


@app.route("/books")
def books():
    return render_template("books.html", product_1=dao.read_products())


@app.route("/bookDetail")
def bookDetail():
    return render_template("book-detail.html", product_1=dao.read_products())


@app.route("/bookList")
def bookList():
    return render_template("book-list.html", product_1=dao.read_products())


@app.route("/myAccount")
def my_account():
    return render_template("my-account.html")


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
    else:
        return render_template("admin/login.html")

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


@app.route("/api/list", methods=['get', 'post'])
def add_to_list():
    if 'list' not in session:
        session['list'] = {}

    list = session['list']

    data = request.json
    id = str(data.get('id'))
    name = data.get('name')
    price = data.get('price')

    if id in list:
        list[id]['quantity'] = list[id]['quantity'] + 1
    else:
        list[id] = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        }

    session['list'] = list

    total_quan, total_amont = dao.list_stats(list)

    return jsonify({
        "total_amount": total_amont,
        "total_quantity": total_quan
    })


if __name__ == "__main__":
    app.run(debug=True)

