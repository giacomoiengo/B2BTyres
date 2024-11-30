# B2BTyres, _a demo project_

### When and why?
This project was made in the **summer of 2022** between one university exam and another, in about 15 days. \
The **goal** was to experiment with technologies like *postgreSQL*, *Django* and *Bootstrap*.

### What? (specification)
The specification was to build a **system for selling tires** to customers.\
Moreover the system had to be used by `supervisors`, `salesmen` and `customers`. In particular:
- a supervisor must be able to do CRUD operations on salesmen,
- a salesman must be able to do CRUD operations on customers,
    - when a salesman add a customer, he must be able to specify a `markup` and a `discout` percentage for that customer, which will then be applied to the actual price of the products,
- a customer must be able to search and filter the available `products`, add them to the `basket` and then eventually `order` them.

### Currently
I have now (in **november 2024**) rediscovered this project, so I proceeded to dockerize it and publish it here on GitHub.

### Run
```bash
cd B2BTyres/
docker compose build --no-cache
docker compose up
```

### Usage
The inizialization process automatically populates the DB with demo products, and creates a supervisor demo account whose credential are `supervisorDemo:supervisorDemo`. Once the containers are up and running you can:
1. open `http://127.0.0.1:8000` on your browser,
2. login with the supervisor demo account and create new salesmen accounts,
3. login with a salesman account and create new customers accounts,
4. login with a customer account and search products, add them the basket and order them