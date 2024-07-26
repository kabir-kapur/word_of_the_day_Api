# Word of the Day
Generates a new word for users to learn and enjoy every day.
## Backend Package
Handles backend logic and URI routing for requests to the Word of the Day API. 
### Getting Started
To get the WOD Django server spun up: `❱ python3 manage.py runserver`
#### `/manage.py`
- Executes the WOD Django server.
#### The `word_of_the_day/views` folder
- Houses business logic for each WOD API and distributes the corresponding `main` method for each bite-sized piece of logic.
#### `word_of_the_day/asgi.py`
- I have no fucking idea
#### `word_of_the_day/urls.py`
- Uses Django to manage routing requests to each WOD API to their corresponding view
#### `word_of_the_day/wsgi.py`
- Literally no idea
