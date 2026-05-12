from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
    SelectField,
    FileField
)

from wtforms.validators import DataRequired, Email,EqualTo

class RegisterForm(FlaskForm):

    username = StringField(
        'Username',
        validators=[DataRequired()]
    )

    email = StringField(
        'Email',
        validators=[Email()]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )

    submit = SubmitField('Register')


class LoginForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[Email()]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )

    submit = SubmitField('Login')


class JournalForm(FlaskForm):

    title = StringField(
        'Title',
        validators=[DataRequired()]
    )

    content = TextAreaField(
        'Content',
        validators=[DataRequired()]
    )

    mood = SelectField(
        'Mood',
        choices=[
            ('Happy', '😀 Happy'),
            ('Sad', '😔 Sad'),
            ('Calm', '😌 Calm'),
            ('Angry', '😡 Angry')
        ]
    )

    image = FileField('Photo')

    audio = FileField('Voice Note')

    submit = SubmitField('Save Entry')

# -----------------------------------
# Forgot Password Form
# -----------------------------------

class ForgotPasswordForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField(
        'Continue'
    )


# -----------------------------------
# Reset Password Form
# -----------------------------------

class ResetPasswordForm(FlaskForm):

    password = PasswordField(
        'New Password',
        validators=[DataRequired()]
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