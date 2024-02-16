from flask_wtf import FlaskForm 
from flask_wtf.file import FileAllowed , FileField
from flask_login import current_user
from wtforms import BooleanField, DateField,TextAreaField, FieldList, EmailField, StringField,FileField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from app.models import User
from flask_wtf.file import FileField, FileAllowed

class registerForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=16)])
    email = EmailField('Email',
                       validators=[DataRequired(), Email(),])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a differet one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):

    email = EmailField('Email',
                       validators=[DataRequired(), Email(),])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Post')
    image = FileField('Article Image')
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    # New category for creation
    new_category = StringField('New Category', validators=[Length(min=1, max=50)])
    
    
    


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=16)])
    email = EmailField('Email',
                   validators=[DataRequired(), Email(),])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    
    submit = SubmitField('Update')
   
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a differet one.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            

class RequestRestForm(FlaskForm):
     email= StringField('email', validators=[DataRequired(), Email()])
     submit = SubmitField('Request Password Reset')
     
     def validate_email(self, email):
        # check if we have user whit this email 
        user = User.query.filter_by(email=email.data).first()
        if user is None:
             raise ValidationError('There is no account with that email. You must register first.')
        

        # lfoqkan ghi dyal request rest password - db hna fin ayconfirmih 
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class CommentForm(FlaskForm):
    comment_text = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')
