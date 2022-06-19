# How to run:
# $ FLASK_APP=main flask run --host=0.0.0.0

from flask import Flask


application = Flask('app')


@application.route('/')
def get_main_page() -> str:
    return f'<p>Hello World!<br>This is a main page.</p>'
