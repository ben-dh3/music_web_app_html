from playwright.sync_api import Page, expect
from lib.album_repository import *
from lib.album import *
from lib.artist_repository import *
from lib.artist import *
# Tests for your routes go here

"""
When we call get_albums
We get an html page of album objects reflecting the seed data.
"""

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    a_tags = page.locator("a")
    expect(a_tags).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa",
        "Title: Waterloo",
        'Add Album',
    ])


def test_get_album_by_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Title: Doolittle",
        "Released: 1989",
    ])

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Title: Surfer Rosa'")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Title: Surfer Rosa",
        "Released: 1988",
    ])

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    a_tags = page.locator("a")
    expect(a_tags).to_have_text([
        "Name: Pixies",
        "Name: ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone",
        'Add Artist',
    ])

def test_get_artist_by_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Name: Pixies",
        "Genre: Rock",
    ])

def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Name: Pixies'")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Name: Pixies",
        "Genre: Rock",
    ])

def test_create_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add Album'")

    page.fill('input[name=title]', "Test Album")
    page.fill('input[name=release_year]', "1234")
    page.click('text=Add Album')

    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Title: Test Album",
        "Released: 1234",
    ])

def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add Artist'")

    page.fill('input[name=name]', "Test Artist")
    page.fill('input[name=genre]', "Test Genre")
    page.click('text=Add Artist')

    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Name: Test Artist",
        "Genre: Test Genre",
    ])


# Create a new albums
# Request: POST /albums
#   With body parameters: "title=Voyage&release_year=2022&artist_id=2"
# Response: None (just creates the resource on the server)

# def test_post_albums(web_client, db_connection):
#     db_connection.seed('seeds/music_library.sql')
#     response = web_client.post('/albums', data={
#         'title': 'Voyage',
#         'release_year': 2022,
#         'artist_id': 2
#     })
#     assert response.status_code == 200
#     response = web_client.get('/albums')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#     "Album(1, Invisible Cities, 2005, 1)\n" \
#     "Album(2, Voyage, 2022, 2)"

# def test_get_artists(web_client, db_connection):
#     db_connection.seed('seeds/music_library.sql')
#     response = web_client.get('/artists')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#         'Pixies'
    
# def test_post_artists(web_client, db_connection):
#     db_connection.seed('seeds/music_library.sql')
#     response = web_client.post('/artists', data={
#         'name': 'Wild nothing',
#         'genre': 'Indie'
#     })
#     assert response.status_code == 200
#     response = web_client.get('/artists')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#     "Pixies\n" \
#     "Wild nothing"

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# === End Example Code ===
