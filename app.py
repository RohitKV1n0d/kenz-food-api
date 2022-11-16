#flask boilerpalte
from flask import Flask, request, jsonify, render_template, url_for ,redirect
#sql
from flask_sqlalchemy import SQLAlchemy
#migration
from flask_migrate import Migrate
import os

from werkzeug.utils import secure_filename
import json





app = Flask(__name__)
app.secret_key = 'asdasdasdasdasdasdasdaveqvq34c'

UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ENV = 'dev'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasdaveqvq34c'
    
   
        

else:
    app.debug = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    
SQLALCHEMY_TRACK_MODIFICATIONS = False


db =SQLAlchemy(app)
migrate = Migrate(app, db)



class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(100))
    user_type = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)    
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    profile_url = db.Column(db.String(100), nullable=True)
    verified_user = db.Column(db.String(100), nullable=True)
    active_user = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.String(100), nullable=True)
    last_login = db.Column(db.String(100), nullable=True)
    fcm_id = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.String(100), nullable=True)
    longitude = db.Column(db.String(100), nullable=True)

    prod_cat = db.relationship('ProductCategory', backref='prod_cat')


class ProductCategory(db.Model):
    __tablename__ = 'productcategory'
    id = db.Column(db.Integer, primary_key=True)
    category_name_en = db.Column(db.String(100), nullable=False)
    category_name_ar = db.Column(db.String(100), nullable=True)
    category_order = db.Column(db.String(100), nullable=True)
    category_image_url = db.Column(db.String(100), nullable=True)
    category_desc_en = db.Column(db.String(100), nullable=True)
    category_desc_ar = db.Column(db.String(100), nullable=True)
    active = db.Column(db.String(100), nullable=True)

    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class ProductSubCategory(db.Model):
    __tablename__ = 'productsubcategory'
    id = db.Column(db.Integer, primary_key=True)
    subcategory_name_en = db.Column(db.String(100), nullable=False)
    subcategory_name_ar = db.Column(db.String(100), nullable=True)
    subcategory_order = db.Column(db.String(100), nullable=True)
    subcategory_image_url = db.Column(db.String(100), nullable=True)
    subcategory_desc_en = db.Column(db.String(100), nullable=True)
    subcategory_desc_ar = db.Column(db.String(100), nullable=True)
    active = db.Column(db.String(100), nullable=True)

    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    fk_prod_cat_id = db.Column(db.Integer, db.ForeignKey('productcategory.id'))







@app.route('/')
def index():
    return render_template('dashboard.html')




## ------------------------------------------------------------------- APIs ------------------------------------------------------------------- ##

@app.route('/insert_users', methods=['POST'])
def insert_users():
    if request.method == 'POST':
        content = request.json
        print(content)
        try: 
            with app.app_context():
                user = Users(ip_address=content['ip_address'], 
                    user_type=content['user_type'],
                    username=content['username'],
                    firstname=content['firstname'],
                    lastname=content['lastname'],
                    password=content['password'],
                    email=content['email'],
                    phone=content['phone'],
                )
                db.session.add(user)
                db.session.commit()
            return jsonify({'return': 'user added successfully'})
        except Exception as e:
            return jsonify({'return': 'error adding user'+str(e)})
    return jsonify({'return': 'no POST request'})

@app.route('/get_users/<parm>', methods=['GET'])
def get_users(parm):

    def get_USER_query(user):
        user_json = {
                    'return': 'success', 
                    'user': user.username,
                    'email': user.email,
                    'phone': user.phone,
                    'password': user.password,
                    'firstname': user.firstname,
                    'lastname': user.lastname,
                    'user_type': user.user_type,
                    'ip_address': user.ip_address,
                    'profile_url': user.profile_url,
                    'verified_user': user.verified_user,
                    'active_user': user.active_user,
                    'created_at': user.created_at,
                    'last_login': user.last_login,
                    'fcm_id': user.fcm_id,
                    'latitude': user.latitude,
                    'longitude': user.longitude,
                    }
        return user_json



    if request.method == 'GET': 
        try:    
            if parm == 'email':
                email = request.args.get('email')
                user = Users.query.filter_by(email=email).first()
                return jsonify(get_USER_query(user))

            elif parm == 'username':
                username = request.args.get('username')
                user = Users.query.filter_by(username=username).first()
                return jsonify(get_USER_query(user))
            
            elif parm == 'phone':
                phone = request.args.get('phone')
                user = Users.query.filter_by(phone=phone).first()
                return jsonify(get_USER_query(user))
            else:
                return jsonify({'return': 'no user found'})
        except Exception as e:
            return jsonify({'return': 'error getting users : '+ str(e)})
    return jsonify({'return': 'no GET request'})

## ------------------------------------------------------------------- APIs ------------------------------------------------------------------- ##

@app.route('/addProductCategory', methods=['POST', 'GET'])
def addProductCategory():
    
    if request.method == 'POST':
        try: 
            with app.app_context():
                img = request.files.get('category_image_url')
                img_filename = secure_filename(request.files['category_image_url'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                prod_cat = ProductCategory(category_name_en=request.form['category_name_en'], 
                    category_name_ar=request.form['category_name_ar'],
                    category_image_url=img_filename,
                    category_desc_en=request.form['category_desc_en'],
                    category_desc_ar=request.form['category_desc_ar']  
                )
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                db.session.add(prod_cat)
                db.session.commit()
            return redirect(url_for('viewProductCategory'))
        except Exception as e:
            return jsonify({'return': 'error adding product category :- '+str(e)})
    return render_template('addProductCategory.html')


@app.route('/viewProductCategory', methods=['GET', 'POST'])
def viewProductCategory():
    if request.method == 'GET':
        try:
            with app.app_context():
                prod_cat = ProductCategory.query.all()
                return render_template('viewProductCategory.html', prod_cat=prod_cat)
        except Exception as e:
            return jsonify({'return': 'error getting product category :- '+str(e)})
    return render_template('viewProductCategory.html')

@app.route('/editProductCategory/<id>', methods=['GET', 'POST'])
def editProductCategory(id):
    prod_cat = ProductCategory.query.get_or_404(id)
    if request.method == 'POST':
        print(prod_cat)
        try:
            # with app.app_context():
            img = request.files.get('category_image_url')
            img_filename = secure_filename(request.files['category_image_url'].filename)
            basedir = os.path.abspath(os.path.dirname(__file__))

            if img_filename == prod_cat.category_image_url:
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                

            prod_cat.category_name_en=request.form['category_name_en']
            prod_cat.category_name_ar=request.form['category_name_ar']
            prod_cat.category_image_url=img_filename
            prod_cat.category_desc_en=request.form['category_desc_en']
            prod_cat.category_desc_ar=request.form['category_desc_ar']  
            
            
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            db.session.commit()
            
            return redirect(url_for('viewProductCategory'))
        except Exception as e:
            return jsonify({'return': 'error getting product category :- '+str(e)})
    return render_template('editProductCategory.html', prod_cat=prod_cat)

@app.route('/deleteProductCategory/<id>', methods=['GET', 'POST'])
def deleteProductCategory(id):
    prod_cat = ProductCategory.query.get_or_404(id)
    try:
        
        db.session.delete(prod_cat)
        db.session.commit()

        return redirect(url_for('viewProductCategory'))
    except Exception as e:
        return jsonify({'return': 'error deleting product category :- '+str(e)})
    