from flask import render_template
from . import core, models


@core.route('/')
def post_list():
    """
    List of blog posts
    """
    posts = models.Post.query.all()


    return render_template(
        'post_list.html', posts=posts)