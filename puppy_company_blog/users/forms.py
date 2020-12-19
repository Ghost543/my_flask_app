from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired,Email,EqualTo

from flask_login import current_user
from puppy_company_blog.models import Users

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('User Name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_conf')])
    pass_conf = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your Email has been Registered Already!')
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username has been Registered Already!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('User Name',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update Profile')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your Email has been Registered Already!')
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username has been Registered Already!')
