from flask import Flask, render_template, jsonify, request

from api.views import api_bp
from utils import *


app = Flask(__name__)


@app.route("/main")
@app.route("/")
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route("/post/<int:pk>")
def show_post(pk):
    post = load_post(pk)
    comments = load_comments_by_post_id(pk)

    return render_template('post.html', post=post, comments=comments)


@app.route("/search/", methods=['GET'])
def search_word_post():
    search_word = request.args.get('search_word')
    print(search_word)
    posts = load_posts()
    found_posts = []
    for post in posts:
        if search_word.lower() in post["content"].lower():
            found_posts.append(post)

    return render_template('search.html', posts=found_posts, count=len(found_posts))


@app.route("/user-feed/<poster_name>", methods=['GET'])
def search_posts_by_user(poster_name):
    post = load_posts_by_poster_name(poster_name)
    print(post)
    return render_template('user-feed.html', posts=post)


app.register_blueprint(api_bp)
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def handle_bad_request(e):
    return 'Page not found', 400


if __name__ == '__main__':
    app.run(debug=True)
