import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'asoianna09leou098qla;dfuap98p2qklda8ea'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCEMY_TRACK_MODIFICATIONS = False
