from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def index():
    return "mara"

"""


@app.route('/holaMundo')
def hola():
    return "hola huecos"


def index():
    return render_template('index.html', titulo='serotes')


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5005)
