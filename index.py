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

@app.route('/find-group')
def find_group():
    return render_template("find-group.html")


