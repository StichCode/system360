# Coffix 360

##### Requirements for project
    apt install memcached
    memcached -u memcached -d -m 1024 -l 127.0.0.1 -p 11211
    pip install -r requirements.txt
    
    
##### Urls of project:
    POST /api/auth
    POST /api/reg
    GET /api/users?role=Manager
    POST /api/refresh
    GET /api/shops?userId=1
    GET /api/map?shopId=1