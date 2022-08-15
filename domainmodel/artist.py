class Artist:
    def __init__(self, artist_id: int, full_name: str):
        self.__artist_id: int = artist_id
        if type(full_name) == int or full_name.strip(" ") == '':
            self.__full_name = "None"
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
        if type(new_full_name) != int and new_full_name.strip(" ") != '':
            self.__full_name = new_full_name.strip(' ')

    def __repr__(self):
        # we use access via the property here
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        if self.__artist_id<other.__artist_id:
            return self.__full_name<other.__full_name
        else:
            return self.__full_name>other.__full_name

    def __hash__(self):
        return hash((self.__artist_id(),self.__full_name()))
