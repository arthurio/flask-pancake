import pytest
from flask import Flask
from flask_redis import FlaskRedis

from flask_pancake import FlaskPancake


@pytest.fixture
def _app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    FlaskRedis(app)
    FlaskPancake(app)
    yield app


@pytest.fixture
def app(_app):
    with _app.app_context():
        yield _app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def flask_pancake_cleanup(app: Flask):
    app.extensions["redis"].flushall()
    yield
    app.extensions["redis"].flushall()
