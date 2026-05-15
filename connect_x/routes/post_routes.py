from flask import Blueprint, redirect, flash, request, url_for,current_app
from flask_login import login_required, current_user
# from app import db
from extensions import db, bcrypt
from models.post import Post
from models.comment import Comment
from models.like import Like
import os
from werkzeug.utils import secure_filename

posts = Blueprint('posts', __name__)

@posts.route('/create_post', methods=['POST'])
@login_required
def create_post():

    content = request.form.get('content')

    image_file = request.files.get('image')

    filename = None

    # SAVE IMAGE

    if image_file and image_file.filename != '':

        filename = secure_filename(
            image_file.filename
        )

        upload_folder = os.path.join(
            current_app.root_path,
            'static/uploads/posts'
        )

        os.makedirs(
            upload_folder,
            exist_ok=True
        )

        image_path = os.path.join(
            upload_folder,
            filename
        )

        image_file.save(image_path)

    # CREATE POST

    post = Post(

        content=content,

        image=filename,

        author=current_user

    )

    db.session.add(post)

    db.session.commit()

    flash(
        'Post created successfully',
        'success'
    )

    return redirect(
        url_for('main.home')
    )


@posts.route('/like/<int:post_id>')
@login_required
def like_post(post_id):

    existing_like = Like.query.filter_by(
        user_id=current_user.id,
        post_id=post_id
    ).first()

    if existing_like:

        db.session.delete(existing_like)

    else:

        like = Like(
            user_id=current_user.id,
            post_id=post_id
        )

        db.session.add(like)

    db.session.commit()

    return redirect(url_for('main.home'))

@posts.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def comment(post_id):

    post = Post.query.get_or_404(post_id)

    comment_text = request.form.get('comment')

    if not comment_text:

        flash(
            'Comment cannot be empty',
            'danger'
        )

        return redirect(
            url_for('main.home')
        )

    # CREATE COMMENT

    new_comment = Comment(

        text=comment_text,

        user_id=current_user.id,

        post_id=post.id

    )

    db.session.add(new_comment)

    db.session.commit()

    flash(
        'Comment added successfully',
        'success'
    )

    return redirect(
        url_for('main.home')
    )