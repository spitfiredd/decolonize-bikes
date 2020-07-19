from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse

from .models import Bike
from .schema import bike_schema, bikes_schema

API_VERSION_V1 = 1

api_bp = Blueprint('api', __name__)
api_v1 = Api(api_bp)
parser = reqparse.RequestParser()


class HelloWorld(Resource):

    def get(self):
        return jsonify({'hello': 'world'})


class BikeListResource(Resource):

    def get(self):
        bikes = Bike.query.all()
        return bikes_schema.dump(bikes)

    def post(self):
        data = request.json
        new_bike = Bike.create(**data)
        new_bike.save()
        return bike_schema.dump(new_bike)


class BikeResource(Resource):

    def get(self, bike_id):
        bike = Bike.query.get_or_404(bike_id)
        return bike_schema.dump(bike)

    def patch(self, bike_id):
        bike = Bike.query.get_or_404(bike_id)
        data = request.json
        bike.update(**data)
        return bike_schema.dump(bike)

    def delete(self, bike_id):
        bike = Bike.query.get_or_404(bike_id)
        bike.delete()
        return bike_schema.dump(bike), 204


api_v1.add_resource(BikeListResource, '/bikes')
api_v1.add_resource(BikeResource, '/bike/<int:bike_id>')
api_v1.add_resource(HelloWorld, '/helloworld')
