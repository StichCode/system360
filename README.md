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
    
    
    
##### Fields for create anything

    ROLE       ["name"] (str)
    FRANCHISE  ["title"] (str)
    USER       ["username", "email", "phone", "password", "first_name", "last_name", "role", "franchise_id"]
               (str, str, str,str,str,str, int, int)
    
    SHOP        ["address", "phone", "user_id"] (str,str,int)
    OBJECT      ["title", "type", "x", "y", "shop_id"] (str,str,int,int,int)
    
    CHECKOUTS    ["shop_id", "start", "end", "worker", "type"] (int, str(31-12-2019 23:49), str, int, str(ENUM))
    TASKS        ["object_id", "checkout", "status", "title"] (int, int, bool, str)
    SUBTASKS     ["task", "title"] (int, str)
    
##### ENV for project
     FLASK_CONFIG            config.BaseConfig
     DATABASE_URL            postgresql+psycopg2://user:pass@url:port/database
     TEST_DATABASE_URL
     PRODUCTION_DATABASE_URL
     FLASK_APP               app/main.py