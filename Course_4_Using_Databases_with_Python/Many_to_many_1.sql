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

-- Insert memberships
Insert INTO Member (user_id, course_id , role) VALUES (1, 1, 1);
Insert INTO Member (user_id, course_id , role) VALUES (2, 1, 0);
Insert INTO Member (user_id, course_id , role) VALUES (3, 1, 0);

Insert INTO Member (user_id, course_id , role) VALUES (1, 2, 0);
Insert INTO Member (user_id, course_id , role) VALUES (2, 2, 1);

Insert INTO Member (user_id, course_id , role) VALUES (2, 3, 1);
Insert INTO Member (user_id, course_id , role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
--Ed	1	PHP
--Sue	0	PHP
--Jane	1	Python
--Ed	0	Python
--Sue	0	Python
--Ed	1	SQL
--Jane	0	SQL






