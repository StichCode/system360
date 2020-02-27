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
    
    
##### Urls for Admin:
    GET    /admin/franchises
    POST   /admin/franchises
    DELETE /admin/franchises?id=?
    PUT    /admin/franchises
    
    GET    /admin/users
    POST   /admin/users
    DELETE /admin/users?id=?
    PUT    /admin/users
    
    GET    /admin/objects
    POST   /admin/objects
    DELETE /admin/objects?id=?
    PUT    /admin/objects
    
    GET    /admin/shops
    POST   /admin/shops
    DELETE /admin/shops
    PUT    /admin/shops
    
    GET    /admin/checkouts
    POST   /admin/checkouts   
    DELETE /admin/checkouts?id=? 
    
    GET    /admin/tasks
    POST   /admin/tasks
    DELETE /admin/tasks?id=?
    
##### ENV for project
     FLASK_CONFIG            config.BaseConfig
     DATABASE_URL            postgresql+psycopg2://user:pass@url:port/database
     TEST_DATABASE_URL
     PRODUCTION_DATABASE_URL
     FLASK_APP               app/main.py