import pytest

from domainmodel.artist import Artist


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