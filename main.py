from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos = {}

# Parser for form data
form_parser = reqparse.RequestParser()
form_parser.add_argument("likes", type=int, help="Number of likes is required", location="form")
form_parser.add_argument("title", type=str, location="form")

# Parser for JSON data
json_parser = reqparse.RequestParser()
json_parser.add_argument("likes", type=int, help="Number of likes is required", location="json")
json_parser.add_argument("title", type=str, location="json")

class Video(Resource):
    def get(self, video_id):
        if video_id in videos:
            return jsonify(videos[video_id])
        else:
            return {"message": "Video not found"}, 404
    
    def put(self, video_id):
        if request.is_json:
            args = json_parser.parse_args()
        else:
            args = form_parser.parse_args()
        
        if not args["likes"]:
            return {"message": "Number of likes is required"}, 400
        
        videos[video_id] = args
        return {"video_id": video_id, **args}, 201

api.add_resource(Video, '/video/<string:video_id>')

if __name__ == "__main__":
    app.run(debug=True)
