from flask import Flask, render_template, redirect, url_for, json
import requests
import json
from .scrape import ThrowInfo

app = Flask(__name__)

infotron = ThrowInfo()
parsed = infotron.parse_data()

@app.route('/')
def index():
    return render_template('index.html', array=parsed)
    
if __name__=='__main__':
    app.run(port=8080, debug = True)