from flask import Flask
from config import Config


app = Flask(__name__)

app.config.from_object(Config)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

from .routes import main_bp
app.register_blueprint(main_bp)




