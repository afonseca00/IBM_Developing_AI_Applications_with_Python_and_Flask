from flask import Flask, request, render_template
from Maths.mathematics import summation, subtraction, multiplication

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum")
def sum_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
def subtract_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul")
def multiply_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    return str(result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
