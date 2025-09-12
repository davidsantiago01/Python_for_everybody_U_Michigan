-- Creating a 4 table from scratch
CREATE TABLE "Album" ( "id" INTEGER NOT NULL UNIQUE, "artist_id" INTEGER, "title" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )
CREATE TABLE "Artist" ( "id" INTEGER NOT NULL, "name" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )
CREATE TABLE "Genre" ( "id" INTEGER NOT NULL UNIQUE, "name" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )
CREATE TABLE "Track" ( "id" INTEGER NOT NULL UNIQUE, "title" TEXT, "album_id" INTEGER, "genre_id" INTEGER, "len" INTEGER, "ratio" INTEGER, "count" INTEGER, PRIMARY KEY("id" AUTOINCREMENT) )

-- Inserting Artists
Insert into Artist (name) values ("Led Zepelin");
Insert into Artist (name) values ("AC/DC")

--Inserting Genrse
Insert into Genre (name) values ("Rock");
Insert into Genre (name) values ("Metal")

-- Inserting Album
Insert into Album (title, artist_id) values ("Who made who", 2);
Insert into Album (title, artist_id) values ("IV", 1)

-- Inserting Track
Insert into Track (title, rating, len, count, album_id, genre_id) values ("Black Dog", 5, 297, 0, 2, 1);
Insert into Track (title, rating, len, count, album_id, genre_id) values ("Stairway", 5, 482, 0, 2, 1)
Insert into Track (title, rating, len, count, album_id, genre_id) values ("About to Rock", 5, 313, 0, 1, 2)
Insert into Track (title, rating, len, count, album_id, genre_id) values ("Who made Who", 5, 207, 0, 1, 2)
