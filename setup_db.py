from time import time
from WebApp import create_app, db
from utils import add_users_to_db


def main():

    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()

    add_data(db)


def add_data(db):
    t0 = time()
    print("adding users to db")
    add_users_to_db(db)
    print(f"Db setup in {time() - t0}s")


if __name__ == "__main__":
    main()

