# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect, url_for

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# main driver function
if __name__ == '__main__':
    app.run()