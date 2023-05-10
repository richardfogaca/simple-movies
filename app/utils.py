import requests

def fetch_movie_data():
    query = """
    SELECT DISTINCT ?movie ?movieLabel ?imdb_id (MAX(?publication_date) AS ?latest_publication_date) WHERE {
        ?movie wdt:P31 wd:Q11424.
        ?movie wdt:P345 ?imdb_id.
        ?movie wdt:P577 ?publication_date.
        FILTER(YEAR(?publication_date) > 2013)
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    GROUP BY ?movie ?movieLabel ?imdb_id
    LIMIT 100
    """

    url = 'https://query.wikidata.org/sparql'
    headers = {
        'Accept': 'application/sparql-results+json'
    }

    response = requests.get(url, headers=headers, params={'query': query})

    if response.status_code == 200:
        return response.json()

    return None
