create table User (
	id INTEGER Not null primary key autoincrement unique,
	name Text,
  email Text
)

create table Course (
	id INTEGER, Not null primary key autoincrement unique,
	title Text,
)

create table Member (
	user_id INTEGER,
	course_id INTEGER,
		role INTEGER,
	PRIMARY key (user_id, course_id)
)

-- insert courses and values

INSERT INTO User (name, email) VALUES ("Jane", "jane@tsugi.org");
INSERT INTO User (name, email) VALUES ("Ed", "ed@tsugi.org");
INSERT INTO User (name, email) VALUES ("Sue", "Sue@tsugi.org");

INSERT INTO Course (title) VALUES ("Python");
INSERT INTO Course (title) VALUES ("SQL");
INSERT INTO Course (title) VALUES ("PHP");


