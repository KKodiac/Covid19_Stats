from flask import Flask, render_template, redirect, url_for, json
import requests
import json
app = Flask(__name__)


@app.route('/')
def index():
    test = [1,2,3,4]
    return render_template('index.html', test=json.dumps(test))
    
if __name__=='__main__':
    app.run(port=8080, debug = True)