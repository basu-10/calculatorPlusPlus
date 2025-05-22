from flask import Flask, render_template, request, jsonify, session
from calculator import Calculator
from flask import redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session

@app.route("/")
def index():
    # Initialize history if not present
    if "history" not in session:
        session["history"] = []
    return render_template("index.html", history=session["history"])

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expr = data.get("expression", "")
    calc = Calculator(expression=expr)
    result = calc.evaluate()

    # Store history
    history = session.get("history", [])
    history.append({"expression": expr, "result": result})
    session["history"] = history
    return jsonify({"result": result})

@app.route("/clear", methods=["POST"])
def clear():
    session["history"] = []
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
