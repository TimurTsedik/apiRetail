# apiRetail

## start DB
docker-compose up -d

## migrations
python manage.py makemigrations
python manage.py migrate

## import data
python manage.py import_products

## make user
python manage.py createsuperuser

## run server
python manage.py runserver

## create user
curl -X POST http://127.0.0.1:8000/register/ \
    -H "Content-Type: application/json" \
    -d '{
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword123"
    }'
response:
{"message":"User created successfully"}

## login and get token
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
    -H "Content-Type: application/json" \
    -d '{
        "username": "testuser",
        "password": "testpassword123"
    }'
response:
{"token":"3ee0f32e3f7f20b98cb1c95a74651dc8cf9832fe"}

## get products
curl -X GET http://127.0.0.1:8000/products/ \
    -H "Authorization: Token your-auth-token-here"
response:
[{"id":1,"name":"Смартфон Apple iPhone XS Max 512GB (золотистый)","description":"","supplier":1,"price":"110000.00","quantity":14,"parameters":{"Диагональ (дюйм)":6.5,"Разрешение (пикс)":"2688x1242","Встроенная память (Гб)":512,"Цвет":"золотистый"}}, ...

## add product to cart
curl -X POST http://127.0.0.1:8000/cart/ \
    -H "Authorization: Token your-auth-token-here" \
    -H "Content-Type: application/json" \
    -d '{
        "product": 1,
        "quantity": 2
    }'
response:
{"id":2,"user":4,"product":1,"quantity":2}

## view cart
curl -X GET http://127.0.0.1:8000/cart/ \
    -H "Authorization: Token your-auth-token-here"
response:
[{"id":2,"user":4,"product":1,"quantity":2}]

## add contact
curl -X POST http://127.0.0.1:8000/contacts/ \
    -H "Authorization: Token your-auth-token-here" \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@example.com",
        "phone": "1234567890",
        "address": "5th Avenue, New York, NY 10011"
    }'
response:
{"id":3,"first_name":"Smith","last_name":"Doe","email":"john.smith@example.com","phone":"1234567890","address":"5th Avenue, New York, NY 10011"}

## view contacts

curl -X GET http://127.0.0.1:8000/contacts/ \
    -H "Authorization: Token your-auth-token-here"
response:
[{"id":3,"first_name":"John","last_name":"Smith","email":"john.smith@example.com","phone":"1234567890","address":"5th Avenue, New York, NY 10011"}]

## remove contact
curl -X DELETE http://127.0.0.1:8000/contacts/1/ \
    -H "Authorization: Token your-auth-token-here"

## confirm order
curl -X POST http://127.0.0.1:8000/orders/confirm/ \
    -H "Authorization: Token 3ee0f32e3f7f20b98cb1c95a74651dc8cf9832fe" \
    -H "Content-Type: application/json" \
    -d '{
        "cart_id": 2,
        "contact_id": 3
    }'
response:
{"status":"Order confirmed successfully","order_id":8}


