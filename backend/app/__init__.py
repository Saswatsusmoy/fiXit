from flask import Flask
from flask_cors import CORS
from config import Config
from .routes import main
from .utils.helpers import ensure_upload_folder_exists
import nltk

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app)
    
    app.register_blueprint(main)
    
    ensure_upload_folder_exists(app)
    
    # Download necessary NLTK data
    nltk.download('vader_lexicon', quiet=True)
    
    return app
