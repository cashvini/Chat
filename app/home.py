import re
from app import app
from flask import Flask,escape,render_template,jsonify, request,make_response
from datetime import datetime as dt
from app import model
from .model import User, db
from flask_login import current_user, login_user,logout_user



@app.route('/')
def home():
    return render_template('index.html')
    
#load chat view page after succesfull login
@app.route('/chat_view/', methods=['GET','POST'])
def chat_view():
    if current_user.is_authenticated:  
            return render_template('chat_view.html')
    if request.method=='POST':
       username= request.form['uname']
       password= request.form['password']
       
       if username and password:
        existing_user = User.query.filter(
            User.username == username or User.email == password
             ).first()
        if existing_user:
            login_user(existing_user)
            return render_template('chat_view.html',uname=username)
        else:
            message="no user. please register"
            return render_template('login.html',message=message)          
       
#login page
@app.route('/login_page/')
def login_page():
    if current_user.is_authenticated: 
            return render_template('chat_view.html',uname=current_user.name)
    return render_template('login.html')

#registration page
@app.route('/register_page/')
def register_page():
    return render_template('register.html')

# login after submit registration form
@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method=='POST':
       name= request.form['name']
       email= request.form['email']
       username= request.form['uname']
       password = request.form['password']
    
    if username and email:
        existing_user = User.query.filter(
        User.username == username or User.email == email
        ).first()
        if existing_user:
            message="User already exists"
            return render_template('register.html',message=message)
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(not re.fullmatch(regex, email)):
            message ="Invalid email address"
            return render_template('register.html', message=message)              
        
        if len(password) < 8:
                message = "Password should be at least 8 characters long"
                return render_template('register.html', message=message)
            
        
    # Create an instance of the User class
        new_user = User(
        
        name=name,
        email=email,
        created_date=dt.now(),
        username=username,
        password=password
        )   
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit() 
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')
       
    
