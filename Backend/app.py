from flask import Flask,request,jsonify
from flask_cors import CORS
import json
import os

app=Flask(__name__)
CORS(app)

CONFIG_FILES=os.path.join(os.path.dirname(__file__),"config.json")

#creating empty config file if it is not in exist
if not  os.path.exists(CONFIG_FILES):
    with open(CONFIG_FILES,"w") as f:
        json.dump([],f)

@app.route('/')
def home():
    return "backend running"

#start remainder
@app.route('/start',methods=["POST"])
def start():
    data=request.json
    try:
        with open(CONFIG_FILES,"r")as f:
            remainders=json.load(f)
    except:
        remainders=[]
    if not isinstance(remainders,list):
        remainders=[]
    remainders.append(data)

    with open(CONFIG_FILES,"w")as f:
        json.dump(remainders,f,indent=4)
    return jsonify({
        "status":"success",
        "message":"Remainder Started",
        "data":data
    })



#stop remainder
@app.route('/stop',methods=["POST"])
def stop():
    with open(CONFIG_FILES,"w") as f:
        json.dump([],f)
    return jsonify({
        "status":"success",
        "message":"Remainder Stopped"
    })

if __name__=="__main__":
    app.run(debug=True)