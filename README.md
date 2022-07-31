# Django Web Scraping

<p>
This project contains webscraping and storing of the scrapped data inside a database.
</p>

## Run Locally

After installing python 3 on your local device

Clone the project locally

```
git clone
```

Navigate inside the project directory

```
cd web-scrap
```

Create a virtual environment and activate it

```
python3 -m virtualenv venv

$ source venv/bin/activate
```

Install Requirements

```
pip install -r requirements.txt
```

Insert scrapped data into database

```
python3 manage.py init_db
```

To test the app

```
python3 manage.py test
```

Start the server locally

```
python3 manage.py runserver
```

Features of this app

<ul>
    <li>
    search data with keyword "q" that searches from title, author name, author designation <code>localhost:8000/?q={value}</code>
    </li>
    <li>
    pagination and page_size <code>localhost:8000/?page={page number}</code><br/><code>localhost:8000/?page_size={page size}</code>
    </li>
    <li>
    dockerfile and docker-compose files that works
    </li>

</ul>

### Project runs on <code>localhost:8000</code> by default
