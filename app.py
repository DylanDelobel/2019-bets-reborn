import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db

# import model for db
from app.model import user

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
