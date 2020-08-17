from WebApp.models import User
from mock_utils.names import names
from datetime import datetime, timedelta
import random

now = datetime.now()


def add_data_to_db(db):
    add_users_to_db(db)


def add_users_to_db(db):
    print("adding users to db")
    users = get_users()
    for user in users:
        user = User(
            first_name=user["first_name"],
            last_name=user["last_name"],
            phone_number=user["phone_number"],
            email=user["email"],
            birth_date=user["birth_date"],
            signup_date=user["signup_date"],
        )
        db.session.add(user)
    db.session.commit()


def get_users():
    users = []
    for _ in range(100):
        user = create_user()
        users.append(user)
    return users


def create_user():
    first_name = random.choice(names)
    last_name = random.choice(names)
    phone_number = f"{random.randint(100, 999)}-555-{random.randint(1000,9999)}"
    email = f"{first_name.lower()}_{last_name.lower()}@bogusemail.com"
    birth_date = datetime(
        random.randint(2017, now.year), random.randint(1, 12), random.randint(1, 28)
    )
    signup_date = datetime(
        random.randint(2017, now.year), random.randint(1, 12), random.randint(1, 28)
    )
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email,
        "birth_date": birth_date,
        "signup_date": signup_date,
    }
    return user

