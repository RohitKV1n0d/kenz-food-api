#flask boilerpalte
from flask import Flask, request, jsonify, render_template, url_for ,redirect, session
#sql
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#migration
from flask_migrate import Migrate
import os


from werkzeug.utils import secure_filename
import requests, json
import pyimgur





app = Flask(__name__)
app.secret_key = 'asdasdasdasdasdasdasaasdasdasdasd12312312daveqvq34c'

UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


CLIENT_ID = "2d3158d36137249"
im = pyimgur.Imgur(CLIENT_ID)


ENV = 'prod'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasdaveqvq34c'
    # PATH = "C:/Users/USER/Desktop/Hash IT/kenz-food-api/kenz-food-api/kenz-api/static/img/uploads/"

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


@app.route('/', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    productCategory = ProductCategory.query.all()

    return render_template('dashboard.html', user=current_user, productCategory=productCategory)




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


@app.route('/get_categories', methods=['GET'])
def get_categories():
    if request.method == 'GET':
        try:
            categories = ProductCategory.query.all()
            categories_json = []
            for category in categories:
                category_json = {
                    'id': category.id,
                    'category_name_en': category.category_name_en,
                    'category_name_ar': category.category_name_ar,
                    'category_desc_en': category.category_desc_en,
                    'category_desc_ar': category.category_desc_ar,
                    'category_image_url': category.category_image_url,
                    'category_order': category.category_order,
                    'active': category.active,
                }
                categories_json.append(category_json)
            return jsonify({'return': 'success', 'categories': categories_json})
        except Exception as e:
            return jsonify({'return': 'error getting categories : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_subcategory', methods=['GET'])
def get_subcategory():
    if request.method == 'GET':
        try:
            get_subcategory = ProductSubCategory.query.filter_by(fk_prod_cat_id=request.args.get('category_id')).all()
            subcategories_json = []
            for subcategory in get_subcategory:
                subcategory_json = {
                    'id': subcategory.id,
                    'subcategory_name_en': subcategory.subcategory_name_en,
                    'subcategory_name_ar': subcategory.subcategory_name_ar,
                    'subcategory_desc_en': subcategory.subcategory_desc_en,
                    'subcategory_desc_ar': subcategory.subcategory_desc_ar,
                    'subcategory_image_url': subcategory.subcategory_image_url,
                    'subcategory_order': subcategory.subcategory_order,
                    'active': subcategory.active,
                }
                subcategories_json.append(subcategory_json)
            return jsonify({'return': 'success', 'subcategories': subcategories_json})
        except Exception as e:
            return jsonify({'return': 'error getting subcategories : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_products_images', methods=['GET'])
def get_products_images():
    if request.method == 'GET':
        try:
            get_products_images = ProductImages.query.filter_by(fk_product_id=request.args.get('product_id')).all()
            if get_products_images:
                products_images_json = []
                for product_image in get_products_images:
                    product_image_json = {
                        'id': product_image.id,
                        'image_url': product_image.product_image_url,
                    }
                    products_images_json.append(product_image_json)
                return jsonify({'return': 'success', 'product_images': products_images_json})
            else:
                return jsonify({'return': 'no product images found'})
        except Exception as e:
            return jsonify({'return': 'error getting product images : '+ str(e)})
    return jsonify({'return': 'no GET request'})

@app.route('/get_product_stocks', methods=['GET'])
def get_product_stocks():
    if request.method == 'GET':
        try:
            get_product_stocks = ProductStock.query.filter_by(fk_product_id=request.args.get('product_id')).all()
            if get_product_stocks:
                product_stocks_json = []
                for product_stock in get_product_stocks:
                    product_stock_json = {
                        'id': product_stock.id,
                        'product_price': product_stock.product_price,
                        'product_offer_price': product_stock.product_offer_price,
                        'product_purchase_price': product_stock.product_purchase_price,
                        'opening_stock': product_stock.opening_stock,
                        'min_stock': product_stock.min_stock,
                        'max_stock': product_stock.max_stock,
                        'main_rack_no': product_stock.main_rack_no,
                        'sub_rack_no': product_stock.sub_rack_no
                    }
                    product_stocks_json.append(product_stock_json)
                return jsonify({'return': 'success', 'product_stocks': product_stocks_json})
            else:
                return jsonify({'return': 'no product stocks found'})
        except Exception as e:
            return jsonify({'return': 'error getting product stocks : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_product', methods=['GET'])
def get_product():
    if request.method == 'GET':
        if request.args.get('parm') ==  'product_id':
            try:
                get_product = Products.query.filter_by(id=request.args.get('id')).first()
                # get_product_stocks = ProductStock.query.filter_by(fk_product_id=request.args.get('id')).all()
                if get_product:
                    product_json = {
                        # 'id': get_product.id,
                        'product_name_en': get_product.product_name_en,
                        'product_name_ar': get_product.product_name_ar,
                        'product_desc_en': get_product.product_desc_en,
                        'product_desc_ar': get_product.product_desc_ar,

                    }
                    return jsonify({'return': 'success', 'product': product_json})
                else:
                    return jsonify({'return': 'no product found'})
            except Exception as e:
                return jsonify({'return': 'error getting product : '+ str(e)})
        elif request.args.get('parm') ==  'category_id':
            try:
                get_products = Products.query.filter_by(cat=int(request.args.get('id'))).all()
                if get_products:
                    products_json = []
                    products_stocks_json = []
                    products_images_json = []
                    for product in get_products: 
                        product_json = {
                            'id': product.id,
                            'product_name_en': product.product_name_en,
                            'product_name_ar': product.product_name_ar,
                            'product_desc_en': product.product_desc_en,
                            'product_desc_ar': product.product_desc_ar,
                            'unit_quantity': product.unit_quantity,
                            'product_code': product.product_code,
                            'product_barcode': product.produc_barcode,
                            'other_title_en': product.other_title_en,
                            'other_title_ar': product.other_title_ar, 
                            'status': product.status,
                            'fast_delivery': product.fast_delivery,
                            'featured': product.featured,
                            'fresh': product.fresh,
                            'offer': product.offer,
                            'product_cat_id': product.cat,
                            'product_subcat_id': product.subcat,
                            'cat_id': product.cat,
                            'subcat_id': product.subcat,
                            'product_stock': [],
                            'product_images': []
                            # 'product_price': product.product_stock,
                        }
                        for product_stock in product.product_stock:
                            product_stock_json = {
                                'id': product_stock.id,
                                'product_price': product_stock.product_price,
                                'product_offer_price': product_stock.product_offer_price,
                                'product_purchase_price': product_stock.product_purchase_price,
                                'opening_stock': product_stock.opening_stock,
                                'min_stock': product_stock.min_stock,
                                'max_stock': product_stock.max_stock,
                                'main_rack_no': product_stock.main_rack_no,
                                'sub_rack_no': product_stock.sub_rack_no,
                                'product_id': product_stock.fk_product_id,
                            }
                            products_stocks_json.append(product_stock_json)
                            product_json['product_stock'] = products_stocks_json
                        for product_image in product.product_image:
                            product_image_json = {
                                'id': product_image.id,
                                'product_image_url': product_image.product_image_url,
                                'product_id': product_image.fk_product_id,
                            }
                            products_images_json.append(product_image_json)
                            product_json['product_images'] = products_images_json

                        products_images_json = []
                        products_stocks_json = []
                        products_json.append(product_json)
                    return jsonify({'return': 'success', 'products': products_json})
                else:
                    return jsonify({'return': 'no products'})
            except Exception as e:
                return jsonify({'return': 'error getting products : '+ str(e)})
        elif request.args.get('parm') ==  'subcategory_id':
            try:
                get_products = Products.query.filter_by(subcat=request.args.get('id')).all()
                if get_products:
                    products_json = []
                    products_stocks_json = []
                    products_images_json = []
                    for product in get_products: 
                        product_json = {
                            'id': product.id,
                            'product_name_en': product.product_name_en,
                            'product_name_ar': product.product_name_ar,
                            'product_desc_en': product.product_desc_en,
                            'product_desc_ar': product.product_desc_ar,
                            'unit_quantity': product.unit_quantity,
                            'product_code': product.product_code,
                            'product_barcode': product.produc_barcode,
                            'other_title_en': product.other_title_en,
                            'other_title_ar': product.other_title_ar, 
                            'status': product.status,
                            'fast_delivery': product.fast_delivery,
                            'featured': product.featured,
                            'fresh': product.fresh,
                            'offer': product.offer,
                            'product_cat_id': product.cat,
                            'product_subcat_id': product.subcat,
                            'cat_id': product.cat,
                            'subcat_id': product.subcat,
                            'product_stock': [],
                            'product_images': []
                            # 'product_price': product.product_stock,
                        }
                        for product_stock in product.product_stock:
                            product_stock_json = {
                                'id': product_stock.id,
                                'product_price': product_stock.product_price,
                                'product_offer_price': product_stock.product_offer_price,
                                'product_purchase_price': product_stock.product_purchase_price,
                                'opening_stock': product_stock.opening_stock,
                                'min_stock': product_stock.min_stock,
                                'max_stock': product_stock.max_stock,
                                'main_rack_no': product_stock.main_rack_no,
                                'sub_rack_no': product_stock.sub_rack_no,
                                'product_id': product_stock.fk_product_id,
                            }
                            products_stocks_json.append(product_stock_json)
                            product_json['product_stock'] = products_stocks_json
                        for product_image in product.product_image:
                            product_image_json = {
                                'id': product_image.id,
                                'product_image_url': product_image.product_image_url,
                                'product_id': product_image.fk_product_id,
                            }
                            products_images_json.append(product_image_json)
                            product_json['product_images'] = products_images_json

                        products_images_json = []
                        products_stocks_json = []
                        products_json.append(product_json)
                    return jsonify({'return': 'success', 'products': products_json})
                else:
                    return jsonify({'return': 'no products'})
            except Exception as e:
                return jsonify({'return': 'error getting products : '+ str(e)})
        elif request.args.get('parm') ==  'all':
            try:
                get_products = Products.query.all()
                if get_products:
                    products_json = []
                    products_stocks_json = []
                    products_images_json = []
                    for product in get_products: 
                        product_json = {
                            'id': product.id,
                            'product_name_en': product.product_name_en,
                            'product_name_ar': product.product_name_ar,
                            'product_desc_en': product.product_desc_en,
                            'product_desc_ar': product.product_desc_ar,
                            'unit_quantity': product.unit_quantity,
                            'product_code': product.product_code,
                            'product_barcode': product.produc_barcode,
                            'other_title_en': product.other_title_en,
                            'other_title_ar': product.other_title_ar, 
                            'status': product.status,
                            'fast_delivery': product.fast_delivery,
                            'featured': product.featured,
                            'fresh': product.fresh,
                            'offer': product.offer,
                            'product_cat_id': product.cat,
                            'product_subcat_id': product.subcat,
                            'cat_id': product.cat,
                            'subcat_id': product.subcat,
                            'product_stock': [],
                            'product_images': []
                            # 'product_price': product.product_stock,
                        }
                        for product_stock in product.product_stock:
                            product_stock_json = {
                                'id': product_stock.id,
                                'product_price': product_stock.product_price,
                                'product_offer_price': product_stock.product_offer_price,
                                'product_purchase_price': product_stock.product_purchase_price,
                                'opening_stock': product_stock.opening_stock,
                                'min_stock': product_stock.min_stock,
                                'max_stock': product_stock.max_stock,
                                'main_rack_no': product_stock.main_rack_no,
                                'sub_rack_no': product_stock.sub_rack_no,
                                'product_id': product_stock.fk_product_id,
                            }
                            products_stocks_json.append(product_stock_json)
                            product_json['product_stock'] = products_stocks_json
                        for product_image in product.product_image:
                            product_image_json = {
                                'id': product_image.id,
                                'product_image_url': product_image.product_image_url,
                                'product_id': product_image.fk_product_id,
                            }
                            products_images_json.append(product_image_json)
                            product_json['product_images'] = products_images_json

                        products_images_json = []
                        products_stocks_json = []
                        products_json.append(product_json)
                    return jsonify({'return': 'success', 'products': products_json})
                else:
                    return jsonify({'return': 'no products'})
            except Exception as e:
                return jsonify({'return': 'error getting products : '+ str(e)})




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
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                prod_cat = ProductCategory(category_name_en=request.form['category_name_en'], 
                    category_name_ar=request.form['category_name_ar'],
                    category_image_url=upload_image.link,
                    category_desc_en=request.form['category_desc_en'],
                    category_desc_ar=request.form['category_desc_ar']  
                )
                db.session.add(prod_cat)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
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

            # if img_filename == prod_cat.category_image_url:
            #     os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                

             
            
            
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
            prod_cat.category_name_en=request.form['category_name_en']
            prod_cat.category_name_ar=request.form['category_name_ar']
            prod_cat.category_image_url=upload_image.link
            prod_cat.category_desc_en=request.form['category_desc_en']
            prod_cat.category_desc_ar=request.form['category_desc_ar'] 
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
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
                
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)

                prod_subcat = ProductSubCategory(fk_prod_cat_id=id,
                    subcategory_name_en=request.form['subcategory_name_en'], 
                    subcategory_name_ar=request.form['subcategory_name_ar'],
                    subcategory_image_url=upload_image.link,
                    subcategory_desc_en=request.form['subcategory_desc_en'],
                    subcategory_desc_ar=request.form['subcategory_desc_ar']  
                )
                db.session.add(prod_subcat)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

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

            # if img_filename == prod_subcat.subcategory_image_url:
            #     os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                

            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)

            prod_subcat.subcategory_name_en=request.form['subcategory_name_en']
            prod_subcat.subcategory_name_ar=request.form['subcategory_name_ar']
            prod_subcat.subcategory_image_url=upload_image.link
            prod_subcat.subcategory_desc_en=request.form['subcategory_desc_en']
            prod_subcat.subcategory_desc_ar=request.form['subcategory_desc_ar']  
            
            
            
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
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

@app.route('/addProductWithSubcat/<subcat_id>', methods=['POST', 'GET'])
@login_required
def addProductWithSubcat(subcat_id):
    category = ProductCategory.query.all()
    subcategory = ProductSubCategory.query.all()

    addSubcat = ProductSubCategory.query.get_or_404(subcat_id)
    addCat = ProductCategory.query.get_or_404(addSubcat.fk_prod_cat_id)

          
        

    if request.method == 'POST':
        try: 
            with app.app_context():
        
                prod = Products(
                    product_name_en=request.form['product_name_en'], 
                    product_name_ar=request.form['product_name_ar'],
                    product_desc_en=request.form['product_desc_en'],
                    product_desc_ar=request.form['product_desc_ar'],
                    unit_id=request.form['unit'],
                    unit_quantity=request.form['unit_quantity'],
                    cat=addCat.id,
                    subcat=addSubcat.id
                )
                db.session.add(prod)
                db.session.commit()
                prod_img = request.files.getlist('product_image_url')
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=upload_image.link
                    )
                    db.session.add(prod_img)
                    db.session.commit()
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

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


            return redirect(url_for('viewSubcatOnlyProducts', id=addSubcat.id))
        except Exception as e:
            return jsonify({'return': 'error adding product :- '+str(e)})
    return render_template('addProductWithSubcat.html', 
                            category=category, 
                            subcategory=subcategory,
                            subcat_id=subcat_id, 
                            addCat=addCat,
                            addSubcat=addSubcat)

@app.route('/addProduct', methods=['POST', 'GET'])
@login_required
def addProduct():
    category = ProductCategory.query.all()
    subcategory = ProductSubCategory.query.all()

    # addSubcat = ProductSubCategory.query.get_or_404(subcat_id)
    # addCat = ProductCategory.query.get_or_404(addSubcat.fk_prod_cat_id)

    subcat= [[],[]]
    opt= {}
    with app.app_context():
        category = ProductCategory.query.all()
        for cat in category:
            for sub in cat.sub_cat:
                subcat[0].append(sub.subcategory_name_en)
                subcat[1].append(sub.id)
                opt[cat.id] = subcat
            subcat= [[],[]]
         
          
        

    if request.method == 'POST':
        try: 
            with app.app_context():
        
                prod = Products(
                    product_name_en=request.form['product_name_en'], 
                    product_name_ar=request.form['product_name_ar'],
                    product_desc_en=request.form['product_desc_en'],
                    product_desc_ar=request.form['product_desc_ar'],
                    unit_id=request.form['unit'],
                    unit_quantity=request.form['unit_quantity'],
                    cat=request.form['category'],
                    subcat=request.form['subcategory']
                )
                db.session.add(prod)
                db.session.commit()
                prod_img = request.files.getlist('product_image_url')
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=upload_image.link
                    )
                    db.session.add(prod_img)
                    db.session.commit()
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

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
    return render_template('addProduct.html', 
                            category=category, 
                            subcategory=subcategory,
                            otp=opt)
                            # subcat_id=subcat_id, 
                            # addCat=addCat,
                            # addSubcat=addSubcat)




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
                    
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)

                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=upload_image.link
                    )
                    db.session.add(prod_img)
                    db.session.commit()
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

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


@app.route('/viewSubcatOnlyProducts/<id>', methods=['GET', 'POST'])
@login_required
def viewSubcatOnlyProducts(id):
    prod = Products.query.filter_by(subcat=id).all()
    sub_cat = ProductSubCategory.query.get_or_404(id)
    prod_img = ProductImages.query.all()
    prod_stock = ProductStock.query.all()
    return render_template('viewSubcatOnlyProducts.html', prod=prod, prod_img=prod_img,zip=zip, prod_stock=prod_stock, sub_cat=sub_cat)