from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo
)


# ================= FORGOT PASSWORD =================

class ForgotPasswordForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField(
        'Send Reset Link'
    )


# ================= RESET PASSWORD =================

class ResetPasswordForm(FlaskForm):

    password = PasswordField(
        'New Password',
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo(
                'password',
                message='Passwords must match'
            )
        ]
    )

    submit = SubmitField(
        'Reset Password'
    )