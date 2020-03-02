from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask_migrate import Migrate
import uuid
from helpers import csv_parser


app = Flask(__name__)

# db settings
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost:5432/unibell"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

ALLOWED_EXTENSIONS = ('csv',)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


class PhoneFileModel(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String)

    def __str__(self):
        return f"File {self.file_name}, fileId {self.file_id}"


class PhoneModel(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String)
    phone_file = db.relationship("PhoneFileModel", backref='phonefile')

    def __str__(self):
        return f"<Phone {self.phone}"


@app.route('phones/', methods=['GET', 'POST'])
def phones_add():
    if request.method == 'POST':
        # принимаем файл, парсим
        file = request.files['file']
        if file and allowed_file(file.filename):
            file_name = file.filename
            phones_list = csv_parser(file)
            # записываем данные в базу

    elif request.method == 'GET':
        # отдаем список файлов с file_id
        files_list = PhoneFileModel.query.all()
        return jsonify(files_list)


@app.route('phones/<uuid:file_id>/', methods=['GET'])
def get_phones_json(file_id):
    if request.method == 'GET':
        # отдаем телефоны из файла file_id в формате json
        # return jsonify(phones)
        pass


if __name__ == '__main__':
    app.run()
