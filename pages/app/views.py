from flask import Flask, render_template, request, redirect, url_for
from app import app
from pymongo import MongoClient
from bson import ObjectId

#Space to load database
client = MongoClient()
db = client.pages

#routing starts
@app.route('/')
@app.route('/index')
def index():
	#post = {"Author":"Manu",
	#		"Title":"Hello Web",
	#		"post":"This is a sample text to say Hello to the web"}
	posts = db.posts.find()
	return render_template("index.html", posts=posts)

@app.route('/post')
def post():
	return render_template("post.html")

@app.route('/post_submit', methods=['GET', 'POST'])
def post_submit():
	if request.method == 'POST':
		#return "Oops! you are on the wrong side of the internet!"
		title = request.form.get('title')
		content = request.form.get('content')
		db.posts.insert({ "author":"Manu", "title":title, "content":content})
		return redirect(url_for('index'))
		#return title+":"+content
	else:
		return "Broken :("

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	if request.method == 'GET':
		posts = db.posts.find()
		return render_template("admin.html", posts=posts)
	else:
		posts_to_be_deleted = request.form.getlist("posts")
		for ids in posts_to_be_deleted:
		#return "In the making"	
			 db.posts.remove({'_id':ObjectId(ids)})
		posts = db.posts.find()
		return render_template("admin.html", posts=posts)
	


