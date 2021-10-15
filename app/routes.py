from flask import Blueprint

# making hello world blueprint
hello_world_bp = Blueprint("hello_world", __name__)

# define an endpoint
# create a blueprint decorator, make the route "hello-world" which accept GET request


@hello_world_bp.route("/hello-world", methods=["GET"])
def get_hello_world():
    response = "Hello World!"
    return response


# GET method & JSON format
@hello_world_bp.route("/hello-world/JSON", methods=["GET"])
def hello_world_json():
    return{
        "name": "Zandra",
        "message": "Hi",
    }, 200
