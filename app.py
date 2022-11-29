from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1> Hello World </h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/<temp>')
def celsius_to_fahrenheit(temp=""):
    temp_num = float(temp) * 9.0 / 5 + 32
    return f"{temp}C is {str(temp_num)}F"


if __name__ == '__main__':
    app.run()

