import os
from flask import Flask
from app.routes import app as main_routes  # Importa la variable "app" del blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    return app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=port)