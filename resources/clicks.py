from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
import json
import taas_execute



class Click(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help="id is mandatory")
        parser.add_argument('url', type=str, required=True, help="url is mandatory")
        parser.add_argument('expected_url', type=str, required=True, help="expected_url mandatory")
        args = parser.parse_args()
        taasExecute = taas_execute.ClickExecute()
        results = taasExecute.testClick(str(args['id']), str(args['url']), str(args['expected_url']))
        return results
