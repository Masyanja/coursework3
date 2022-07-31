
from api.logger import get_logger

from flask import Blueprint, jsonify

from utils import load_posts, load_post

logger = get_logger('api_logger')


api_bp = Blueprint('api', __name__)
#api_logger = logging.getLogger('api_logger')


@api_bp.route("/api/post/")
def api_posts():
    posts = load_posts()
    logger.info('api_posts')
    return jsonify(posts)


@api_bp.route("/api/post/<int:pk>")
def api_post(pk):
    post = load_post(pk)
    logger.info(f'api_post{pk}')
    return jsonify(post)
