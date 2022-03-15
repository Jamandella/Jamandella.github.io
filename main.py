from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import json
import mysql.connector


app = Flask(__name__)
api = Api(app)
CORS(app)
#protocol//[hosts][ILikeTurtles][turtles]

class Quotes(Resource):
    """First test class"""

    @app.route('/test/')
    def test():
        param = request.args.get('param')
        return json.dumps({'success':True, 'param': param}), 200, {'ContentType':'application/json'}

    @app.route('/login/')
    def login():
        username = request.args.get('username')

    def get(self):

        cnx = mysql.connector.connect(user='root', password='thecolorblue970710',
                                      host='127.0.0.1',
                                      database='ILikeTurtles')
        mycursor = cnx.cursor()

        mycursor.execute("SELECT * FROM User")

        myresult = mycursor.fetchall()
        cnx.close()

        return jsonify({
            "User" : str(myresult),
            "Hello": "world",
            #query_parap: {value}
            })
 #   def protocol(self):
 #       return jdbc:mysql:replication//myUser:myPassword@[address=(host=myHost1)(port=1111)(key1=value1)]

    def post():
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201

api.add_resource(Quotes, '/')
#api.add_resource(Square, '/square/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
