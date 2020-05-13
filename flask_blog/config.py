import os


class Config:
    SECRET_KEY = '2fdec672e37de1f17ebe9287eb6caec8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email')
    MAIL_PASSWORD = os.environ.get('pass')