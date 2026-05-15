from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    url_for,
    request
)

from flask_login import (
    login_user,
    logout_user
)

from extensions import db, bcrypt

from models.user import User

from forms.auth_forms import (
    RegisterForm,
    LoginForm
)

from forms.reset_forms import (
    ForgotPasswordForm,
    ResetPasswordForm
)

auth = Blueprint('auth', __name__)


# ================= REGISTER =================

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode('utf-8')

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash(
            'Registration Successful',
            'success'
        )

        return redirect(url_for('auth.login'))

    return render_template(
        'register.html',
        form=form
    )


# ================= LOGIN =================

@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            flash(
                'Login Successful',
                'success'
            )

            return redirect(
                url_for('main.home')
            )

        flash(
            'Invalid Credentials',
            'danger'
        )

    return render_template(
        'login.html',
        form=form
    )


# ================= LOGOUT =================

@auth.route('/logout')
def logout():

    logout_user()

    flash(
        'Logged out successfully',
        'success'
    )

    return redirect(
        url_for('auth.login')
    )


# ================= FORGOT PASSWORD =================

@auth.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():

    form = ForgotPasswordForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user:

            return redirect(
                url_for(
                    'auth.reset_password',
                    user_id=user.id
                )
            )

        flash(
            'Email not found',
            'danger'
        )

    return render_template(
        'forgot_password.html',
        form=form
    )


# ================= RESET PASSWORD =================

@auth.route('/reset_password/<int:user_id>', methods=['GET', 'POST'])
def reset_password(user_id):

    user = User.query.get_or_404(user_id)

    form = ResetPasswordForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode('utf-8')

        user.password = hashed_password

        db.session.commit()

        flash(
            'Password reset successful',
            'success'
        )

        return redirect(
            url_for('auth.login')
        )

    return render_template(
        'reset_password.html',
        form=form
    )