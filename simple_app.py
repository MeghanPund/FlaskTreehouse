from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/') # decorator makes the function a view/controller
@app.route('/<name>') # captures whatever follows / as the name variable/arg
def index(name="Treehouse"):
    return f"Hello from {name}"

@app.route('/<int:num1>/<float:num2>')
@app.route('/<float:num1>/<int:num2>')
@app.route('/<int:num1>/<int:num2>')
@app.route('/<float:num1>/<float:num2>')
def sum(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template("add.html", **context)

app.run(debug=True, port=8000, host='0.0.0.0') 
# anytime we make changes, Flask will autorestart if debug=True
# port tells python which port to listen on
# host='0.0.0.0' means listen on all addresses that can get to port