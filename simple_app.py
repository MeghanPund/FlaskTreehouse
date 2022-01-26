from flask import Flask
from flask import request # global

app = Flask(__name__)

@app.route('/') # decorator makes the function a view/controller
def index(name="Treehouse"):
    name = request.args.get('name', name)
    # to change the value from Treehouse to a name, open the page
    # append '?name='whatevername' to URL
    return f"Hello from {name}"

app.run(debug=True, port=8000, host='0.0.0.0') 
# anytime we make changes, Flask will autorestart if debug=True
# port tells python which port to listen on
# host='0.0.0.0' means listen on all addresses that can get to port