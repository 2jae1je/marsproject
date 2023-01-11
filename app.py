from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb://musfiah:najaemin@ac-xpiom7m-shard-00-00.cthitbn.mongodb.net:27017,ac-xpiom7m-shard-00-01.cthitbn.mongodb.net:27017,ac-xpiom7m-shard-00-02.cthitbn.mongodb.net:27017/?ssl=true&replicaSet=atlas-xe2201-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_recieve = request.form['name_give']
    address_recieve = request.form['address_give']
    size_recieve = request.form['size_give']
    doc = {
        'name' : name_recieve,
        'address' : address_recieve,
        'size' : size_recieve
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)