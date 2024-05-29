from flask import Flask, render_template, request
#import Maths.mathematics functions
from Maths.mathematics import addition, subtraction, multiplication
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    """Addition"""
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return str(addition(num1, num2))

@app.route("/sub")
def sub_route():
    """Subtraction"""
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return str(subtraction(num1, num2))

@app.route("/mul")
def mul_route():
    """Multiplication"""
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return str(multiplication(num1, num2))

@app.route("/")
def render_index_page():
    # render index page
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
