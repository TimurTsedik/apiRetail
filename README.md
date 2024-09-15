# apiRetail

## start DB
```bash
docker-compose up -d
```

## migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## import data
```bash
python manage.py import_products
```

## make user
```bash
python manage.py createsuperuser
```

## run server
```bash
python manage.py runserver
```

## create user
```bash
curl -X POST http://127.0.0.1:8000/register/ \
    -H "Content-Type: application/json" \
    -d '{
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword123"
    }'
```
response:
{"message":"User created successfully"}

## login and get token
```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
    -H "Content-Type: application/json" \
    -d '{
        "username": "testuser",
        "password": "testpassword123"
    }'
```
response:
{"token":"3ee0f32e3f7f20b98cb1c95a74651dc8cf9832fe"}

## get products
```bash
curl -X GET http://127.0.0.1:8000/products/ \
    -H "Authorization: Token your-auth-token-here"
```
response:
[{"id":1,"name":"Смартфон Apple iPhone XS Max 512GB (золотистый)","description":"","supplier":1,"price":"110000.00","quantity":14,"parameters":{"Диагональ (дюйм)":6.5,"Разрешение (пикс)":"2688x1242","Встроенная память (Гб)":512,"Цвет":"золотистый"}}, ...

## add product to cart
```bash
curl -X POST http://127.0.0.1:8000/cart/ \
    -H "Authorization: Token your-auth-token-here" \
    -H "Content-Type: application/json" \
    -d '{
        "product": 1,
        "quantity": 2
    }'
```
response:
{"id":2,"user":4,"product":1,"quantity":2}

## view cart
```bash
curl -X GET http://127.0.0.1:8000/cart/ \
    -H "Authorization: Token your-auth-token-here"
```
response:
[{"id":2,"user":4,"product":1,"quantity":2}]

## add contact
```bash
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
```
response:
{"id":3,"first_name":"Smith","last_name":"Doe","email":"john.smith@example.com","phone":"1234567890","address":"5th Avenue, New York, NY 10011"}

## view contacts
```bash
curl -X GET http://127.0.0.1:8000/contacts/ \
    -H "Authorization: Token your-auth-token-here"
```
response:
[{"id":3,"first_name":"John","last_name":"Smith","email":"john.smith@example.com","phone":"1234567890","address":"5th Avenue, New York, NY 10011"}]

## remove contact
```bash
curl -X DELETE http://127.0.0.1:8000/contacts/1/ \
    -H "Authorization: Token your-auth-token-here"
```

## confirm order
```bash
curl -X POST http://127.0.0.1:8000/orders/confirm/ \
    -H "Authorization: Token your-auth-token-here" \
    -H "Content-Type: application/json" \
    -d '{
        "cart_id": 2,
        "contact_id": 3
    }'
```
response:
{"status":"Order confirmed successfully","order_id":8}

## orders list
```bash
curl -X GET http://127.0.0.1:8000/orders/ \
    -H "Authorization: Token your-auth-token-here"
``` 
response:
[{"id":6,"customer":4,"created_at":"2024-09-15T12:32:56.867272Z","updated_at":"2024-09-15T13:06:17.864354Z","contact":null,"items":[{"product":1,"quantity":2,"price":"110000.00"},{"product":3,"quantity":1,"price":"65000.00"}]}, ...]
