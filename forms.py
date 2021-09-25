from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, DateField, BooleanField


# from wtforms.validators import DataRequired, Length


class MemberForm(FlaskForm):
    email = StringField('email')
    referee = StringField('referee')
    created_at = DateField('created_at')
    approved = BooleanField('approved')
    approved_at = DateField('approved_at')
    recaptcha = RecaptchaField()
    submit = SubmitField('submit')
