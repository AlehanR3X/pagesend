from flask import Flask, jsonify
import pytest

def create_app():
    app = Flask(__name__)

    @app.route('/api/test', methods=['GET'])
    def test_route():
        return jsonify({"message": "Test successful!"})

    return app

def test_test_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/test')
    assert response.status_code == 200
    assert response.json == {"message": "Test successful!"}