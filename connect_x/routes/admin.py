from flask import Blueprint, render_template, redirect, flash, url_for

from flask_login import login_required, current_user

from extensions import db

from models.user import User
from models.post import Post
from models.comment import Comment


admin = Blueprint('admin', __name__)


# ================= ADMIN CHECK =================

def admin_required():

    return current_user.is_authenticated and current_user.role == 'admin'


# ================= DASHBOARD =================

@admin.route('/admin')
@login_required
def dashboard():

    if not admin_required():

        flash('Access Denied', 'danger')

        return redirect(url_for('main.home'))

    users = User.query.all()

    posts = Post.query.order_by(
        Post.created_at.desc()
    ).all()

    comments = Comment.query.all()

    return render_template(
        'admin_dashboard.html',
        users=users,
        posts=posts,
        comments=comments
    )


# ================= DELETE POST =================

@admin.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):

    if not admin_required():

        flash('Access Denied', 'danger')

        return redirect(url_for('main.home'))

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)

    db.session.commit()

    flash('Post Deleted Successfully', 'success')

    return redirect(url_for('admin.dashboard'))


# ================= DELETE COMMENT =================

@admin.route('/delete_comment/<int:comment_id>')
@login_required
def delete_comment(comment_id):

    if not admin_required():

        flash('Access Denied', 'danger')

        return redirect(url_for('main.home'))

    comment = Comment.query.get_or_404(comment_id)

    db.session.delete(comment)

    db.session.commit()

    flash('Comment Deleted Successfully', 'success')

    return redirect(url_for('admin.dashboard'))