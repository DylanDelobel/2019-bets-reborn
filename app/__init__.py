from flask_restplus import Api
from flask import Blueprint

from .controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='2019 BETS API',
          version='1.0',
          description='BETS REST Documentation'
          )

api.add_namespace(user_ns, path='/user')
