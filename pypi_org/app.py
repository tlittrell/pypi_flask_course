import flask

app = flask.Flask('pypi_org')

@app.route('/')
def hello_world():
    return "Hello world."

app.run()