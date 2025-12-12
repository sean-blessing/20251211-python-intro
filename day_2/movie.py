class Movie:
    # constructor
    def __init__(self, id, title, year, rating, director):
        self._id = id
        self._title = title
        self._year = year
        self._rating = rating
        self._director = director

    def detail(self):
        det_str = (f"{self._id} - {self._title}({self._year}), rated {self._rating}, "
                   f"directed by {self._director}")
        return det_str