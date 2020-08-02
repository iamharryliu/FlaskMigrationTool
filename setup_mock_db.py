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
    add_users_to_db(db)
    print(f"DB setup in {time.time() - t0}s")


if __name__ == "__main__":
    main()

