<h1>Instalation</h3>

<p>First, make a virtualenv and acticate it.</p>

<p>Now we will install the dependencies.</p>

```
$ pip install -r requirements.txt
```

<p>Now make sure your mongo is working. If all works well, this is the next step:</p>

```
$ python manage.py makemigrations app
$ python manage.py migrate
```

<p>This will create the database and the documents. And now, just run the server!</p>

```
$ python manage.py runserver
```
