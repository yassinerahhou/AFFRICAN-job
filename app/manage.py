from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Drop the _alembic_tmp_comment table if it exists
with app.app_context():
    db.engine.execute("DROP TABLE IF EXISTS _alembic_tmp_comment")

# Additional database-related tasks can be added here

if __name__ == '__main__':
    print("Database management script executed.")
