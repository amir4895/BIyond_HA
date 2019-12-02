from random import randrange

from flask_restful import Api, Resource
from flask import request
from flask_executor import Executor
from flask import Response

from BIyond import app, requests_queue
from BIyond.utils_functions import analyze_json
from BIyond.request_queue import RequestQueueObject

api = Api(app)
executor = Executor(app)


class ETLPost(Resource):
    def post(self):
        jsn = request.get_json()
        jsn_data = jsn.get("filenames")
        if not jsn_data or type(jsn_data) != list:
            return Response(status=204)
        corrupted_chance = randrange(0, 9)
        corrupt = True if corrupted_chance == 0 else False
        new_request = executor.submit(analyze_json, file_names_list=jsn_data, is_corrupt=corrupt)
        requests_queue.append(RequestQueueObject(new_request, jsn_data))
        return Response(status=202)


api.add_resource(ETLPost, '/etl')
api.init_app(app)


