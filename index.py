from flask import Flask, render_template, request, redirect, send_from_directory, url_for, make_response
from pymongo import MongoClient

app = Flask(__name__, static_folder='static')

@app.route('/')
def resume():
    return render_template('home.html')

app.run()