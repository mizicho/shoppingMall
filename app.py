from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      

@app.route('/')
def home():
   return render_template('1week.html')

@app.route('/shoppingMall', methods=['POST'])
def write_orders():
    name_receive = request.form['name_give']
    select_receive = request.form['select_give']
    address_receive = request.form['address_give']
    phoneNumber_receive = request.form['phoneNumber_give']

    doc = {
        'name': name_receive,
        'select': select_receive,
        'address': address_receive,
        'phoneNumber': phoneNumber_receive
    }
    print(doc)
    db.shoppingMall.insert_one(doc)
    return jsonify({'result':'success', 'msg':'주문이 완료되었습니다'})

@app.route('/shoppingMall', methods=['GET'])
def read_orders():

    orders = list(db.shoppingMall.find({},{'_id':0}))
    return jsonify({'result':'success', 'all_orders':orders})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)