class Genre:
    def __init__(self,genre_id: int, name: str):
        if not isinstance(genre_id, int) or genre_id <= 0:
            raise ValueError("This is invalid genre id")
        else:
            self.genre_id: int = genre_id
        
        if not isinstance(name, str):
            self.name = None
        else:
            self.name = name.strip()

        @property
        def genre_id(self) -> int:
            return self.gener_id

        @property
        def name(self) -> str:
            return self.name

        @name.setter
        def name(self, new_name):
            if not isinstance(name, str):
                self.name = None
            else:
                self.name = name.strip()
        
        def __repr__(self):
            return f"<Genre {self.name}, genre id = {self.genre_id}>"

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return self.genre_id == other.genre_id

        def __lt__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return self.genre_id < other.genre_id

        def __hash__(self):
            return self.genre_id
            