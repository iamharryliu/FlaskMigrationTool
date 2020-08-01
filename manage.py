from WebApp import create_app, db
from WebApp.config import Config
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command("runserver", Server(port=Config.PORT_NUMBER))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
