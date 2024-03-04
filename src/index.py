from flask import Flask
from flask import jsonify
from flask import request as req

from request_grpc import run
from dotenv import load_dotenv

import threading
import requests
import json
import time
import os

load_dotenv()
# instance of flask application
app = Flask(__name__)

# home route that returns below text 
# when root url is accessed

@app.route("/download/<file>" , methods=['GET', 'POST'])
def downloadResource(file):
    return file

@app.route("/connect" , methods=['GET', 'POST'])
def connect():
    try:
        url = os.getenv('URL_PEERSU')
        data = req.json["body"][0]
        response = requests.post('http://' + url + '/pedirRecurso', json={"body": data})
        return response.text
    except:
        return "404"
    
@app.route("/pedirRecurso" , methods=['GET', 'POST'])
def pedirRecurso():
    file = req.json["body"]
    data = run(file)
    return data

if __name__ == '__main__':
    
    app.run(debug=True, port=os.getenv('PORT'))
    