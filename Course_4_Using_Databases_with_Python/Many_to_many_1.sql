create table User (
	id INTEGER Not null primary key autoincrement unique,
	name Text,
  email Text
)

create table User (
	id INTEGER, Not null primary key autoincrement unique,
	title Text,
)

create table Member (
	user_id INTEGER,
	course_id INTEGER,
		role INTEGER,
	PRIMARY key (user_id, course_id)
)
