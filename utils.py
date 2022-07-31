import json


def load_json(filename):
    with open(filename, encoding='utf8') as file:
        return json.load(file)


def load_posts():
    data = load_json('data/data.json')

    return data


def load_post(pk):
    for post in load_posts():
        if post['pk'] == pk:
            return post

    return None


def load_posts_by_poster_name(poster_name):
    posts = []
    for post in load_posts():
        if post['poster_name'] == poster_name:
            posts.append(post)
    return posts


def load_comments():
    data = load_json('data/comments.json')

    return data


def load_comments_by_post_id(pk):
    comments = []
    for comment in load_comments():
        if comment['post_id'] == pk:
            comments.append(comment)
    return comments
