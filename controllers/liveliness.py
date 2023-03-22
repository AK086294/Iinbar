from flask import Blueprint

liveLinessController = Blueprint('liveliness',__name__)

@liveLinessController.route("/isAlive")
def asd():
    return "True"