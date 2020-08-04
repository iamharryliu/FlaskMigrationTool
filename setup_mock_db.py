from WebApp import create_app, db
from mock_utils import add_data_to_db
import time


def main():
    t0 = time.time()
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()
    add_data_to_db(db)
    print(f"DB setup in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()

