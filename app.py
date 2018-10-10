from flask import Flask
from flask.json import jsonify
from dev_tmp.test import get_employees
from dev_tmp.Employee import Employee
from flask.json import JSONEncoder

app = Flask(__name__)


# A customized JSON encoder that knows about your SiteConfig class
# TODO Really? Move to another place
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Employee):
            return obj.__dict__
        return JSONEncoder.default(self, obj)


# Tell your flask app to use your customised JSON encoder
app.json_encoder = CustomJSONEncoder


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/employees")
def employees():
    return jsonify(get_employees())
