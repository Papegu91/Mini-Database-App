from app import db
from .models import User


# Define sample data
sample_users = [
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "password1",
        "phone_number": "123-456-7890",
    },
    {
        "username": "user2",
        "email": "user2@example.com",
        "password": "password2",
        "phone_number": "987-654-3210",
    },

]


for user_data in sample_users:
    user = User(**user_data)
    db.session.add(user)


db.session.commit()
