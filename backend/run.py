# backend/run.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend import create_app
from app.utils.helpers import ensure_upload_folder_exists

app = create_app()

ensure_upload_folder_exists(app)

if __name__ == '__main__':
    # Use environment variables for host and port, with defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    app.run(host=host, port=port, debug=debug)




