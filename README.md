# Coffix 360

##### Requirements for project
    apt install memcached
    memcached -u memcached -d -m 1024 -l 127.0.0.1 -p 11211
    pip install -r requirements.txt
    
    
##### Urls of project:
    POST /api/auth
    POST /api/refresh
    
    GET /api/users?role=Manager
    
    GET /api/shops?userId=1
    
    GET /api/map?shopId=1
    
    
##### Urls for API:
    GET    /api/franchises
    POST   /api/franchises
    DELETE /api/franchises?id=?
    PUT    /api/franchises
    
    GET    /api/users
    POST   /api/users
    DELETE /api/users?id=?
    PUT    /api/users
    
    GET    /api/objects
    POST   /api/objects
    DELETE /api/objects?id=?
    PUT    /api/objects
    
    GET    /api/shops
    POST   /api/shops
    DELETE /api/shops
    PUT    /api/shops
    
    GET    /api/checkouts
    POST   /api/checkouts   
    DELETE /api/checkouts?id=? 
    
    GET    /api/tasks
    POST   /api/tasks
    DELETE /api/tasks?id=?
    
    GET    /api/subtasks
    POST   /api/subtasks
    DELETE /api/subtasks?id=?
    
    
    GET    /api/roles?test=true
    
    
##### Fields for create anything

    Keys to dict you can checked on:
    
    GET:
        ROLE                /keys/role
        USER                /keys/user
        SHOP                /keys/shop
        OBJECT              /keys/object
        FRANCHISE           /keys/franchise
        CHECKOUT            /keys/checkout
        CHECKOUT TASK       /keys/checkout_task
        CHECOUT SUB TASK    /keys/checkout_sub_task
    
##### ENV for project
     FLASK_CONFIG            config.BaseConfig
     DATABASE_URL            postgresql+psycopg2://user:pass@url:port/database
     TEST_DATABASE_URL
     PRODUCTION_DATABASE_URL
     FLASK_APP               app/main.py