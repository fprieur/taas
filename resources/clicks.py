from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
import json


class GetUrl(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        return {'result': True}


class ClickButton(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('button_id', type=str, required=True, help="button_id is mandatory")
        args = parser.parse_args()
        return {'result': True}
