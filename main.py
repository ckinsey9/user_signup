from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def validate_user():
    username_error = ""
    password_error = ""
    email_error = ""
    verify_error = ""
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    minimum = 3
    maximum = 20
    space = " "
    needed = ["@","."]
    if username == "":
        username_error = "Please enter a valid username"
    elif len(username) > maximum or len(username) < minimum or space in username:
        username_error = "Length of username must be 3-20 characters, no spaces"
    
    if password == "":
        password_error = "Please enter a valid password"
    elif len(password) > maximum or len(password) < minimum or space in password:
        password_error = "Length of password must be 3-20 characters, no spaces"
    
    if verify == "":
        verify_error = "Please verify your password"
    elif not verify == password:
        verify_error = "The passwords do not match"

    if email:
        if len(email) > maximum or len(email) < minimum or "@" not in email or "." not in email:
            email_error = 'If provided, email must be 3-20 characters, no spaces, and only one "@" and "."'

    if not username_error and not password_error and not email_error and not verify_error:
        return redirect("/welcome?user={0}".format(username))
    else:
        return render_template("index.html", 
        username_error=username_error,
        password_error=password_error,
        email_error=email_error,
        verify_error=verify_error, 
        username=username,
        password="",
        verify="", 
        email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get("user")
    return render_template("welcome.html", user = username)
          

app.run()