from datetime import datetime
from secrets import token_hex

from flask import Flask, request, abort, jsonify, render_template, make_response, redirect, url_for, session

from .data import MOVIES  # Относительный импорт


app = Flask(__name__)
app.secret_key = token_hex()

message = "Всем привет!"
counter = 0

@app.get("/")
def index():
    print(session.get("password"))
    content = render_template(
        "index.html",
        movies=MOVIES,
        movies_count=len(MOVIES),
        username=request.cookies.get("username"),
    )
    response = make_response(content)
    response.status = 201
    response.headers["Server"] = "Apache 2.0"
    if request.cookies.get("abc") is None:
        response.set_cookie(key="abc", value="def")
    return response


@app.get("/login")
def get_login_page():
    return render_template("login.html")


@app.post("/login")
def login():
    response = redirect(url_for("index"))
    response.set_cookie(key="username", value=request.form["username"])
    session["password"] = request.form["password"]
    return response


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.get("/faq")
def faq():
    return render_template("faq.html")

@app.route("/movies/<int:movie_id>")
def get_movie(movie_id):
    for movie in MOVIES:
        if movie["id"] == movie_id:
            return render_template(f"movie.html", movie=movie)
    abort(404)

@app.errorhandler(404)
def handle_404(error):
    return render_template("404.html")

@app.route("/old")
def old_index():
    content = "<h1>Всем привет!</h1>"
    return (content, 200, {"X-Cinema-Status": "Open"})

@app.route("/date")
def get_date():
    now = datetime.now()
    content = f"<h1>{message} Сейчас {now}</h1>"
    return (content, 200, {"X-Cinema-Status": "Open"})

@app.route("/counter")
def get_counter():
    global counter
    content = f"<h1>{message} Это {counter} запрос</h1>"
    counter += 1
    return (content, 200, {"X-Cinema-Status": "Open"})


@app.route("/add/<int:a>/<int:b>")
def calculate(a, b):
    content = a + b
    return (str(content), 200, {"X-Cinema-Status": "Open"})


@app.route("/calculator")
def calculator():
    operation = request.args.get("operation")

    try:
        first = int(request.args["first"])
        second = int(request.args["second"])
    except (KeyError, ValueError):
        abort(400)

    if operation == "add":
        content = str(first + second)
    elif operation == "sub":
        content = str(first - second)
    elif operation == "mul":
        content = str(first * second)
    elif operation == "div":
        content = str(first / second)
    else:
        abort(400)
    return (str(content), 200, {"X-Cinema-Status": "Open"})


@app.errorhandler(400)
def handle_bad_request(error):
    print(error)
    return "Неправильные данные, будь внимательнее"


@app.errorhandler(ZeroDivisionError)
def handle_zero_division(error):
    print(error)
    return "Нельзя делить на 0"


@app.route("/movies_json")
def get_movies_json():
    return jsonify(MOVIES)


@app.route("/movies_json/<int:movie_id>")
def get_movie_json(movie_id):
    found = None
    for movie in MOVIES:
        if movie["id"] == movie_id:
            found = movie
            break 
    if found is not None:
        return jsonify(found)
    else:
        abort(404)
