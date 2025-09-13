-- "Album.title, Artist.name" is what we want to see on the new table  
-- "Album" and "Artist" are the tables that hold the data
-- "Album.artist_id = artist.id" is how the tables are linked
select Album.title, Artist.name from Album join Artist on Album.artist_id = artist.id
--Who Made Who	AC/DC
--IV	Led Zepelin

select Album.title, Album.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist.id
--Who Made Who	2	2	AC/DC
--IV	1	1	Led Zepelin


-- Track.title, Genre.name is what we want to see 
-- Track and Genre are the tables that hold the daa
-- Track.genre_id = Genre.id is how the tables are linked   
select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id
--Black Dog	Rock
--Stairway	Rock
--About to Rock	Metal
--Who made Who	Metal


-- Track.title, Artist.name, Album.title, Genre.name  what we want to see
-- Track, Genre, Album and Artist are the tables that hold the data
-- Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id is how the tables are linked
select Track.title, Artist.name, Album.title, Genre.name 
from Track join Genre join Album join Artist 
on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id
--Black Dog	Led Zepelin	IV	Rock
--Stairway	Led Zepelin	IV	Rock
--About to Rock	AC/DC	Who Made Who	Metal
--Who made Who	AC/DC	Who Made Who	Metal
