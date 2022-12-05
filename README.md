# An Ecommerce API.

## Introduction

### Installations
- pip install requirements.txt to install all the dependecies for the project.


In this Ecommerce API Project it will return three(3) types of error when the request fails:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed


### Endpoints
#### GET /products, /products/<int:pk>
- General
  - Returns a list of products.
  - Delete, update and get a particular product.
  
  
#### GET /category, /category/<int:pk>
- General 
  - Returns a list of categories.
  - Get, Update and Delete a particular category
  
#### GET /reviews/<int:pk>/list, /reviews/<int:pk>/details
- General 
  - Returns a list of reviews for a particular product.
  - Get, Update and Delete a particular review for a product.

#### GET /customer/cart, /customer/cart/<int:pk>
- General
  - Gives cart for a customer.
  - Updates and Delete a particular product for a customer.
  
#### POST /products/create
- General
  - Create a product.
  
#### POST /category/create
- General
  - Create a category for the products.

#### POST /

