# How to run:
# $ FLASK_APP=main flask run --host=0.0.0.0

from flask import Flask
from flask_jsonrpc import JSONRPC as JsonRpc


application = Flask('app')
json_rpc = JsonRpc(application, '/api')


@application.route('/')
def get_main_page() -> str:
    return f'<p>Hello World!<br>This is a main page.</p>'


@json_rpc.method('get_text')
def get_test_text() -> str:
    return 'Lorem ipsum dolor sit amet'


@json_rpc.method('get_number')
def get_test_number() -> int:
    return 42
