from datetime import datetime, timedelta
import random
from mock_data.transactions import (
    clothing_transactions,
    food_transactions,
    drink_transactions,
)
from WebApp.models import User, Transaction


def add_users_to_db(db):
    for i in range(100):
        user = User(name=f"User {i+1}")
        db.session.add(user)
    db.session.commit()


def add_transactions_to_db(db):
    total = 0
    for i in range(User.query.count()):
        transactions = get_user_transactions()
        total += len(transactions)
        for transaction in transactions:
            db.session.add(
                Transaction(
                    owner=User.query.get(i + 1),
                    amount=transaction["amount"],
                    timestamp=transaction["timestamp"],
                    merchant_name=transaction["merchant_name"],
                    category=transaction["category"],
                )
            )
    db.session.commit()


def get_user_transactions(days=30):
    now_dt = datetime.now()
    dt = datetime.now() - timedelta(days=days)
    transactions = []
    while dt < now_dt.now():
        dt = dt + timedelta(days=1)
        bought_lunch = random.randint(0, 2)
        if bought_lunch:
            transaction = dict(random.choice(food_transactions["fast-food"]))
            transaction["timestamp"] = dt
            transactions.append(transaction)
        ate_out_for_dinner = not random.randint(0, 5)
        if ate_out_for_dinner:
            ate_fast_food = random.randint(0, 1)
            if ate_fast_food:
                transaction = dict(random.choice(food_transactions["fast-food"]))
                transaction["timestamp"] = dt
                transactions.append(transaction)
            else:
                transaction = dict(random.choice(food_transactions["dining"]))
                transaction["timestamp"] = dt
                transactions.append(transaction)
        bought_clothes = not random.randint(0, 30)
        if bought_clothes:
            transaction = dict(random.choice(clothing_transactions))
            transaction["timestamp"] = dt
            transactions.append(transaction)
    return transactions
