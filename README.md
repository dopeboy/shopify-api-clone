# shopify-api-clone

This is part of the technical interview for backend developer candidates for Coop Commerce.

## Setup

1. Clone this repo and `cd` into it
2. Create the virtual environment: `python3 -m venv venv`
3. Enter the virtual environment: `source venv/bin/activate`
4. Download the necessary packages: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver`
7. Run `curl 'http://127.0.0.1:8000/api/ping/' | python -mjson.tool`. If it works, you should see `{
    "status": "pong"
}
`

## Exercise

We want to understand your proficiency with Django, Django REST Framework, and backend API development.

Please write an API that mimics the shopify API using the following specifications:

1. There are stores and each one has a set of products.
2. There are users, some of whom have bought products.
3. There are tags (e.g. 'women over 30', 'men under 25', etc). They are applied to stores to specify their category (only one can be set). They are also applied to a user to specify their preferences (many can be applied).
4. No frontend code required, only backend.
5. No auth code needed; assume anonymous users can do everything.

## Test cases

1. `POST` /api/stores creates a store.
2. `POST` /api/users creates a user.
3. `POST` /api/purchases creates a purhase.
4. `GET` /api/stores/1 retrieves a store. Each store has a list of products and a category.
5. `GET` /api/users/1 retrieves a user. Each user has a list of preferences.
6. `GET` /api/purchases/1 retrieves a purhase.

## Procedure

1. Create a branch, write your code, and submit a PR with the output for the test cases above.

## Bonus

Suppose we wanted to give recommendations to users on what they should buy in the future based off what they've bought in the past. Draft some pseudo-code to describe how you'd do this.
