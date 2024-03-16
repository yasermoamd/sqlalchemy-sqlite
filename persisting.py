from models import User, Comment
from connect import engine
from sqlalchemy.orm import Session

session = Session(bind=engine)

user1 = User(
    username = 'Yaser',
    email = 'user1@example.com',
    comments = [
        Comment(text= "Hello World!"),
        Comment(text= "Great man!!"),
        Comment(text= "Yea bro!"),
    ]
)

user2 = User(
    username = 'Omar',
    email = 'user2@example.com',
    comments = [
        Comment(text= "What's app "),
        Comment(text= "is this in england"),
    ]
)

user3 = User(
    username = 'Naser',
    email = 'user3@example.com',
    comments = [
        Comment(text= "Call me back"),
    ]
)

session.add_all([user1, user2, user3])
session.commit()
