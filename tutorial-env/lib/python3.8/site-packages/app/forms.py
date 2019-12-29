from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class TwitInfoForm(FlaskForm):
    username = StringField('Please Enter Your Username Below', validators=[DataRequired()])
    submit = SubmitField('Submit')

class InstaInfoForm(FlaskForm):
    username = StringField('Please Enter Your Username Below', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ModalForm(FlaskForm):
    code = StringField('Please enter the code sent to your email', validators=[DataRequired()])
    submit = SubmitField('Submit')