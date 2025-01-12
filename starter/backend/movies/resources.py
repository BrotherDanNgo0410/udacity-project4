from flask import jsonify
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {
        "title": "Venom 2",
        "description": "Superhero movie"
    },
    "1010": {"title": "Avenger: End Games", "description": "Action movie"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
    "110": {"title": "Fast and Furious", "description": "action movie"},
    "1102": {"title": "Transformer 1", "description": "Superhero movie"},
    "1108": {"title": "Dr Strange", "description": "Superhero movie"},
    "1103": {"title": "Titanic", "description": "Drama movie"},
    "1111": {"title": "Mùi cỏ cháy", "description": "Vietnamese movie"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            # Return a list of all movies
            movies_data = [
                dict({"title": movie["title"]}, **{"id": i})
                for i, movie in movies.items()
            ]
            response_data = {"movies": movies_data}
            return jsonify(response_data)
        else:
            # Return the details of a specific movie
            return jsonify({"movie": movies[str(movie_id)]})
