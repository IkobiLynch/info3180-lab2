from flask import Flask

DEBUG = True

app = Flask(__name__)

app.config.from_object(__name__)

from app import views