from flask_script import (
    Server,
    Manager,
)
from flask_migrate import Migrate, MigrateCommand
from project import create_app, config
from project.database import db


app = create_app(app_config=config.DevelopmentConfig)

Migrate(app, db)

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
