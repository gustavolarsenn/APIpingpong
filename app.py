from flask import Flask, jsonify,request

app = Flask(__name__)


@app.route('/pingpong', methods=['GET'])
def show():
    return "Ping ou pong?"
    
@app.route('/pingpong/<string:req>', methods=['GET'])    
def convert(req): 
    if req.upper() == 'PING':
        res = "Pong"
    elif req.upper() == "PONG":
        res = "Ping"
    else: 
        res = "Nem ping nem pong!"
    return res

app.run(port=5000, host='localhost', debug=True)