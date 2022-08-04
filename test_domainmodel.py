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
