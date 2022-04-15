import imdb
import datetime

today = datetime.datetime.now()


class IMDBProvider(object):
    def __init__(self):
        self.ia = imdb.IMDb()

    def get_movies_ids(self, movie_str: str) -> list:
        """Get movies IDs using IMDB library"""
        movie_data = IMDBProvider.parse_request(string=movie_str)
        similar_movies = self.ia.search_movie(title=movie_data['title'])
        results = []
        for movie in similar_movies:
            if movie_data['title'].lower() in movie.data.get('title').lower():
                if movie_data['year']:
                    results.append(movie.movieID) if movie.data.get('year') == movie_data['year'] else None
                elif movie.data.get('year') in list(
                    range(today.year - 10, today.year + 1)
                ):
                    results.append(movie.movieID)
        return results

    @staticmethod
    def parse_request(string: str) -> dict:
        """
        Get movie request as a string, transform and return it as a dict
        """
        lst = string.split('-')
        data = dict(title=lst[0].strip())
        if len(lst) > 1:
            try:
                year = int(lst[1].strip())
            except ValueError:
                year = None
        else:
            year = None
        data['year'] = year
        return data
