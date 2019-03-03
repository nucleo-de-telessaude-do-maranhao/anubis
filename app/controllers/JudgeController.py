from flask import render_template, request, render_template, redirect

from datetime import date

from werkzeug.security import generate_password_hash, check_password_hash

from app import app

from app.models.Judge import Judge

@app.route("/jauthorsudges/new/", methods=["GET"])
def redirect_new_judge():
    return render_template("new-judge.html")


@app.route("/judges/", methods=["POST"])
def create_judge():
    name = request.form.get("name")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    password = generate_password_hash(request.form.get("password"))
    createdAt = str(date.today())
    modifiedAt = str(date.today())

    judge = Judge(name=name, cpf=cpf, email=email, password=password, createdAt=createdAt, modifiedAt=modifiedAt)

    judge.create()

    return redirect("/")
