from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import app as main_blueprint  # Importar el blueprint llamado "app" desde routes.py
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)