from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

comments = []

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin":
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Login failed"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html")
    return redirect("/")


@app.route("/comment", methods=["GET","POST"])
def comment():
    if request.method == "POST":
        text = request.form["comment"]
        comments.append(text)

    return render_template("comment.html", comments=comments)


app.run(host="0.0.0.0", port=5000)
