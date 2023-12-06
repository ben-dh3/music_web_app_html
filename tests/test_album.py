from lib.album import Album

def test_album_constructs():
    album = Album(1, "Test Album", "1997", 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == "1997"
    assert album.artist_id == 1

def test_album_format_nicely():
    album = Album(1, "Test Album", "1997", 1)
    assert str(album) == "Album(1, Test Album, 1997, 1)"

def test_albums_are_equal():
    album1 = Album(1, "Test Album", "1997", 1)
    album2 = Album(1, "Test Album", "1997", 1)
    assert album1 == album2