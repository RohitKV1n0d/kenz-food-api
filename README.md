<h1>Kenz-Food-APIs Documentaions</h1>

<h2>User APIs</h2>


<h3>Insert User</h3>
<ul>
    <p>Insert a new user into the database</p>
    <p>URL: /inster_users</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>
    
       
        Example Input body:
        {
            "ip_address" : "0.0.0.0", 
            "user_type" : "admin",
            "username" : "admin",
            "firstname" : "adminf",
            "lastname" : "adminl",
            "password" : "admin123",
            "email" : "admin@admin.com",
            "phone" :  "1234567890"
        }
      
</ul>

        
    

<h3>Get Users</h3>
<ul>
    <p>Get user data from database</p>
    <p>URL: /get_users/{parm}</p>
    <p>Method: GET</p>

<p>Pram list:-</p>

    •	/username
    •	/email
    •	/phone

<p>Example:-</p>
<p>https://kenz-food-api.herokuapp.com/get_users/username?username=admin</p>


    Response Body: JSON Object
    Example:
    {
        "active_user": null,
        "created_at": null,
        "email": "admin@admin.com",
        "fcm_id": null,
        "firstname": "adminf",
        "ip_address": "0.0.0.0",
        "last_login": null,
        "lastname": "adminl",
        "latitude": null,
        "longitude": null,
        "password": "admin123",
        "phone": "1234567890",
        "profile_url": null,
        "return": "success",
        "user": "admin",
        "user_type": "admin",
        "verified_user": null
    }
        


</ul>


<h2>Category APIs</h2>

<h3>Get all Categories</h3>
<ul>
    <p>Get all data from category table</p>
    <p>URL: /get_categories</p>
    <p>Method : GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/get_categories</p>
    
    Response Body: JSON Object
    Example:
    {
        "categories": [
            {
                "active": null,
                "category_desc_ar": "هذا إدخال اختبار فرعي للقطط",
                "category_desc_en": "this is a test entery",
                "category_image_url": "FWA_LOGO.png",
                "category_name_ar": "إدخال الاختبار",
                "category_name_en": "test_xcat1",
                "category_order": null,
                "id": 1
            },
            {
                "active": null,
                "category_desc_ar": "إدخال اإدخال اإدخال اإدخال اإدخال اإدخال اإدخال ا",
                "category_desc_en": "this is about cat 2",
                "category_image_url": "hash-it-02.jpg",
                "category_name_ar": "إدخال اإدخال الاختبار",
                "category_name_en": "cat 2",
                "category_order": null,
                "id": 2
            },
            {
                "active": null,
                "category_desc_ar": "asd",
                "category_desc_en": "asd",
                "category_image_url": "TESLA_BLACK_AAA_shrink_10_transparent_-_kopie.png",
                "category_name_ar": "asd",
                "category_name_en": "test_xcat1",
                "category_order": null,
                "id": 3
            }
        ],
        "return": "success"
    }
        

</ul>

<h3>Get SubCategory by ID</h3>
<ul>
    <p>Get all subcatagories data  in a given category by ID</p>
    <p>URL: /get_subcategory</p>
    <p>Method : GET</p>
    <p>Example : http://192.168.100.83:5000/get_subcategory?category_id=1</p>
    
    Response Body: JSON Object
    Example:
    {
        "return": "success",
        "subcategories": [
            {
                "active": null,
                "id": 1,
                "subcategory_desc_ar": "هذا إدخال اختبار فرعي للقطط",
                "subcategory_desc_en": "this is a test sub cat entrty",
                "subcategory_image_url": "Group_84logo.png",
                "subcategory_name_ar": "دخول الاختبار",
                "subcategory_name_en": "test_Subcat1 edit",
                "subcategory_order": null
            },
            {
                "active": null,
                "id": 2,
                "subcategory_desc_ar": "دخول الاختباردخول الاختباردخول الاختبار",
                "subcategory_desc_en": "Thso os tets",
                "subcategory_image_url": "Group_85.png",
                "subcategory_name_ar": "دخول الاختبار",
                "subcategory_name_en": "test_Subcat2",
                "subcategory_order": null
            },
            {
                "active": null,
                "id": 3,
                "subcategory_desc_ar": "دخول الاختباردخول الاختباردخول الاختباردخول الاختبار",
                "subcategory_desc_en": "this is a test 3 entry",
                "subcategory_image_url": "HASH_IT_LOGO.png",
                "subcategory_name_ar": "دخول الاختبار",
                "subcategory_name_en": "test_Subcat3",
                "subcategory_order": null
            }
        ]
    }

</ul>

<h2>Product APIs</h2>

<h3>Get Product images by ID</h3>
<ul>
    <p>Get All images of a product query by Product ID</p>
    <p>URL: /get_product_images</p>
    <p>Method : GET</p>
    <p>Example : http://kenz-food-api.herokuapp.com/get_products_images?product_id=3</p>

    Response Body: JSON Object
    Example:
    {
        "product_images": [<image_URL1>, <image_URL2>, <image_URL3>],
        "return": "success"
    }
</ul>

<h3>Get Product Stock data by ID</h3>
<ul>
    <p>Get all product stocks query by product ID</p>
    <p>URL: /get_product_stocks</p>
    <p>Method : GET</p>
    <p>Example : http://kenz-food-api.herokuapp.com/get_product_stocks?product_id=1</p>

    Response Body: JSON Object
    Example:
    {
        "product_stocks": [<stock_URL_10>, <stock_URL_20>, <stock_URL_30>],
        "return": "success"
    }
</ul>

<h3>Get Products</h3>
<ul>
    <p>Get all Products based on parm input</p>
    <p>URL: /get_products</p>
    <p>Method : GET</p>
    <p>Parameters : parm, id</p>
    <ol>
        <li>parm = {product_id, category_id, subcategory_id, all}</li>
        <li>id = {id}</li>
        <p><b>*(parm=all) requires no id</b></p>
    </ol>
    <p>Example : http://kenz-food-api.herokuapp.com/get_product?parm=category_id&id=1</p>

    Response Body: JSON Object
    Example:
    {
    "products": [
        {
            "cat_id": 2,
            "fast_delivery": null,
            "featured": null,
            "fresh": null,
            "id": 10,
            "offer": null,
            "other_title_ar": null,
            "other_title_en": null,
            "product_barcode": null,
            "product_cat_id": 2,
            "product_code": null,
            "product_desc_ar": "asdasdasd",
            "product_desc_en": "asdasd",
            "product_images": [
                {
                    "id": 42,
                    "product_id": 10,
                    "product_image_url": "https://i.imgur.com/rFpmw8C.jpg"
                }
            ],
            "product_name_ar": "asd",
            "product_name_en": "Test image url 1",
            "product_stock": [
                {
                    "id": 24,
                    "main_rack_no": null,
                    "max_stock": "",
                    "min_stock": "",
                    "opening_stock": "",
                    "product_id": 10,
                    "product_offer_price": "asd",
                    "product_price": "dasd",
                    "product_purchase_price": "asd",
                    "sub_rack_no": null
                }
            ],
            "product_subcat_id": 2,
            "status": null,
            "subcat_id": 2,
            "unit_quantity": "dasdasd"
        }
    ],
    "return": "success" }


</ul>

<h3>Add Products</h3>
<ul>
    <p>Add Products to a subcatagory</p>
    <p>URL: \addProduct</p>
    <p>Method : POST</p>
    <p>Parameters : product_name_en, product_name_ar, product_desc_en, product_desc_ar, product_image_url, subcategory_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/addProduct</p>

    Request Body: JSON Object
    Example:
    {
        "product_name_en": "test_Subcat1 edit",
        "product_name_ar": "دخول الاختبار",
        "product_desc_en": "this is a test sub cat entrty",
        "product_desc_ar": "هذا إدخال اختبار فرعي للقطط",
        "product_image_url": "Group_84logo.png",
        "subcategory_id": 1
        ,.......{more left for disccusion}
    }

</ul>



    
    
    
    
