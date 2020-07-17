from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


cors = CORS()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
