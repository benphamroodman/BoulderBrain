from flask import Flask, jsonify
from flask_cors import CORS
from services.image_processing_service import get_holds_from_image, get_holds_main
# from services.image_processing_service import generate_dense_holds, get_holds_from_image
from services.route_generation_service import generateRoutes, process_final_routes, filter_routes_by_hold_overlap
from services.reachable_foot_area import calc_knee_angle, calc_hold_angle, calc_hip_angle, calc_max_hip_angle
from services.output_processing import output_route
from services.climber import Climber
from services.wall import Wall


import random
import copy

#gggg
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
        # image_path = 'services/files/example_wall.jpg'
        image_path = 'services/files/860.jpg'
        print("Loading wall and climber details...")
        wall = Wall(id=4, height=350, width=450, image_path=image_path) #made it quite larger on purpose
        climber = Climber(wall, height=180, upper_arm_length=40*(10/9), forearm_length=30*(10/9),
                          upper_leg_length=45*(10/9), lower_leg_length=40*(10/9), torso_height=80*(10/9),
                          torso_width=50*(10/9))

        # Set up a new wall with holds
        holds_path = f'services/result{wall.id}/holds'
        files_path = f'services/result{wall.id}'
        wall.holds,holds_map = get_holds_main(wall, image_path, holds_path, files_path)


        print("Generating routes...")
        routes = generateRoutes(wall, climber)
        holds_dict, routes_description_dict = process_final_routes(routes)
    
        # overlap_threshold = 30  # TODO: adjust where? Frontend? Try again when tree grows longer
        overlap_threshold = int(input("Insert your maximum overlap threshold: "))
        # print("OT:", overlap_threshold )
        print("Getting valid routes...")
        valid_routes = filter_routes_by_hold_overlap(holds_dict, overlap_threshold, wall)
        # print("Valid Routes:", valid_routes)    
        # Convert set to list to make it serializable
        valid_routes_list = list(valid_routes)
        print(f"Total of {len(valid_routes_list)} valid routes.")

        output_route(wall.holds, holds_map, valid_routes, wall.image_path, files_path)
        
        # return jsonify(valid_routes)
        return jsonify({'Valid Routes': valid_routes})


    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
