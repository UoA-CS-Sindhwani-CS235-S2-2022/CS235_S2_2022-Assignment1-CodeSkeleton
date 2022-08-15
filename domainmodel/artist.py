class Artist:
    def __init__(self, artist_id: int, full_name: str):
        if artist_id < 0 or not isinstance(artist_id, int):
            raise ValueError("This is invalid artist id")
        else:
            self.__artist_id: int = artist_id
        if not isinstance(full_name, str):
            self.__full_name = None
        else:
            self.__full_name = full_name.strip(' ')

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        if not isinstance(new_full_name, str):
            self.__full_name = None
        else:
            self.__full_name = new_full_name.strip(' ')

    def __repr__(self):
        # we use access via the property here
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id<other.artist_id

    def __hash__(self):
        return self.__artist_id
