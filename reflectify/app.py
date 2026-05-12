import os
import random
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from werkzeug.utils import secure_filename

from config import Config
from models import db, User, JournalEntry
from forms import (
    RegisterForm,
    LoginForm,
    JournalForm,
    ForgotPasswordForm,
    ResetPasswordForm
)

# ---------------------------------------------------
# Flask App Setup
# ---------------------------------------------------

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# ---------------------------------------------------
# Login Manager
# ---------------------------------------------------

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'

login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# ---------------------------------------------------
# Home Route
# ---------------------------------------------------

@app.route('/')
def home():

    return redirect(url_for('login'))


# ---------------------------------------------------
# Register
# ---------------------------------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_user:

            flash(
                'Email already exists.',
                'danger'
            )

            return redirect(url_for('register'))

        hashed_password = generate_password_hash(
            form.password.data
        )

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        flash(
            'Account created successfully ✨',
            'success'
        )

        return redirect(url_for('login'))

    return render_template(
        'register.html',
        form=form
    )


# ---------------------------------------------------
# Login
# ---------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            flash(
                'Welcome back ✨',
                'success'
            )

            return redirect(url_for('dashboard'))

        else:

            flash(
                'Invalid email or password',
                'danger'
            )

    return render_template(
        'login.html',
        form=form
    )
# ---------------------------------------------------
# Forgot Password
# ---------------------------------------------------

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():

    form = ForgotPasswordForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user:

            return redirect(
                url_for(
                    'reset_password',
                    user_id=user.id
                )
            )

        else:

            flash(
                'No account found with this email',
                'danger'
            )

    return render_template(
        'forgot_password.html',
        form=form
    )
# ---------------------------------------------------
# Reset Password
# ---------------------------------------------------

@app.route(
    '/reset_password/<int:user_id>',
    methods=['GET', 'POST']
)

def reset_password(user_id):

    user = User.query.get_or_404(user_id)

    form = ResetPasswordForm()

    if form.validate_on_submit():

        hashed_password = generate_password_hash(
            form.password.data
        )

        user.password = hashed_password

        db.session.commit()

        flash(
            'Password updated successfully ✨',
            'success'
        )

        return redirect(url_for('login'))

    return render_template(
        'reset_password.html',
        form=form
    )
# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

@app.route('/dashboard')
@login_required
def dashboard():

    entries = JournalEntry.query.filter_by(
        user_id=current_user.id
    ).order_by(
        JournalEntry.created_at.desc()
    ).all()

    return render_template(
        'dashboard.html',
        entries=entries
    )


# ---------------------------------------------------
# New Journal Entry
# ---------------------------------------------------

@app.route('/new_entry', methods=['GET', 'POST'])
@login_required
def new_entry():

    form = JournalForm()

    # AI Style Reflection Prompts

    ai_prompts = [

        "🌸 What emotion stayed with you the longest today?",

        "✨ Describe a small moment today that felt meaningful.",

        "💭 What thoughts are taking up most of your mind right now?",

        "🌙 If today had a title, what would it be?",

        "🫶 What is something you needed today but didn’t ask for?",

        "🌱 What is one thing you are slowly healing from?",

        "📖 What conversation affected your mood today?",

        "☁️ What made you overthink today?",

        "💡 What lesson is life trying to teach you recently?",

        "🎯 What is one thing you want tomorrow’s version of you to remember?",

        "❤️ What made your heart feel full today?",

        "🌧️ What drained your energy today?",

        "🌈 What are you secretly hopeful about?",

        "🕊️ What helped you feel calm today?",

        "🔥 What motivated you today?",

        "🎵 What song best describes your current mood?",

        "📸 What moment do you wish you could relive today?",

        "💬 What is something you wish someone told you today?",

        "🌻 What are you grateful for at this moment?",

        "🚀 What is one step you took toward becoming a better version of yourself?"

    ]

    prompt = random.choice(ai_prompts)

    if form.validate_on_submit():

        image_filename = None
        audio_filename = None

        # ---------------------------------------------------
        # Image Upload
        # ---------------------------------------------------

        image = request.files.get('image')

        if image and image.filename != '':

            image_filename = secure_filename(
                image.filename
            )

            image.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    image_filename
                )
            )

        # ---------------------------------------------------
        # Audio Upload
        # ---------------------------------------------------

        audio = request.files.get('audio')

        if audio and audio.filename != '':

            audio_filename = secure_filename(
                audio.filename
            )

            audio.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    audio_filename
                )
            )

        # ---------------------------------------------------
        # Save Entry
        # ---------------------------------------------------

        entry = JournalEntry(

            title=form.title.data,

            content=form.content.data,

            mood=form.mood.data,

            image=image_filename,

            audio=audio_filename,

            user_id=current_user.id
        )

        db.session.add(entry)

        db.session.commit()

        flash(
            'Journal entry saved successfully ✨',
            'success'
        )

        return redirect(url_for('dashboard'))

    return render_template(
        'new_entry.html',
        form=form,
        prompt=prompt
    )


# ---------------------------------------------------
# View Entry
# ---------------------------------------------------

@app.route('/entry/<int:id>')
@login_required
def view_entry(id):

    entry = JournalEntry.query.get_or_404(id)

    # Security Check

    if entry.user_id != current_user.id:

        flash(
            'Unauthorized Access',
            'danger'
        )

        return redirect(url_for('dashboard'))

    return render_template(
        'view_entry.html',
        entry=entry
    )


# ---------------------------------------------------
# Delete Entry
# ---------------------------------------------------

@app.route('/delete/<int:id>')
@login_required
def delete_entry(id):

    entry = JournalEntry.query.get_or_404(id)

    if entry.user_id != current_user.id:

        flash(
            'Unauthorized Access',
            'danger'
        )

        return redirect(url_for('dashboard'))

    # Delete Image

    if entry.image:

        image_path = os.path.join(
            app.config['UPLOAD_FOLDER'],
            entry.image
        )

        if os.path.exists(image_path):

            os.remove(image_path)

    # Delete Audio

    if entry.audio:

        audio_path = os.path.join(
            app.config['UPLOAD_FOLDER'],
            entry.audio
        )

        if os.path.exists(audio_path):

            os.remove(audio_path)

    db.session.delete(entry)

    db.session.commit()

    flash(
        'Journal entry deleted',
        'info'
    )

    return redirect(url_for('dashboard'))


# ---------------------------------------------------
# Logout
# ---------------------------------------------------

@app.route('/logout')
@login_required
def logout():

    logout_user()

    flash(
        'Logged out successfully',
        'info'
    )

    return redirect(url_for('login'))


# ---------------------------------------------------
# Run Flask App
# ---------------------------------------------------

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(debug=True)