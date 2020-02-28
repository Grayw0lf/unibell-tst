from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost:5432/unibell"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class PhonesModel(db.Model):
    __tablename__ = 'phones'

    id = db.Column(db.Integer, primary_key=True)
    phones_json = db.Column(db.JSON)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
