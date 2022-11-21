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


    
    
    
    
