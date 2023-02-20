from flask import Flask
import os

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LEGTH'] = 16 * 1024 * 1024

