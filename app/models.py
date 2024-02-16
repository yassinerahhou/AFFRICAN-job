from datetime import datetime
from app import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer # first thing we import to addd rst password funtion in our site
from flask import current_app
from sqlalchemy.orm import relationship


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
# we l l ccreat 2 methods to geenerate tokens : reset & verify the token :
    def get_reset_token(self, expires_sec=1800):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY']) # s = serialaser object ! 
        return s.dumps({'user_id': self.id}) # dumps ?
    
    @staticmethod
    # s = take the token as an argument and creat serialazer , if we hav exeption (not the same)  return non if not retur user whi that user id
    
    def verify_reset_token(token):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)






class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
# Update Post Model: addcomments 
    
    comments = db.relationship('Comment', backref='post', lazy=True)
    # update for category 
    
    
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)






    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
# first thing to add comment section is to add comment class
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Add a relationship to the User model
    user = db.relationship('User', backref='comments' , lazy=True)
    def __repr__(self):
        return f"Comment('{self.text}', '{self.user_id}')"
    



