from flask import render_template
from app.main import bp
from app.models import Post
from flask_login import login_required

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('main/index.html', posts=posts)
  
@bp.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html')