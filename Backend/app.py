from flask import Flask,request,jsonify
from flask_cors import CORS
import json
import os

app=Flask(__name__)
CORS(app)
CONFIG_FILES="config.json"
#creating empty config file if it is not in exist
if not  os.path.exists(CONFIG_FILES):
    with open(CONFIG_FILES,"w") as f:
        json.dump({},f)

@app.route('/')
def home():
    return "backend running"

#start remainder
@app.route('/start',methods=["POST"])
def start():
    data=request.json
    with open(CONFIG_FILES,'w') as f:
        json.dump(data,f)
    return jsonify({
        "status":"success",
        "message":"remainder started",
        "data":data
    })

