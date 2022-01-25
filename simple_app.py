from flask import Flask

app = Flask(__name__)

@app.route('/') # decorator makes the function a view/controller
def index():
    return "Hello from Treehouse"

app.run(debug=True, port=8000, host='0.0.0.0') 
# anytime we make changes, Flask will autorestart if debug=True
# port tells python which port to listen on
# host='0.0.0.0' means listen on all addresses that can get to port