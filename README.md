<h1>Kenz-Food-APIs Documentaions</h1>

<h2>User Authentication</h2>

<h3>Sign In User</h3>
<ul>
    <p>Sign in a user by passing email and password</p>
    <p>URL: /sign_in</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>
    
       
        Example Input body:
        {
            "email" : "admin@test.com",
            "password" : "test123"
        }

        Example Response body:
        {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI4Yzk2MmI0Mi04ZTI0LTRhYjMtOTI4Ny02M2Y0OTA2NjI4OTkiLCJleHAiOjE2NzEzMDkzNjl9.u3u2eBxvdloQttUOEi1SePQF9HjIU1rz7MSXnnjj3EY"
        }
</ul>

<h3>Token Headers format</h3>   
<p>Headers : </p>
    
    var headers = {
        'x-access-token': '[token]'
        };


<h2>User APIs</h2>


<h3>Insert User</h3>
<ul>
    <p>Insert a new user into the database</p>
    <p>URL: /insert_users</p>
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

<h3>Add User Address</h3>
<ul>
    <p>Add a new address for a user</p>
    <p>URL: /user_addr</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr</p>
    
       
        Example Input body:
        {
            'address_line1': "address_line1",
            'address_line2': "address_line2",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile': "1234567890",
            'latitude': '10.995003718149182', 
            'longitude': '76.99166976233744'
        }
</ul>

<h3>Get All User Address</h3>
<ul>
    <p>Get all address for a user</p>
    <p>URL: /user_addr</p>
    <p>Method: GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr</p>
    
       
        Example Response body:
        {
            'id': 1,
            'address_line1': "address_line123",
            'address_line2': "address_line123",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile':   "1234567890",
            'latitude':  '10.995003718149182',
            'longitude': '76.99166976233744',
            'created_at':  '2021-08-03T09:00:00.000Z',
            'modified_at': '2021-08-03T09:00:00.000Z',
            'user_id': 1
        }
</ul>

<h3>Get User Address with id</h3>
<ul>
    <p>Get a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr/1</p>
    
       
        Example Response body:
        {
            'id': 1,
            'address_line1': "address_line123",
            'address_line2': "address_line123",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile':   "1234567890",
            'latitude':  '10.995003718149182',
            'longitude': '76.99166976233744',
            'created_at':  '2021-08-03T09:00:00.000Z',
            'modified_at': '2021-08-03T09:00:00.000Z',
            'user_id': 1
        }
</ul>

<h3>Update User Address</h3>
<ul>
    <p>Update a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr/1</p>
    
       
        Example Input body:
        {
            'address_line1': "address_line112",
            'address_line2': "address_line2223",
            'city': "cityxyz12",
            'postal_code': "123456213",
            'country': "countryxyz13",
            'telephone': "1234522890",
            'mobile': "1234567220",
            'latitude': '10.99500312312718149182', 
            'longitude': '76.99166976212333744'
        }

</ul>

<h3>Delete User Address</h3>
<ul>
    <p>Delete a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: DELETE</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr/1</p>
    
       
        Example Response body:
        {
            'message': 'Address deleted successfully',
            'return': 'success'
        }
</ul>


<h2>Banner API</h2>

<h3>Get all Banners</h3>
<ul>
    <p>Get all data from banner table</p>
    <p>URL: /banner</p>
    <p>Method : GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/banner</p>
    
    Response Body: JSON Object
    Example:
    {
        "data": [
            {
                "banner_desc_en": "qweqwe",
                "banner_image_url": "https://i.imgur.com/vy00tog.jpg",
                "banner_name_en": "Test ",
                "id": 1,
                "status": null
            }
        ],
        "message": "banner fetched",
        "return": "success"
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

<h3>Product Status</h3>
<ul>
    <p>Change and Check Product Status</p>
    <p>URL: /changeProductStatus/{status}</p>
    <p>Method : GET</p>
    <p>Parameters : product_id, status</p>
    <p>{status} = enable,diable,check</p>
    <p>Example : http://kenz-food-api.herokuapp.com/enable?id=8</p>

    Request Body: JSON Object
    Example:
    {
        "message": "product status changed",
        "return": "success"
    }

    Example : http://kenz-food-api.herokuapp.com/check?id=8

    {
        "return": "success",
        "status": "enable"
    }

</ul>

<h2>Cart APIs</h2>

<h3>Add Product to cart</h3>
<ul>
    <p>Add Product to cart with product id</p>
    <p>URL: /cart/{product_id}</p>
    <p>Method : POST</p>
    <p>Parameters : product_id, quantity, user_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/1</p>

    Request Body: JSON Object
    Example :
    {
        "quantity": "1"
    }

    Response Body: JSON Object
    Example (If product is already in cart):
    {
        "message": "product quantity updated",
        "return": "success"
    }

    Response Body: JSON Object
    Example:
    {
        "message": "product added to cart",
        "return": "success"
    }
</ul>

<h3>Get all items in Cart</h3>
<ul>
    <p>Get all items in cart</p>
    <p>URL: /cart</p>
    <p>Method : GET</p>
    <p>Parameters : user_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart</p>

    Response Body: JSON Object
    Example Output:
    {
        "cart items": [
            {
                "cat_id": 1,
                "created_at": "Sun, 18 Dec 2022 02:18:43 GMT",
                "fast_delivery": null,
                "featured": null,
                "fresh": null,
                "id": 2,
                "modified_at": "Sun, 18 Dec 2022 02:18:43 GMT",
                "offer": null,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 1,
                "product_code": null,
                "product_desc_ar": "veg briyani - 2veg briyaasdani - 2veg briyani - 2vesdbriyani - asda2veg briyani - 2",
                "product_desc_en": "veg briyandasdai - 2veg briyani - 2veg briyani - 2vegasda briyani - 2",
                "product_id": 2,
                "product_images": [
                    {
                        "id": 4,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/ECJ7Uws.jpg"
                    },
                    {
                        "id": 5,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/erT6QGZ.jpg"
                    },
                    {
                        "id": 6,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/SKdJx59.jpg"
                    }
                ],
                "product_name_ar": "veg briyani - 2",
                "product_name_en": "veg briyani - 2",
                "product_stock": {
                    "id": 2,
                    "main_rack_no": null,
                    "max_stock": "5435",
                    "min_stock": "5",
                    "opening_stock": "45",
                    "product_id": 2,
                    "product_offer_price": "345",
                    "product_price": "5345",
                    "product_purchase_price": "3453",
                    "sub_rack_no": null
                },
                "product_subcat_id": 1,
                "quantity": "5",
                "status": "enable",
                "subcat_id": 1,
                "unit_quantity": "1234",
                "user_id": 1
            }
        ],
        "return": "success"
    }
</ul>

<h3>Delete Cart item</h3>
<ul>
    <p>Delete a specific item in the cart with product id</p>
    <p>URL: /cart/itemDelete/{product_id}</p>
    <p>Method : DELETE</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/itemDelete/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "cart item deleted",
        "return": "success"
    }
</ul>

<h3>Clear cart</h3>
<ul>
    <p>Clear all items in cart</p>
    <p>URL: /cart/clear</p>
    <p>Method : DELETE</p>
    <p>Parameters : user_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/clear</p>

    Response Body: JSON Object
    Example:
    {
        "message": "cart cleared",
        "return": "success"
    }
</ul>

<h3>Increment Cart item</h3>
<ul>
    <p>Increment a specific item in the cart with product id by 1 (+1)</p>
    <p>URL: /cart/incQty/{product_id}</p>
    <p>Method : PUT</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/incQty/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "quantity increased",
        "return": "success"
    }
</ul>

<h3>Decrement Cart item</h3>
<ul>
    <p>Decrement a specific item in the cart with product id by 1 (-1)</p>
    <p>URL: /cart/decQty/{product_id}</p>
    <p>Method : PUT</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/decQty/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "quantity decreased",
        "return": "success"
    }
</ul>   

<h2>Wishlist APIs</h2>

<h3>Add to Wishlist</h3>
<ul>
    <p>Add a product to wishlist</p>
    <p>URL: /wishlist/{product_id}</p>
    <p>Method : POST</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/1</p>

    Request Body: JSON Object
    Example :
    {
        "message": "product added to wishlist",
        "return": "success"
    }

    Response Body: JSON Object
    Example (If product is already in wishlist):
    {
        "message": "product already in wishlist",
        "return": "success"
    }
</ul>

<h3>Get all Wishlist items</h3>
<ul>
    <p>Get all items in wishlist</p>
    <p>URL: /wishlist</p>
    <p>Method : GET</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist</p>

    Response Body: JSON Object
    Example Output:
    {
        "data": [
            {
                "cat_id": 1,
                "created_at": "Sun, 18 Dec 2022 04:05:54 GMT",
                "fast_delivery": null,
                "featured": null,
                "fresh": null,
                "id": 1,
                "modified_at": "Sun, 18 Dec 2022 04:05:54 GMT",
                "offer": null,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 1,
                "product_code": null,
                "product_desc_ar": "veg briyani 1veg briyani 1veg briyani 1veg briyani 1veg briyani 1veg briyani 1",
                "product_desc_en": "veg briyani 1veg briyani 1ac",
                "product_id": 1,
                "product_images": [
                    {
                        "id": 1,
                        "product_id": 1,
                        "product_image_url": "https://i.imgur.com/Ptusp9y.jpg"
                    },
                    {
                        "id": 2,
                        "product_id": 1,
                        "product_image_url": "https://i.imgur.com/q8PDpAp.jpg"
                    },
                    {
                        "id": 3,
                        "product_id": 1,
                        "product_image_url": "https://i.imgur.com/PRIIs60.jpg"
                    }
                ],
                "product_name_ar": "veg briyani 1",
                "product_name_en": "veg briyani 1",
                "product_stock": {
                    "id": 1,
                    "main_rack_no": null,
                    "max_stock": "3",
                    "min_stock": "12312",
                    "opening_stock": "123",
                    "product_id": 1,
                    "product_offer_price": "123",
                    "product_price": "123",
                    "product_purchase_price": "123",
                    "sub_rack_no": null
                },
                "product_subcat_id": 1,
                "status": "enable",
                "subcat_id": 1,
                "unit_quantity": "2",
                "user_id": 1
            }
        ],
        "message": "wishlist fetched",
        "return": "success"
    }
</ul>

<h3>Delete Wishlist item</h3>
<ul>
    <p>Delete a specific item in the wishlist with product id</p>
    <p>URL: /wishlist/{product_id}</p>
    <p>Method : DELETE</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "product removed from wishlist",
        "return": "success"
    }
</ul>

<h3>Clear wishlist</h3>
<ul>
    <p>Clear all items in wishlist</p>
    <p>URL: /wishlist/clear</p>
    <p>Method : DELETE</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/clear</p>

    Response Body: JSON Object
    Example:
    {
        "message": "wishlist cleared",
        "return": "success"
    }
</ul>

<h3>Check for an item in Wishlist</h3>
<ul>
    <p>Check if a specific item is in the wishlist with product id</p>
    <p>URL: /wishlist/check/{product_id}</p>
    <p>Method : GET</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/check/2</p>

    Response Body: JSON Object
    Example 1:
    {
        "message": "product in wishlist",
        "return": "True"
    }
    Example 2:
    {
        "message": "product not in wishlist",
        "return": "False"
    }
</ul>



<h2>Order APIs</h2>

<h3>Place Order</h3>
<ul>
    <p>Place an order, all items in cart will be deleted and moved to order</p>
    <p>URL: /order/{user_addr_id}</p>
    <p>Method : POST</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/1</p>

    Response Body: JSON Object
    Example:
    {
        "message": "order placed",
        "return": "success"
    }
</ul>

<h3>Get all Orders</h3>
<ul>
    <p>Get all orders</p>
    <p>URL: /order</p>
    <p>Method : GET</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/order</p>

    Response Body: JSON Object
    Example:
    {
        "orders": [
            {
                "address_id": 1,
                "created_at": "Thu, 22 Dec 2022 16:08:36 GMT",
                "id": 1,
                "modified_at": "Thu, 22 Dec 2022 16:08:36 GMT",
                "status": "cancelled",
                "total_price": "22500",
                "total_quantity": "3"
            },
            {
                "address_id": 1,
                "created_at": "Thu, 22 Dec 2022 16:09:51 GMT",
                "id": 2,
                "modified_at": "Thu, 22 Dec 2022 16:09:51 GMT",
                "status": "pending",
                "total_price": "35000",
                "total_quantity": "4"
            },
            {
                "address_id": 1,
                "created_at": "Thu, 22 Dec 2022 18:17:58 GMT",
                "id": 3,
                "modified_at": "Thu, 22 Dec 2022 18:17:58 GMT",
                "status": "pending",
                "total_price": "15000",
                "total_quantity": "2"
            }
        ],
        "return": "success"
    }
</ul>

<h3>Get specific Order</h3>
<ul>
    <p>Get a specific order with order id</p>
    <p>URL: /order/{order_id}</p>
    <p>Method : GET</p>
    <p>Parameters : order_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/1</p>

    Response Body: JSON Object
    Example:
    {
        "data": {
            "id": 1,
            "order_date": "Sun, 18 Dec 2022 04:05:54 GMT",
            "order_no": "ORD-1",
            "order_status": "pending",
            "order_total": "123",
            "user_id": 1
        },
        "message": "order fetched",
        "return": "success"
    }
</ul>


<h3>Get all Order items</h3>
<ul>
    <p>Get all items in a specific order with order id</p>
    <p>URL: /order/details/{order_id}</p>
    <p>Method : GET</p>
    <p>Parameters : order_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/details/1</p>

    Response Body: JSON Object
    Example:
    {
        "order_details": [
            {
                "cat_id": 1,
                "fast_delivery": null,
                "featured": null,
                "fk_order_id": 2,
                "fk_product_id": 3,
                "address_id": 1,
                "item_quantity":"5";
                "fresh": null,
                "offer": null,
                "order_date": "Thu, 22 Dec 2022 16:09:51 GMT",
                "order_id": 11,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 1,
                "product_code": null,
                "product_desc_ar": "849",
                "product_desc_en": "9849",
                "product_id": 3,
                "product_images": [
                    {
                        "id": 7,
                        "product_id": 3,
                        "product_image_url": "https://i.imgur.com/fsKa5Xh.jpg"
                    },
                    {
                        "id": 8,
                        "product_id": 3,
                        "product_image_url": "https://i.imgur.com/PdnR6Qu.jpg"
                    },
                    {
                        "id": 9,
                        "product_id": 3,
                        "product_image_url": "https://i.imgur.com/Hh39YnI.jpg"
                    }
                ],
                "product_name_ar": "454984",
                "product_name_en": "p3",
                "product_stock": {
                    "id": 3,
                    "main_rack_no": null,
                    "max_stock": "4",
                    "min_stock": "498",
                    "opening_stock": "98",
                    "product_id": 3,
                    "product_offer_price": "984",
                    "product_price": "1500",
                    "product_purchase_price": "984",
                    "sub_rack_no": null
                },
                "product_subcat_id": 1,
                "status": null,
                "subcat_id": 1,
                "unit_quantity": "84"
            },
            {
                "cat_id": 1,
                .
                .
                .
                .
                .
                .
                .
                .
                "status": null,
                "subcat_id": 1,
                "unit_quantity": "123"
            },
            {
                "cat_id": 1,
                .
                .
                .
                .
                .
                .
                .
                .
                "status": null,
                "subcat_id": 1,
                "unit_quantity": "651"
            }
        ],
        "return": "success"
    }
</ul>
    
<h3>Cancel Order</h3>
<ul>
    <p>Cancel a specific order with order id</p>
    <p>URL: /order/{order_id}</p>
    <p>Method : DELETE</p>
    <p>Parameters : order_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/1</p>

    Response Body: JSON Object
    Example:
    {
        "message": "order cancelled",
        "return": "success"
    }
</ul>
