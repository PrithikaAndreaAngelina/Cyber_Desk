from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
import numpy as np
import sys

flask_app = Flask(_name_)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Cyber Desk", 
		  description = "Intrusion Detection System")

name_space = app.namespace('Detection', description='Detection APIs')

model = app.model('Detection params', 
				  {'src_bytes': fields.Float(required = True, 
				  							   description="src_bytes", 
    					  				 	   help="The field cannot be blank"),
				  'dst_bytes': fields.Float(required = True, 
				  							   description="dst_bytes", 
    					  				 	   help="The field cannot be blank"),
				  'is_host_login': fields.Float(required = True, 
				  							description="is_host_login", 
    					  				 	help="The field cannot be blank"),
				  'is_guest_login': fields.Float(required = True, 
				  							description="is_guest_login", 
    					  				 	help="The field cannot be blank")
                                            'dst_bytes': fields.Float(required = True, 
				  							   description="dst_bytes", 
    					  				 	   help="The field cannot be blank"),
				  'diff_srv_rate': fields.Float(required = True, 
				  							description="diff_srv_rate", 
    					  				 	help="The field cannot be blank"),
				  'srv_diff_host_rate': fields.Float(required = True, 
				  							description="srv_diff_host_rate", 
    					  				 	help="The field cannot be blank")
                  'flag': fields.Float(required = True, 
				  							description="flag", 
    					  				 	help="The field cannot be blank")})

classifier = joblib.load('classifier.joblib')

@name_space.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(model)		
	def post(self):
		try: 
			formData = request.json
			data = [val for val in formData.values()]
			detection = classifier.detection(np.array(data).reshape(1, -1))
			types = { 0: "DOS", 1: "R2L", 2: "U2R",3:"probing"}
			response = jsonify({
				"statusCode": 200,
				"status": "Detected",
				"result": "The type of Attack is: " + types[detection[0]]
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Not Detected",
				"error": str(error)
			})