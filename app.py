from flask import Flask, render_template
from markupsafe import escape

from os_info import get_os_version, get_kernel_version

app = Flask(__name__)

@app.route('/')
def index(name=None):
    os_version = get_os_version()
    kernel_version = get_kernel_version()

    return render_template('index.html', os_version=os_version, kernel_version=kernel_version)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def helllo_name(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello_template/')
@app.route('/hello_template/<name>')
def hello_template(name=None):
    return render_template('hello.html', person=name)
