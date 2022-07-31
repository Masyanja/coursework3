from flask import Blueprint, jsonify

from utils import load_posts, load_post

api_blueprint = Blueprint("api", __name__, url_prefix='/api')


@api_blueprint.route("/post/")
def api_posts():
    posts = load_posts()

    return jsonify(posts)


@api_blueprint.route("/post/<int:pk>")
def api_post(pk):
    post = load_post(pk)

    return jsonify(post)
