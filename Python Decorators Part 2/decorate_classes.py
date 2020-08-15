class MovieDatabase:

    def __init__(self, db):
        self.db = db
    
    @exception_logger
    def get_all_movies_of_an_actor(self, actor_name):
        return filter(lambda movie: actor_name in movie["actors"], self.db)


from typing import List
from dataclasses import dataclass

@dataclass
class Movie:
    actor: str
    year: int
    genre: List[str]
