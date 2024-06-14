from flask import jsonify, Blueprint
from app.controllers import Weathercontroller

main = Blueprint('main',__name__)

@main.route('/weather', methods=["GET"])
def get_weather_data():
    data = Weathercontroller.fetch_weather()
    
    print(jsonify(data))

    return jsonify(data)