from flask_wtf import FlaskForm

from wtforms import (
    TextAreaField,
    SubmitField
)

from flask_wtf.file import (
    FileField,
    FileAllowed
)

from wtforms.validators import DataRequired


class PostForm(FlaskForm):

    content = TextAreaField(
        'Content',
        validators=[DataRequired()]
    )

    image = FileField(
        'Post Image',
        validators=[
            FileAllowed(
                ['jpg', 'png', 'jpeg', 'gif'],
                'Images only!'
            )
        ]
    )

    submit = SubmitField(
        'Create Post'
    )