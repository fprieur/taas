from flask import Flask
from flask.ext import restful
from resources import clicks
from flask.ext.cors import CORS

app = Flask(__name__)
api = restful.Api(app)
cors = CORS(app)

api.add_resource(clicks.Click, '/1/click')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
