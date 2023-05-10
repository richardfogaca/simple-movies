# Movie Ingestion

This project demonstrates how to build a simple application using Flask-AppBuilder that retrieves movie data from the Wikidata API, processes the JSON data, saves it to an SQLite3 database using SQLAlchemy, and displays it in a simple interface.

## Prerequisites

- Python 3.9.6 or higher
- A virtual environment (recommended)

## Installation

Follow these steps to set up the project:

1. Clone the repository:

```bash
$ git clone https://github.com/richardfogaca/simplemovies.git
$ cd simplemovies
```

2. Create a virtual environment and activate it:

```python
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install the required dependencies:

```python
(venv) $ pip install -r requirements.txt
```

4. Set the FLASK_APP environment variable:

```bash
$ export FLASK_APP=SimpleApp/run.py
```

## Configuration

1. Configure the Flask app by updating the config.py file as needed. The default configuration uses SQLite3 as the database.


## Database Setup
1. Create the database tables:

```python
>>> from app import db
>>> db.create_all()
```

2. To create an admin user, run:

```python
(venv) $ flask fab create-admin
```

## Running the Application

1. Run the application:
```python
(venv) $ python3 run.py
```

2. To load movies data use the following endpoint. This will fetch the data from wikidata and list using Flask-AppBuilder
http://127.0.0.1:5000/movies/load_data/

3. If you would like to delete all data from the database, just use the folowing endpoint:
http://127.0.0.1:5000/movies/drop_data/