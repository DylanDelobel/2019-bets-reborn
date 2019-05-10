import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from dotenv import load_dotenv

load_dotenv()

from app.flask_app import create_app, db

# import model for db
from app.model import user

from app import blueprint

app = create_app(os.getenv('PROJECT_ENV') or 'prod')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@manager.command
def run():
    app.run(port)


if __name__ == '__main__':
    manager.run(port)
