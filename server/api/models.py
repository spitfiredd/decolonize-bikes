# from server.extensions import db
from sqlalchemy.orm import backref
from server.database import (
    Column,
    PkModel,
    db,
    reference_col,
    relationship,
)


class BasePersonModel(PkModel):

    __abstract__ = True

    first_name = Column(db.String(100))
    last_name = Column(db.String(100))
    pronouns = Column(db.String(50))
    email = Column(db.String(100))
    mobile_phone = Column(db.String(15))
    address = Column(db.String(255))
    address2 = Column(db.String(255))
    city = Column(db.String(100))
    state = Column(db.String(50))
    zip_code = Column(db.String(20))


class Recipient(BasePersonModel):

    __tablename__ = 'recipient'
    height = Column(db.Integer)
    bike_recieved = Column(db.DateTime)
    delivery_date = Column(db.DateTime)
    consult_date = Column(db.DateTime)
    bike_id = reference_col('bike', nullable=True)
    bike = relationship('Bike', backref='recipient')
    accessory_id = reference_col('accessory', nullable=True)
    accessory = relationship('Accessory', backref='recipient')


class Accessory(PkModel):

    __tablename__ = 'accessory'
    item_name = Column(db.String(200))
    donor_id = reference_col('donor')
    donor = relationship('Donor', backref='accessory')


class Bike(PkModel):

    __tablename__ = 'bike'

    name = Column(db.String(150))
    color = Column(db.String(100))
    size_chart_to_use = Column(db.String(50))
    bottom_tube_length = Column(db.Integer)
    brakes = Column(db.String(50))
    shifters = Column(db.String(50))
    water_bottle = Column(db.Boolean)
    lights = Column(db.Boolean)
    bell = Column(db.Boolean)
    rack = Column(db.Boolean)
    pannier = Column(db.Boolean)
    kickstand = Column(db.Boolean)
    notes = Column(db.Text)
    intake_date = Column(db.DateTime)
    bike_tech_review_date = Column(db.DateTime)
    drop_off_date = Column(db.DateTime)
    mechanic_id = reference_col('mechanic', nullable=True)
    mechanic = relationship('Mechanic', backref='bike')
    donor_id = reference_col('donor', nullable=True)
    donor = relationship('Donor', backref='bike')


class Donor(BasePersonModel):

    __tablename__ = 'donor'
    pickup_date = Column(db.DateTime)
    platform = Column(db.String(100))


class Mechanic(BasePersonModel):

    __tablename__ = 'mechanic'


class User(BasePersonModel):

    __tablename__ = 'user'
