import os


class Config():
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'asoianna09leou098qla;dfuap98p2qklda8ea'
