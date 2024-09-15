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

## get product
```bash
curl -X GET http://127.0.0.1:8000/products/\1/ \
    -H "Authorization: Token your-auth-token-here"
```
response:
{"id":1,"name":"Смартфон Apple iPhone XS Max 512GB (золотистый)","description":"","supplier":1,"price":"110000.00","quantity":14,"parameters":{"Диагональ (дюйм)":6.5,"Разрешение (пикс)":"2688x1242","Встроенная память (Гб)":512,"Цвет":"золотистый"}}

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

## update contact
```bash
curl -X POST http://127.0.0.1:8000/contacts/ \
    -H "Authorization: Token <your_token>" \
    -H "Content-Type: application/json" \
    -d '{
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "address": "456 New St, New City, Country"
    }'
```
response:
{"id":4,"first_name":"John","last_name":"Doe","email":"john.doe@example.com","phone":"1234567890","address":"456 New St, New City, Country"}

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

mail sent to contact's email (in developing stage, is printed in console):

```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order Confirmation - 8
From: admin@example.com
To: testuser@example.com
Date: Sun, 15 Sep 2024 14:24:11 -0000
Message-ID: <172641025162.6170.11250587817648987203@1.0.0.127.in-addr.arpa>

Thank you for your order. Order ID: 9
-------------------------------------------------------------------------------
```

## orders list
```bash
curl -X GET http://127.0.0.1:8000/orders/ \
    -H "Authorization: Token your-auth-token-here"
``` 
response:
[{"id":6,"customer":4,"created_at":"2024-09-15T12:32:56.867272Z","updated_at":"2024-09-15T13:06:17.864354Z","contact":null,"items":[{"product":1,"quantity":2,"price":"110000.00"},{"product":3,"quantity":1,"price":"65000.00"}]}, ...]

## get order
```bash
curl -X GET http://127.0.0.1:8000/orders/6/ \
    -H "Authorization: Token your-auth-token-here"
``` 
response:
{"id":6,"customer":4,"contact":null,"created_at":"2024-09-15T12:32:56.867272Z","updated_at":"2024-09-15T13:06:17.864354Z","status":"pending","items":[{"product":1,"quantity":2,"price":"110000.00"},{"product":3,"quantity":1,"price":"65000.00"}]}

## order status update
```bash
curl -X PATCH http://127.0.0.1:8000/orders/1/update-status/ \
    -H "Authorization: Token YOUR_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "status": "shipped"
    }'
```
response:
{"status":"Order status updated to shipped"}