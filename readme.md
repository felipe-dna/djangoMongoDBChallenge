<h1>Available here</h1>
- https://thumbsupcounter.herokuapp.com/


<h1>Installation</h3>

<p>First, make a virtualenv and acticate it.</p>

```
$ virtualenv --python='/usr/bin/python3.7' venv
$ source venv/bin/activate
```

<p>Now we will install the dependencies.</p>

```
$ pip install -r requirements.txt
```

<p>Create a .env file and put the follow values:</p>

```
DB_NAME=<your-db-name>
DB_HOST=<your-db-host>
DB_USER=<your-db-user>
DB_PASSWORD=<your-db-password>
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
