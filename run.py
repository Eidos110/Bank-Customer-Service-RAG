"""Main entry point for the application"""

from app.main import app
from app.config import Config
import os

if __name__ == "__main__":
    # Run the Flask application
    app.run(
        host=Config.FLASK_HOST,
        port=Config.FLASK_PORT,
        debug=Config.FLASK_DEBUG
    )