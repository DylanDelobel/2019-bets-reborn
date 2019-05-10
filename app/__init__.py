from flask_restplus import Api
from flask import Blueprint, url_for

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)


class CustomAPI(Api):
    """https://github.com/noirbizarre/flask-restplus/issues/223#issuecomment-381439513"""

    @property
    def specs_url(self):
        """
        The Swagger specifications absolute url (ie. `swagger.json`)
        :rtype: str
        """
        return url_for(self.endpoint('specs'), _external=False)


api = CustomAPI(blueprint,
                title='2019 BETS API',
                version='1.0',
                description='BETS REST Documentation'
                )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
