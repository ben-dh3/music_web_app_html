import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist_repository import *
from lib.artist import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()

    return render_template("albums.html", albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album_by_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)

    return render_template("find_album.html", album=album)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()

    return render_template("artists.html", artists=artists)

@app.route('/artists/<int:id>', methods=['GET'])
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)

    return render_template("find_artist.html", artist=artist)

@app.route('/albums/new')
def get_album_new():
    return render_template("new_album.html")

@app.route('/albums', methods=["POST"])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    title = request.form['title']
    release_year = int(request.form['release_year'])
    album = Album(None, title, release_year, 1)

    repository.create(album)
    return redirect(f"/albums/{album.id}")

@app.route('/artists/new')
def get_artist_new():
    return render_template("new_artist.html")

@app.route('/artists', methods=["POST"])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)

    repository.create(artist)
    return redirect(f"/artists/{artist.id}")

# @app.route('/albums', methods=['POST'])
# def post_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     title = request.form['title']
#     release_year = request.form['release_year']
#     artist_id = request.form['artist_id']
#     repository.create(Album(None, title, release_year, artist_id))

#     return ''

# @app.route('/artists', methods=['GET'])
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
#     return "\n".join(
#         f"{artist.name}" for artist in artists
#     )

# @app.route('/artists', methods=['POST'])
# def post_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     name = request.form['name']
#     genre = request.form['genre']
#     repository.create(Artist(None, name, genre))
#     return ''

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')

# # This imports some more example routes for you to see how they work
# # You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
