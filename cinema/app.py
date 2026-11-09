from datetime import datetime

from flask import Flask, request, abort, jsonify, render_template

from .data import MOVIES  # Относительный импорт


app = Flask(__name__)

message = "Всем привет!"
counter = 0

@app.route("/", methods=["GET", "POST", "DELETE"])
def index():
    if request.method == "GET":
        return render_template("index.html", now=datetime.now(), abracadabra="ABC")


@app.get("/faq")
def faq():
    return render_template("faq.html")

@app.route("/movies/<int:movie_id>")
def get_movie(movie_id):
    try:
        return render_template(f"movies/{movie_id}.html")
    except:
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
