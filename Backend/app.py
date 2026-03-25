from flask import Flask,request,jsonify
from flask_cors import CORS
import json
import os

app=Flask(__name__)
CORS(app)
