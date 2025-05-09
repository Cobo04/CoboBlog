from flaskapp import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self): # How the object is printed whenever we print it
        return f"User('{self.username}', '{self.image_file}', '{self.account_type}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text(1000), nullable=False)
    description = db.Column(db.Text(1000), nullable=False)
    blog_type = db.Column(db.String, nullable=False)
    authors = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # removed a nullable=False argument to allow for deletion of users but may cause bugs idk

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"