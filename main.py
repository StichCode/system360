from web_backend import create_app

app = create_app()


"""
FIXME сделать юнит тест на подключение к базе


hardcoded data:

insert into roles (name) values ('admin');
insert into roles (name) values ('owner');
insert into roles (name) values ('manager');
insert into roles (name) values ('auditor');

insert into franchises (title) values ('kfc');
insert into franchises (title) values ('coffix')

insert into users (username, email, phone, password, first_name, last_name, role, franchise_id) values ('sys30', 
'sys30', '495', '$2b$12$C.mDo4bspef/kZ3fEhdipOa0/cjItRpEe8ties/hAz/AyiE8EBH9S', 'Admin', 'Adminovich', 1, 1);

insert into shops (address, phone, user_id) values ('Moscow', '495', 1);
insert into shops (address, phone, user_id) values ('Moscow', '495', 2);


insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);
insert into objects (title, type, x, y, shop_id) values ('Table', 'table', 100, 100, 3);



"""
