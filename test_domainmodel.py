import pytest

from domainmodel.artist import Artist
from domainmodel.genre import Genre


class TestArtist:

    def test_construction(self):
        artist1 = Artist(1, 'Tailor Swift')
        assert str(artist1) == "<Artist Tailor Swift, artist id = 1>"
        artist2 = Artist(2, "Maroon 5")
        assert str(artist2) == '<Artist Maroon 5, artist id = 2>'
        artist3 = Artist(3, 'Kate Bush')
        assert str(artist3) == '<Artist Kate Bush, artist id = 3>'
        artist4 = Artist(4, ' Bad Bunny ')# Test full_name with trailing spaces
        assert str(artist4) == '<Artist Bad Bunny, artist id = 4>'
        artist5 = Artist(5, 2910)# Test invalid type for the full_name sets it to None
        assert str(artist5.full_name) == 'None'
        artist6 = Artist(-1, 'Tailor Swift')# Test when the artist id type is invalid
        assert str(artist6) == 'This is invalid artist id'

class TestGener:

    def test_construction(self):
        genre1 = Genre(1, 'Jazz ')
        assert str(genre1) == '<Genre Jazz, genre id = 1>'
        genre2 = Genre(2, ' Electronic ')
        assert str(genre2) == '<Genre Electronic, genre id = 2>'
        genre3 = Genre(3, 300) # Test invalid types for a name sets it to None
        assert str(genre3.name) == 'None'
        genre4 = Genre(1, 'Jazz')
        genre4.name = 'New Jazz'
        assert str(genre4) == '<Genre New Jazz, genre id = 1>'
        genre5 = Genre(-2, 'Jazz')# Test invalid id raises error
        assert str(genre5) == 'This is invalid gener id'