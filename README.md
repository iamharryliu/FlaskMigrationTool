# FlaskMigrationTool
Flask App to handle database migration.

### Requirements

Python3.6+

### Setup


By default the script is configured to create an SQLite database in the mock-db directory called site.db. You can define the SQL server in the configuragtion file, WebApp/config.py.
```
SQLALCHEMY_DATABASE_URI="mysql+pymysql://user:password@host/dbname"
```

Setup virtual environment.
```
python -m venv venv
source venv/bin/activate # venv/Scripts/activate for Windows users.
pip install -r requirements.txt
```

### Usage

Run script to create datbase.
```
python setup_db.py
```

Preview the database by running the command below and visiting http://localhost:5000/admin/.
```
python manage.py runserver
```