import flask
from flask import Flask

app = Flask(__name__)


def get_services():
    return [
        {'service': 'Tech Support', 'description': 'Tech Support description'}
        , {'service': 'Data architecture', 'description': 'Data architecture description'}
        , {'service': 'Data migration services', 'description': 'Data migration services description'}
        , {'service': 'Data Management', 'description': 'Data management services description'}
        , {'service': 'Consulting', 'description': 'Consulting services description'}
    ]


@app.route('/')
def index():  # put application's code here
    cnc_services = get_services()
    return flask.render_template('main/index.html', services=cnc_services)


if __name__ == '__main__':
    app.run(debug=True)
