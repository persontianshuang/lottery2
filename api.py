from flask import Flask,jsonify
from db.mongoeng import Log
from db.settings import mg_lottery

from db.trans import trans

app = Flask(__name__)

def lastest(uid):
    last_time = mg_lottery.find({'uid':uid},{'_id': 0}).sort('progress', direction=-1)
    return list(last_time)[0]

@app.route('/all')
def index():
    # ids
    lottery_ids = ['001', '113', '002', '106','104','107']
    datas = [lastest(x) for x in lottery_ids]
    return jsonify(trans(datas))


@app.route('/single/<uid>')
def dtails(uid):
    uid = str(uid)
    data = lastest(uid)
    return jsonify(trans(data))

@app.route('/dtails/<uid>/<num>')
def dtails_num(uid,num):
    uid = str(uid)
    num = int(str(num).strip())
    last_num = mg_lottery.find({'uid': uid}, {'_id': 0}).sort('progress', direction=1).limit(num)
    data = list(last_num)
    return jsonify(trans(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
