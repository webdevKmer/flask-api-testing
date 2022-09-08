#!/usr/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_albums = "https://jsonplaceholder.typicode.com/albums"
url_todos = "https://jsonplaceholder.typicode.com/todos"
url_comments = "https://jsonplaceholder.typicode.com/comments"
url_photos = "https://jsonplaceholder.typicode.com/photos"

def get_data(url):
    response = json.loads(requests.request("GET", url).text)
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def get_users():
    users = get_data(url_users)
    return render_template("users.html", users=users)

@app.route("/posts")
def get_posts():
    posts = get_data(url_posts)
    return render_template("posts.html", posts=posts)

@app.route("/albums")
def get_albums():
    albums = get_data(url_albums)
    return render_template("albums.html", albums=albums)


@app.route("/todos")
def get_todos():
    todos = get_data(url_todos)
    nbr_todos = len(todos)
    return render_template("todos.html", todos=todos, nbr_todos=nbr_todos)


@app.route("/comments")
def get_comments():
    comments = get_data(url_comments)
    nbr_comments = len(comments)
    return render_template("comments.html", comments=comments, nbr_comments=nbr_comments)


@app.route("/photos")
def get_photos():
    photos = get_data(url_photos)
    nbr_photos = len(photos)
    return render_template("photos.html", photos=photos, nbr_photos=nbr_photos)
app.run(debug=True, host="0.0.0.0", port=8080)
