import time
from WebApp import create_app, db
from mock_utils import add_users_to_db


def main():
    t0 = time.time()
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()
    add_users(db)
    print(f"DB setup in {time.time() - t0}s")


def add_users(db):
    print("adding users to db")
    add_users_to_db(db)


if __name__ == "__main__":
    main()

