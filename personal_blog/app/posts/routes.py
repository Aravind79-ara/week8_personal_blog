from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.posts import bp
from app.posts.forms import PostForm
from app import db
from app.models import Post
from app.comments.forms import CommentForm

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('posts/create.html', form=form)
@bp.route('/<int:id>')
def view(id):   # ✅ FUNCTION NAME MUST BE "view"
    post = Post.query.get_or_404(id)
    form = CommentForm()
    return render_template('posts/post.html', post=post, form=form)