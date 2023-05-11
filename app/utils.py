import requests
from typing import List, Tuple

class WikiDataMovieService:
    def fetch_movies(self) -> List[Tuple[str, str]]:
        query = """
        SELECT DISTINCT ?movie ?movieLabel ?imdb_id (MAX(?publication_date) AS ?release_date) WHERE {
            ?movie wdt:P31 wd:Q11424.
            ?movie wdt:P345 ?imdb_id.
            ?movie wdt:P577 ?publication_date.
            FILTER(YEAR(?publication_date) > 2013)
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }
        GROUP BY ?movie ?movieLabel ?imdb_id
        ORDER BY ASC(?release_date)
        LIMIT 100
        """

        url = 'https://query.wikidata.org/sparql'
        headers = {
            'Accept': 'application/sparql-results+json'
        }

        response = requests.get(url, headers=headers, params={'query': query})

        if response.status_code == 200:
            results = []
            for row in response.json()['results']['bindings']:
                movie_title = row['movieLabel']['value']
                imdb_id = row['imdb_id']['value']
                release_date = row['release_date']['value']
                results.append((movie_title, imdb_id, release_date))

            return results

        return None
