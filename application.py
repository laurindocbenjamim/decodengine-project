
from flask import Flask, render_template, jsonify

app = Flask("Decodengine")

@app.route('/')
def index():
    return '<h1 style="color: blue">Welcome to DecodEngine Application</h1>'

@app.route('/tes')
def test():
    return jsonify({"sms": "Welcome to DecodEngine Application"})

if __name__ == '__main__':
    app.run(debug=True)