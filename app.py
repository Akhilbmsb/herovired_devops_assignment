from flask import Flask,request
import hashlib
from flask import jsonify
from pymongo import MongoClient

app = Flask(__name__)
# client = MongoClient('')
# db = client.
# db = client['megashop']
# collection = db['items']

@app.route('/hello')
def helloRoute():
    return jsonify('Hello World')

# @app.route('/items', methods=['POST'])
# def postItemRoute():
#     item = request.json
#     collection.insert_one(item)
#     return jsonify({'message': 'Added Successfully'})    


if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')    
