from flask import Flask, render_template, redirect, url_for, json
import requests
import json
from .scrape import ThrowInfo

app = Flask(__name__)

@app.route('/')
def index():
    infotron = ThrowInfo()
    datarray_all, datarray_chart = infotron.parse_data()
    return render_template('index.html', array=json.dumps(datarray_chart), array_all=json.dumps(datarray_all))

@app.route('/World')
def world():
    infortron = ThrowInfo()
    datarry_chart = infortron.parse_data()
    return render_template('world.html', warray=json.dumps(datarry_chart))
    
def run():
    app.run(port=8080, debug = True)