from compound_interest import app
from flask import render_template, redirect, url_for, flash, request, jsonify
from compound_interest.models import User, Investment, calculate_compound_interest
from compound_interest.forms import RegisterForm, LoginForm, DeleteInvestmentForm, AddInvestmentForm
from compound_interest import db
from flask_login import login_user, logout_user, login_required, current_user
import bcrypt
import uuid



@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')



@app.route('/investments/', methods=['GET', 'DELETE'])
@login_required
def investments_page():
    form = DeleteInvestmentForm()
    if request.method == "DELETE":
        #Delete Investment Logic
        pass

        return redirect(url_for('investments_page'))

    if request.method == "GET":
        investments = db.investments.find({"user_id" : current_user._id})
        return render_template('investments.html', investments = investments, form = form)



@app.route('/add_investment/', methods=['GET', 'POST'])
@login_required
def add_investment():
    form = AddInvestmentForm()
    if form.validate_on_submit():
        initial_deposit=form.initial_deposit.data
        monthly_deposit=form.monthly_deposit.data
        yearly_interest=form.yearly_interest.data
        years_of_investment=form.years_of_investment.data
        total_deposit, total_interest, total_money = calculate_compound_interest(initial_deposit, monthly_deposit, yearly_interest, years_of_investment)
        investment = Investment(
            _id=uuid.uuid4(),
            user_id=current_user._id,
            initial_deposit=initial_deposit,
            monthly_deposit=monthly_deposit,
            yearly_interest=yearly_interest,
            years_of_investment=years_of_investment,
            total_deposit=total_deposit,
            total_interest=total_interest,
            total_money=total_money
            )
        db.investments.insert_one(jsonify(investment))
        flash('Investment added successfully.', category='success')
        return redirect(url_for('investments_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating an investment: {err_msg}', category='danger')
    return render_template('add_investment.html', form=form)



@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password=form.password1.data
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        user = User(
            _id=uuid.uuid4(),
            username=username,
            email=email,
            password=hashed_pw
            )
        if user.isuserexist(username) or user.isemailexist(email):
            flash(f'There was an error with creating a user: username or email alredy exist', category='danger')
            return redirect(url_for('register_page'))   
        db.users.insert_one(jsonify(user))
        login_user(user.username)
        flash(f"Account created successfully! You are now logged in as {user.username}", category='success')
        return redirect(url_for('investments_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)



@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user and user.verifypw(form.password.data):
            login_user(user.username)
            flash(f'Success! You are logged in as: {user.username}', category='success')
            return redirect(url_for('investments_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    elif form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with login: {err_msg}', category='danger')
    
    return render_template('login.html', form=form)



@app.route('/logout/')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))










