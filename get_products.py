from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
 
'''db_connect = create_engine('sqlite:///chinook.db')'''
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
         return {'employees': [1,2,3] } # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        return {'data':   {
        "details": {
			"icomoonbase": "icomoon",
			"icomoon": "icomoon",
			"intelbase": "vi",
			"secondary": "pro",
			 
		}
	}
}
         

class Employees_Name(Resource):
    def get(self):
     return {'data':    [ {
     "address": "B3",
     "Place":"Blr",
     "State":"kar"
     }
     ]
}    
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employeeDetail') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
