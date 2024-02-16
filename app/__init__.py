from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = '427a827e54ecf862b56f3d13a10802ea'


# here where our data will be stored 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'test_login_3'
login_manager.login_message_category = 'info'
migrate = Migrate(app, db)
# REst password config ; 
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'  # Update with your email provider
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kichouhi989@gmail.com' #os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = 'nagfnmlconlnvirj '   # to skep it save : os.environ.get('EMAIL_PASS')
mail = Mail(app)
# end of the rest passwordt config

from app.errors.handlers import errors
app.register_blueprint(errors)


from app import routes