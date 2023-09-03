from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from compound_interest.models import User, db


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = db.users.find({"username": username_to_check})
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email = db.users.find({"email": email_address_to_check})
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class AddInvestmentForm(FlaskForm):
    initial_deposit = FloatField(label='Initial Deposit:', validators=[DataRequired()])
    monthly_deposit = FloatField(label='Monthly Deposit:', validators=[DataRequired()])
    yearly_interest = FloatField(label='Yearly Interest:', validators=[DataRequired()])
    years_of_investment = IntegerField(label='Years of Investment:', validators=[DataRequired()])
    submit = SubmitField(label='Add Investment')

class DeleteInvestmentForm(FlaskForm):
    submit = SubmitField(label='Delete')

