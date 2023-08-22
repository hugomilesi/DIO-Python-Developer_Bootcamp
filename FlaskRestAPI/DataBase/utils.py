from model import Users, Playlists, PlaylistSongs, Songs, Albums, Artists, db_session
import datetime

def insert_data():

    user1 = Users(UserID=1,
                  FirstName='Hugo',
                  LastName='Milesi',
                  Email='hugogmilesi@gmail.com',
                  Address='ABC Street 123')

    user2 = Users(UserID=2,
                  FirstName='John',
                  LastName='Doe',
                  Email='jdow@gmail.com.com',
                  Address='XYZ Avenue 456')

    # Playlists
    playlist1 = Playlists(UserID=1)
    playlist2 = Playlists(UserID=2)

    # PlaylistSongs
    playlist_song_1 = PlaylistSongs(PlaylistSongID=1, SongID=1)
    playlist_song_2 = PlaylistSongs(PlaylistSongID=2, SongID=2)

    # Songs
    songs1 = Songs(AlbumID=1,
                   Title='All we needed',
                   Duration=4.06)

    songs2 = Songs(AlbumID=2,
                   Title='Count me out',
                   Duration=3.26)

    # Albums
    album1 = Albums(ArtistID=1,
                  Title='Higher Ground (part 1)',
                  ReleaseDate=datetime.datetime.strptime('2022-08-18', '%Y-%m-%d'))

    album2 = Albums(ArtistID=2,
                    Title='Mr. Morale & the Big Steppers',
                    ReleaseDate=datetime.datetime.strptime('2022-02-04', '%Y-%m-%d'))

    # Artists
    artist1 = Artists(Name='Koven',
                      Genre='EDM',
                      Country='England')

    artist2 = Artists(Name='Kendrick Lamar',
                      Genre='Rap',
                      Country='California')
    # add all insertions
    db_session.add_all([user1, user2,
                        playlist1, playlist2,
                        playlist_song_1, playlist_song_2,
                        songs1, songs2,
                        artist1, artist2])

    db_session.commit()
    db_session.close()

def delete():
    """Deleta usuários"""
    user = Users.query.filter_by(FirstName='John').first()
    db_session.delete(user)
    db_session.commit()


def alter_table():
    """Alterando o sobrenome do usuário"""
    user = Users.query.filter_by(FirstName='Hugo').first()
    user.LastName = 'Guilherme'
    db_session.add(user)
    db_session.commit()

def query():
    print("Informações dos usuários")
    users = Users.query.all()
    print(users)
    print('_' * 80)


def query_songs():
    """Recupera o nome de todas as musicas e exibe suas informações"""
    print('\nInformações sobre as músicas')
    songs = Songs.query.all()
    for song in songs:
        print(f'songID: {song.SongID}, AlbumID: {song.AlbumID}, Song Title: {song.Title}, Duration: {song.Duration}')
    print('_'*80)

def query_albums():
    """Recupera o nome de todos os albuns e exibe suas informações"""
    print('\nInformações sobre os albuns')
    albums = Albums.query.all()
    for album in albums:
        print(f"AlbumID: {album.AlbumID}, ArtistID: {album.ArtistID}, Title: {album.Title}, Release Date: {album.ReleaseDate}")
    print('_' * 80)

def query_artists():
    """Recupera o nome de todos os artistas e exibe suas informações"""
    print("\nInformações sobre os Artistas")
    artists = Artists.query.all()
    for artist in artists:
        print(f'ArtistID: {artist.ArtistID}, Name: {artist.Name}, Genre: {artist.Genre}, Country: {artist.Country}')
    print('_'*80)

if __name__ == '__main__':
    insert_data()
    query()
    #delete()
    #alter_table()
    #query_songs()
    #query_albums()
    #query_artists()
