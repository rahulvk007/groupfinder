import re
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, make_response
from pymongo import MongoClient

app = Flask(__name__, static_folder='static')

cluster = MongoClient(
    "mongodb+srv://rahulvk:rvk4551@cluster0.c8dkc.mongodb.net/mydb?retryWrites=true&w=majority")

db = cluster["groupfinder"]
collection = db["groups"]

@app.route('/')
def home():
    return render_template('home-menu.html')

@app.route('/find-group',methods=['POST','GET'])
def find_group():
    if request.method == "POST":
        slot = request.form['slot']
        faculty = request.form['faculty']
        course_code = request.form['course-code']
        res = collection.find({"slot":slot,"faculty":faculty,"course_code":course_code})
        if res:
            links = [i for i in res]
            return render_template("view-group.html",l = links)
    result = collection.find()
    r = [i for i in result]
    return render_template("find-group.html", a=r)

@app.route('/submit-group', methods=['POST','GET'])
def submit_group():
    if request.method == "POST":
        slot = request.form['slot']
        faculty = request.form['faculty']
        course_code = request.form['course-code']
        link = request.form['link']
        desc = request.form['select']
        collection.insert_one({"slot":slot,"faculty":faculty,"course_code":course_code,"link":link,"desc":desc})
        return redirect('/')
    result = collection.find()
    r = [i for i in result]
    return render_template("submit-group.html",a=r)

