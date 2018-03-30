from flask import render_template
from . import core, models


@core.route('/authors')
def author_list():
    """
    List of blog authors
    """
    authors = models.Author.query.all()

    return render_template(
        'author_list.html', authors=authors)


@core.route('/posts')
def post_list():
    """
    List of blog posts
    """
    posts = models.Post.query.all()

    return render_template('post_list.html', posts=posts)


@core.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = models.Post.query.get_or_404(post_id)

    return render_template('post_detail.html', post=post)