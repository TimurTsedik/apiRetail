# apiRetail

The E-Shop REST API is a fully-featured, backend service designed for managing an e-commerce platform. It allows users, customers, and administrators to interact with the shop’s core functionalities such as products, orders, and customer profiles through secure and efficient API endpoints. Built with Django Rest Framework (DRF), this API is optimized for high-performance and scalable web applications, facilitating seamless communication between the frontend and backend.

Key Features

1. User Authentication & Management

	•	Authentication: Secure user authentication using token-based authentication (provided by DRF’s rest_framework.authtoken).
	•	Authorization: All user actions are securely managed through role-based access control, ensuring that only authenticated users can interact with their respective resources.
	•	User Registration & Login: Customers can sign up for an account, log in, and manage their profile information.
	•	Profile Management: Users can update personal information such as their name, email, phone number, and delivery address.

2. Product Management

	•	View All Products: Customers can view a list of available products with details such as name, description, price, supplier, and quantity.
	•	Filter Products by Supplier: The API allows customers to filter products by a specific supplier for a more customized shopping experience.
	•	Get Specific Product Information: Customers can retrieve detailed information for any specific product by its ID.

3. Order Management

	•	Place Orders: Customers can place orders by confirming items from their shopping cart and providing a delivery contact.
	•	Order Status: Orders are associated with various statuses such as pending, confirmed, shipped, delivered, and canceled. Customers and administrators can track the current status of each order.
	•	Update Order Status: Administrators or authorized users can update the status of an order, ensuring proper order processing flow from confirmation to delivery.
	•	Retrieve Order Information: Customers can view their past and current orders, including order details, contact information, and status.
	•	Email Notifications: Upon order confirmation, customers receive an email notification with the details of their order.

4. Cart Management

	•	Cart Confirmation: The API enables customers to confirm their shopping cart before placing an order. Items in the cart are cleared once the order is confirmed.
	•	Add to Cart: Customers can add products to their shopping cart, adjusting quantities as needed before placing an order.

5. Contact & Address Management

	•	Add/Remove Delivery Address: Customers can manage multiple delivery addresses and contact information (first name, last name, email, phone, address) for order fulfillment.
	•	View Saved Contacts: Customers can view all previously saved delivery addresses and contact information.
	•	Delete Contacts: Users can delete a specific delivery address if no longer needed.

6. Order Confirmation and Email Integration

	•	Order Confirmation Email: After successfully placing an order, customers receive an email confirming the order details, including order ID, items purchased, and delivery information.
	•	Customizable Confirmation: The system supports customizable email templates for different stages of the order lifecycle, ensuring professional communication with customers.

Technologies and Design

	•	Backend: The API is built on Django Rest Framework (DRF), leveraging its robust features to provide efficient data handling, serialization, and authentication.
	•	Database: The API integrates with a PostgreSQL database to store user, product, order, and contact information in a reliable and scalable manner.
	•	Authentication: Token-based authentication ensures that users can securely interact with their orders and account details without compromising data integrity.
	•	Error Handling: Built-in error handling provides informative messages, allowing developers to easily troubleshoot issues.

Use Cases

	•	Customers: Customers can register, log in, browse products, place orders, manage their cart, track orders, and update personal contact information.
	•	Administrators: Administrators can manage the status of customer orders, view customer data, and interact with the API to handle specific order workflows such as shipping or delivery.

API Endpoints Overview

	1.	Authentication:
	•	/auth/login/: User login.
	•	/auth/logout/: User logout.
	2.	Product Management:
	•	/products/: List all products.
	•	/products/{id}/: Get details of a specific product.
	•	/products/?supplier={id}: Filter products by supplier.
	3.	Order Management:
	•	/orders/: List all orders for the authenticated user.
	•	/orders/{id}/: Retrieve a specific order by ID.
	•	/orders/confirm/: Confirm an order based on the cart and contact ID.
	•	/orders/{id}/update-status/: Update the status of a specific order (available for authorized users).
	4.	Cart Management:
	•	/cart/: Manage items in the cart (add, view, remove).
	5.	Contact Management:
	•	/contacts/: View all saved contacts.
	•	/contacts/{id}/: Add or remove a contact.


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