# Movie Rating System
## About it
* Here I used Django framework(Python) and sqlite3 database.
* In the given json file there was a field called "phone". But django default user do not have "phone" field in-built. So, I made a custom user including phone field in it.
* I created custom password validator called "AllowSimplePasswordValidator" so that it can take simple password of any types and lengths.
* In given json file there was a white space in name/username like "John Doe". But django username field does not accept white space by default. So, I made a custom udername validator. called "ASCIIUsernameValidator" and attached it with the username field so that it can accept white space in it.
* I have created models named 'Movie' and 'Rating'. The fields of these models are named to match those of the sample data.
* I initialized the database with sample data given in json file.

## functionality
you can access the API endpoints at http://localhost:8000/api/ and perform the following operations:
* User Login: You can login from the django admin at http://localhost:8000/admin/ with the user's credentials or you can send a POST request to /api/users/ with the user's credentials in the request body.
* Add a Movie: You can send a POST request to /api/movies/ with the movie details in the request body(raw data/HTML form).
* View List of Movies: You can send a GET request to /api/movies/ to retrieve a list of all movies.
* Rate a Movie: You can send a POST request to /api/ratings/ with the user ID, movie ID, and rating in the request body.
* Search and View Specific Movie Details: You can send a GET request to /api/movies/<movie_id>/ratings/ to retrieve the movie details, list of ratings, and average rating for a specific movie.
* I used routers in it. It can return json responses with proper error handling.

## How to setup
* Run git clone https://github.com/azmain-rahi/Movie_Rating_System.git
* Go to project folder cd movie_rating/
* Create a Virtual Environment(recomended not required):python -m venv env(to create), env\Scripts\activate(to activate)
* Run pip install django (if required)
* Run pip install djangorestframework (if required)
* open settings.py and configure database
* Run python manage.py migrate
* Run python manage.py runserver

