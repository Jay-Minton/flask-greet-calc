# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_call():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = add(a,b)
    return str(total)

@app.route('/sub')
def sub_call():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = sub(a,b)
    return str(total)

@app.route('/mult')
def mult_call():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = mult(a,b)
    return str(total)

@app.route('/div')
def div_call():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = div(a,b)
    return str(total) 

functions = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<id>')
def math_call(id):
        a = int(request.args["a"])
        b = int(request.args["b"])
        total = functions[id](a,b)
        return str(total)