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
    
# if __name__=='__main__':
#     app.run(port=8080, debug = True)