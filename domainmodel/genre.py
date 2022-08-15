class Genre:
    def __init__(self, genre_id: int, name: str):
        if not isinstance(genre_id, int) or genre_id <= 0:
            raise ValueError("This is invalid genre id")
        else:
            self.__genre_id: int = genre_id
        
        if not isinstance(name, str):
            self.__name = None
        else:
            self.__name = name.strip()

    @property
    def genre_id(self) -> int:
        return self.__genre_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            self.__name = None
        else:
            self.__name = new_name.strip()
        
    def __repr__(self):
        return f"<Genre {self.__name}, genre id = {self.genre_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id == other.genre_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id < other.genre_id

    def __hash__(self):
        return self.__genre_id
            