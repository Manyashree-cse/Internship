from flask import Blueprint, render_template,request,redirect,url_for,flash, current_app
  
from models.post import Post
from models.user import User

from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename
from extensions import db
main = Blueprint('main', __name__)

# ================= HOME =================

@main.route('/')
def home():

    posts = Post.query.order_by(
        Post.created_at.desc()
    ).all()

    return render_template(
        'home.html',
        posts=posts
    )


# ================= PROFILE =================

@main.route('/profile/<int:user_id>')
def profile(user_id):

    user = User.query.get_or_404(user_id)

    return render_template(
        'profile.html',
        user=user
    )

# ================= UPDATE PROFILE PIC =================

@main.route('/upload_profile_pic', methods=['POST'])
@login_required
def upload_profile_pic():

    if 'profile_pic' not in request.files:

        flash('No file selected', 'danger')

        return redirect(
            url_for(
                'main.profile',
                user_id=current_user.id
            )
        )

    file = request.files['profile_pic']

    if file.filename == '':

        flash('No file selected', 'danger')

        return redirect(
            url_for(
                'main.profile',
                user_id=current_user.id
            )
        )

    filename = secure_filename(file.filename)

    upload_path = os.path.join(
        current_app.config['UPLOAD_FOLDER'],
        filename
    )

    file.save(upload_path)

    current_user.profile_pic = filename

    db.session.commit()

    flash(
        'Profile Picture Updated',
        'success'
    )

    return redirect(
        url_for(
            'main.profile',
            user_id=current_user.id
        )
    )