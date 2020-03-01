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

ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


class FilePhonesModel(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String)
    file_id = db.Column(UUID(as_uuid=True), default=str(uuid.uuid4()))

    def __repr__(self): # Непонятно нужно ли вообще переопределять данный метод
        return f"<File {self.filename}, fileId {self.file_id}>"

    def __str__(self):
        return f"File {self.file_name}, fileId {self.file_id}"


class PhoneModel(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String)
    file_phone = db.relationship("FilePhonesModel", backref='phone')

    def __repr__(self):
        return f"<Phone {self.phone}"

    def __str__(self):
        return f"<Phone {self.phone}"


@app.route('phones/', methods=['GET', 'POST'])
def phones_add():
    if request.method == 'POST':
        # принимаем файл, парсим, записываем в базу
        file = request.files['file']
        if file and allowed_file(file.filename):
            file_name = file.filename
            phones_list = csv_parser(file)

    elif request.method == 'GET':
        # отдаем список файлов с file_id
        # return jsonify(files_list)
        pass


@app.route('phones/<uuid:file_id>/', methods=['GET'])
def get_phones_json(file_id):
    if request.method == 'GET':
        # отдаем телефоны из файла file_id в формате json
        # return jsonify(phones)
        pass


if __name__ == '__main__':
    app.run()
