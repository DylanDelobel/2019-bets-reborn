import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.flask_app import create_app, db

# import model for db
from app.model import user

from app import blueprint

app = create_app(os.getenv('PROJECT_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(port=8000)


if __name__ == '__main__':
    manager.run()
