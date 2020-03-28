# Coffix 360

##### Requirements for project
    apt install memcached
    memcached -u memcached -d -m 1024 -l 127.0.0.1 -p 11211
    pip install -r requirements.txt
    
    
##### Urls of project:
    POST /api/auth
    POST /api/refresh
   
##### Urls for API:
    GET, POST, PUT, DELETE (all data with pagination and data with criterie):    
        /api/roles
        /api/franchises
        /api/users 
        /api/objects
        /api/shops
        /api/checkouts
        /api/tasks
        /api/subtasks    
    

    
##### ENV for project
     FLASK_CONFIG            config.BaseConfig
     DATABASE_URL            postgresql+psycopg2://user:pass@url:port/database
     TEST_DATABASE_URL
     PRODUCTION_DATABASE_URL
     FLASK_APP               app/main.py