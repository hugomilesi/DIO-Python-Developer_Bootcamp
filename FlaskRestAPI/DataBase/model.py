from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base


# Criando a sessão
engine = create_engine("sqlite:///MusicStreaming.db")
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Users(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(40), index=True)
    LastName = Column(String(40))
    Email = Column(String(40))
    Address = Column(String(100))

    def __repr__(self):
        return f"Users(UserID={self.UserID}, FirstName='{self.FirstName}', LastName='{self.LastName}', Email='{self.Email}', Address='{self.Address}')"



class Playlists(Base):
    __tablename__ = 'Playlists'
    PlaylistID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"))

    user = relationship("Users")

    def __repr__(self):
        return f"Playlists(PlaylistID={self.PlaylistID}, UserID={self.UserID})"


class PlaylistSongs(Base):
    __tablename__ = 'PlaylistSongs'
    PlaylistSongID = Column(Integer, primary_key=True)
    PlaylistID = Column(Integer, ForeignKey('Playlists.PlaylistID'))
    SongID = Column(Integer, ForeignKey("Songs.SongID"))

    song = relationship("Songs")

    def __repr__(self):
        return f"PlaylistSongs(PlaylistSongID={self.PlaylistSongID}, PlaylistID={self.PlaylistID}, SongID={self.SongID})"


class Songs(Base):
    __tablename__ = 'Songs'
    SongID = Column(Integer, primary_key=True)
    AlbumID = Column(Integer, ForeignKey('Albums.AlbumID'))
    Title = Column(String(40))
    Duration = Column(Float)

    album = relationship("Albums")

    def __repr__(self):
        return f"Songs(SongID={self.SongID}, AlbumID={self.AlbumID}, Title = '{self.Title}', Duration={self.Duration})"


class Albums(Base):
    __tablename__ = 'Albums'
    AlbumID = Column(Integer, primary_key=True)
    ArtistID = Column(Integer, ForeignKey('Artists.ArtistID'))
    Title = Column(String(40))
    ReleaseDate = Column(DateTime)

    artist = relationship("Artists")

    def __repr__(self):
        return f"Albums(AlbumID={self.AlbumID}, ArtistID={self.ArtistID}, Title='{self.Title}', ReleaseDate={self.ReleaseDate})"


class Artists(Base):
    __tablename__ = 'Artists'
    ArtistID = Column(Integer, primary_key=True)
    Name = Column(String(40))
    Genre = Column(String(20))
    Country = Column(String(40))

    def __repr__(self):
        return f"Artists(ArtistID={self.ArtistID}, Name='{self.Name}', Genre='{self.Genre}', Country='{self.Country}')"


def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()