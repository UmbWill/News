# News
Collect news and show them.

With this repository we want download the news from https://newsapi.org/ and show 20 news via html and 100 news as json.

Clone the repository from github.

The very first operation will be create an enviroment with pipenv and run it:

```
pipenv install
pipenv shell
```

When you will be inside the enviroment, install all packages using the requirements.txt file
```
pip install -r requirements.txt
```
The enviroment could be fine now, we can move on to the migration.

In order to create all the tables inside our database we run the migration as follow:
```
python manage.py makemigrations news
python manage.py migrate
```

Finally run our django server
```
python manage.py runserver
```

The main page will be in http://127.0.0.1:8000/news/ , see the wiki for some images.
