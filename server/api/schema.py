from ..extensions import ma
from .models import Bike


class BikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bike


bike_schema = BikeSchema()
bikes_schema = BikeSchema(many=True)

    # id = ma.auto_field()
    # name = ma.auto_field()
    # size_chart_to_use = ma.auto_field()
    # bottom_tube_length = ma.auto_field()
    # brakes = ma.auto_field()
    # shifters = ma.auto_field()
    # water_bottle = ma.auto_field()
    # lights = ma.auto_field()
    # bell = ma.auto_field()
    # rack = ma.auto_field()
    # pannier = ma.auto_field()
    # kickstand = ma.auto_field()
    # notes = ma.auto_field()
    # intake_date = ma.auto_field()
    # bike_tech_review_date = ma.auto_field()
    # drop_off_date = ma.auto_field()
