from flask import Flask, render_template, request
from app import app

#Space to load database


#routing starts
@app.route('/')
@app.route('/index')
def index():
	post = {"Author":"Manu",
			"Title":"Hello Web",
			"post":"This is a sample text to say Hello to the web"}
	return render_template("index.html", post=post)


