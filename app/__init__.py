from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # import hello_world_bp variable from file called routes
    from .routes import hello_world_bp

    # register the variable flask so it knows to use the blueprint for our route
    app.register_blueprint(hello_world_bp)

    return app
