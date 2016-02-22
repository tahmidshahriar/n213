import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory, jsonify, session
import pymongo

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route("/", methods=['GET', 'POST'])
def hello():
    try:
        conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
        db = conn.test
        tim = db.tim
        myList = list(tim.find())
        print myList
        return render_template('./app.html', myList = myList)
    except:
        print "Failed"
        return render_template('./app.html', myList = [])

                 

@app.route("/val/<post_id>", methods=['GET', 'POST'])
def d(post_id):
    try:
        conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
        db = conn.test
        tim = db.tim
        data = {}
        data['time'] = post_id
        tim.insert(data)
        return redirect('/')
    except:
        print "Failed"
        return redirect('/')




if __name__ == '__main__':
    app.run(debug="True")
