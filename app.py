from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/hi')
@app.route('/hello')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/greet/<name>')
def greets(name):
    return '<h1>Hello {}!</h1>'.format(name)


@app.cli.command()
def hello():
    click.echo('Hello, Human! ')

