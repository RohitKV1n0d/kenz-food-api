#flask boilerpalte
from flask import Flask, request, jsonify, render_template, url_for ,redirect, session
#sql
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#migration
from flask_migrate import Migrate
import os


from werkzeug.utils import secure_filename
import json





app = Flask(__name__)
app.secret_key = 'asdasdasdasdasdasdasdaveqvq34c'

UPLOAD_FOLDER = '/static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ENV = 'prod'

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



class Users(db.Model, UserMixin):
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

    # prod_cat = db.relationship('ProductCategory', backref='prod_cat')


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

    cat_product = db.relationship('Products', backref='product')
    sub_cat = db.relationship('ProductSubCategory', backref='sub_cat')
    # fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


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

    # fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sub_product = db.relationship('Products', backref='products')
    fk_prod_cat_id = db.Column(db.Integer, db.ForeignKey('productcategory.id'))


class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name_en = db.Column(db.String(100), nullable=False)
    product_name_ar = db.Column(db.String(100), nullable=True)
    product_desc_en = db.Column(db.String(100), nullable=True)
    product_desc_ar = db.Column(db.String(100), nullable=True)
    unit_id = db.Column(db.String(100), nullable=True)
    unit_quantity = db.Column(db.String(100), nullable=True)
    product_code = db.Column(db.String(100), nullable=True)
    produc_barcode = db.Column(db.String(100), nullable=True)
    other_title_en = db.Column(db.String(100), nullable=True)
    other_title_ar = db.Column(db.String(100), nullable=True)
    other_desc_en = db.Column(db.String(100), nullable=True)
    other_desc_ar = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(100), nullable=True)
    fast_delivery = db.Column(db.String(100), nullable=True)
    featured = db.Column(db.String(100), nullable=True)
    fresh = db.Column(db.String(100), nullable=True)
    offer = db.Column(db.String(100), nullable=True)

    cat = db.Column(db.Integer, db.ForeignKey('productcategory.id'))
    subcat = db.Column(db.Integer, db.ForeignKey('productsubcategory.id'))

    product_image = db.relationship('ProductImages', backref='product_image')
    product_stock = db.relationship('ProductStock', backref='product_stock')


class ProductImages(db.Model):
    __tablename__ = 'productimages'
    id = db.Column(db.Integer, primary_key=True)
    product_image_url = db.Column(db.String(100), nullable=True)
    product_image_desc_en = db.Column(db.String(100), nullable=True)
    product_image_desc_ar = db.Column(db.String(100), nullable=True)

    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class ProductStock(db.Model):
    __tablename__ = 'productstock'
    id = db.Column(db.Integer, primary_key=True)
    product_price = db.Column(db.String(100), nullable=True)
    product_offer_price = db.Column(db.String(100), nullable=True)
    product_purchase_price = db.Column(db.String(100), nullable=True)
    opening_stock = db.Column(db.String(100), nullable=True)
    min_stock = db.Column(db.String(100), nullable=True)
    max_stock = db.Column(db.String(100), nullable=True)
    main_rack_no = db.Column(db.String(100), nullable=True)
    sub_rack_no = db.Column(db.String(100), nullable=True)


    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))




login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard(methods=['GET', 'POST']):
    return render_template('dashboard.html', user=current_user)




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




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('dashboard'))
        return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


                                            #-----Porduct category-----#

@app.route('/addProductCategory', methods=['POST', 'GET'])
@login_required
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
@login_required
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
@login_required
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
@login_required
def deleteProductCategory(id):
    prod_cat = ProductCategory.query.get_or_404(id)
    try:
        
        db.session.delete(prod_cat)
        db.session.commit()

        return redirect(url_for('viewProductCategory'))
    except Exception as e:
        return jsonify({'return': 'error deleting product category :- '+str(e)})
    
                                             #-----Porduct category-----#



                                            #-----Porduct sub category-----#

@app.route('/addProductSubCategory/<id>', methods=['POST', 'GET'])
@login_required
def addProductSubCategory(id):   
    if request.method == 'POST':
        try: 
            with app.app_context():
                img = request.files.get('subcategory_image_url')
                img_filename = secure_filename(request.files['subcategory_image_url'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                prod_subcat = ProductSubCategory(fk_prod_cat_id=id,
                    subcategory_name_en=request.form['subcategory_name_en'], 
                    subcategory_name_ar=request.form['subcategory_name_ar'],
                    subcategory_image_url=img_filename,
                    subcategory_desc_en=request.form['subcategory_desc_en'],
                    subcategory_desc_ar=request.form['subcategory_desc_ar']  
                )
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                db.session.add(prod_subcat)
                db.session.commit()
            return redirect(url_for('viewProductSubCategory',id=id,name=request.form['subcategory_name_en']))
        except Exception as e:
            return jsonify({'return': 'error adding product sub category :- '+str(e)})
    return render_template('addProductSubCategory.html')
    

@app.route('/viewProductSubCategory/<id>/<name>', methods=['GET', 'POST'])
@login_required
def viewProductSubCategory(id,name):
    prod_subcat = ProductSubCategory.query.filter_by(fk_prod_cat_id=id).all()
    return render_template('viewProductSubCategory.html', prod_subcat=prod_subcat, name=name, id=id)
       
@app.route('/editProductSubCategory/<id>/<name>', methods=['GET', 'POST'])
@login_required
def editProductSubCategory(id,name):
    prod_subcat = ProductSubCategory.query.get_or_404(id)
    if request.method == 'POST':
        print(prod_subcat)
        try:
            # with app.app_context():
            img = request.files.get('subcategory_image_url')
            img_filename = secure_filename(request.files['subcategory_image_url'].filename)
            basedir = os.path.abspath(os.path.dirname(__file__))

            if img_filename == prod_subcat.subcategory_image_url:
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                

            prod_subcat.subcategory_name_en=request.form['subcategory_name_en']
            prod_subcat.subcategory_name_ar=request.form['subcategory_name_ar']
            prod_subcat.subcategory_image_url=img_filename
            prod_subcat.subcategory_desc_en=request.form['subcategory_desc_en']
            prod_subcat.subcategory_desc_ar=request.form['subcategory_desc_ar']  
            
            
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            db.session.commit()
            
            return redirect(url_for('viewProductSubCategory', id=prod_subcat.fk_prod_cat_id, name=name))
        except Exception as e:
            return jsonify({'return': 'error getting product sub category :- '+str(e)})
    return render_template('editProductSubCategory.html', prod_subcat=prod_subcat , name=name)

@app.route('/deleteProductSubCategory/<id>', methods=['GET', 'POST'])
@login_required
def deleteProductSubCategory(id):
    prod_subcat = ProductSubCategory.query.get_or_404(id)
    try:
        
        db.session.delete(prod_subcat)
        db.session.commit()

        return redirect(url_for('viewProductSubCategory',id=prod_subcat.fk_prod_cat_id,name=prod_subcat.subcategory_name_en))
    except Exception as e:
        return jsonify({'return': 'error deleting product sub category :- '+str(e)})

                                            #-----Porduct sub category-----#

@app.route('/addProduct', methods=['POST', 'GET'])
@login_required
def addProduct():
    category = ProductCategory.query.all()
    subcategory = ProductSubCategory.query.all()
    if request.method == 'POST':
        try: 
            with app.app_context():
        
                prod = Products(
                    product_name_en=request.form['product_name_en'], 
                    product_name_ar=request.form['product_name_ar'],
                    product_desc_en=request.form['product_desc_en'],
                    product_desc_ar=request.form['product_desc_ar'],
                    unit_id=request.form['unit'],
                    unit_quantity=request.form['unit_quantity']
                )
                db.session.add(prod)
                db.session.commit()
                prod_img = request.files.getlist('product_image_url')
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=img_filename
                    )
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    db.session.add(prod_img)
                    db.session.commit()

                prod_stock = ProductStock(fk_product_id=prod.id,
                        product_price=request.form['product_price'],
                        product_offer_price=request.form['product_offer_price'],
                        product_purchase_price=request.form['product_purchase_price'],
                        opening_stock=request.form['opening_stock'],
                        min_stock=request.form['min_stock'],
                        max_stock=request.form['max_stock']
                )
                db.session.add(prod_stock)
                db.session.commit()


            return redirect(url_for('viewProduct'))
        except Exception as e:
            return jsonify({'return': 'error adding product :- '+str(e)})
    return render_template('addProduct.html', category=category, subcategory=subcategory)




@app.route('/viewProduct', methods=['GET', 'POST'])
@login_required
def viewProduct():
    prod = Products.query.all()
    prod_img = ProductImages.query.all()
    prod_stock = ProductStock.query.all()
    return render_template('viewProduct.html', prod=prod, prod_img=prod_img,zip=zip, prod_stock=prod_stock)


@app.route('/editProduct/<id>/<name>', methods=['GET', 'POST'])
@login_required
def editProduct(id,name):
    prod = Products.query.get_or_404(id)
    prod_img = ProductImages.query.filter_by(fk_product_id=id).all()
    prod_stock = ProductStock.query.filter_by(fk_product_id=id).all()
    if request.method == 'POST':
        try:
            with app.app_context():
                prod.product_name_en=request.form['product_name_en']
                prod.product_name_ar=request.form['product_name_ar']
                prod.product_desc_en=request.form['product_desc_en']
                prod.product_desc_er=request.form['product_desc_ar']
                prod.unit_id=request.form['unit']
                prod.unit_quantity=request.form['unit_quantity']
                db.session.commit()
                prod_img = request.files.getlist('product_image_url')
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=img_filename
                    )
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    db.session.add(prod_img)
                    db.session.commit()

                prod_stock = ProductStock(fk_product_id=prod.id,
                        product_price=request.form['product_price'],
                        product_offer_price=request.form['product_offer_price'],
                        product_purchase_price=request.form['product_purchase_price'],
                        opening_stock=request.form['opening_stock'],
                        min_stock=request.form['min_stock'],
                        max_stock=request.form['max_stock']
                )
                db.session.add(prod_stock)
                db.session.commit()
            return redirect(url_for('viewProduct'))
        except Exception as e:
            return jsonify({'return': 'error getting product :- '+str(e)})
    return render_template('editProduct.html', prod=prod, prod_img=prod_img, prod_stock=prod_stock , name=name)



@app.route('/deleteProduct/<id>', methods=['GET', 'POST'])
@login_required
def deleteProduct(id):
    prod = Products.query.get_or_404(id)
    try:
        db.session.delete(prod)
        db.session.commit()
        return redirect(url_for('viewProduct'))
    except Exception as e:
        return jsonify({'return': 'error deleting product :- '+str(e)})