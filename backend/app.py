from flask import Flask, jsonify
from flask_cors import CORS
from services.image_processing_service import generate_dense_holds, get_holds_from_image
from services.route_generation_service import generateRoutes
from services.reachable_foot_area import calc_knee_angle, calc_hold_angle, calc_hip_angle, calc_max_hip_angle

from services.climber import Climber
from services.wall import Wall

import random
import copy

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/api/data')
def data():
    return jsonify({"message": "Ty hacked the back end!"})

@app.route('/api/generate_routes', methods=['GET'])
def api_generate_routes():
    try:
        # Initialize Wall and Climber
        newWall = Wall(id=1, height=400, width=500) #made it quite larger on purpose
        newClimber = Climber(newWall, height=180, upper_arm_length=40, forearm_length=30,
                          upper_leg_length=45, lower_leg_length=40, torso_height=80,
                          torso_width=50)

        routes = generateRoutes(newWall, newClimber)
        return jsonify({"reply": "this is not correctly calling the right function! Better use backend terminal rn. "})

    #     # # Set up a new wall with holds
    #     # wall.holds = get_holds_from_image()
    #     #

    #     #new wall with dense holds
    #     wall.holds = generate_dense_holds(wall)

    #     # generate routes
    #     routes = generateRoutes(wall, climber)

    #     print("Number of routes generated: ", len(routes))

    #     for position in routes: print(position.toString())

    #     finalPosition = routes[random.randint(1, len(routes))]

    #     finalRoute = [finalPosition.toString()]

    #     currentPosition = finalPosition
    #     parentPosition = currentPosition.parent_position
    #     iteration = 0
    #     while (currentPosition.parent_position != None):
    #         iteration += 1
    #         print("Iteration: ", iteration)
    #         print("Current position:", currentPosition.toString())
    #         print("Parent position: ", parentPosition.toString())
    #         finalRoute.insert(0, currentPosition.parent_position.toString())
    #         currentPosition = copy.deepcopy(parentPosition)
    #         parentPosition = currentPosition.parent_position

    #     # print(finalRoute)

    #     if not routes:
    #         raise ValueError("No routes could be generated with the current setup.")
    #     return jsonify({"routes": routes}) # best for frontend

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
