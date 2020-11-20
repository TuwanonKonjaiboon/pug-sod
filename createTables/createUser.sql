CREATE TABLE user(
	user_id  int NOT NULL auto_increment,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    password varchar(20) NOT NULL,
	profile_pic_URL varchar(255),
    primary key(user_id)
);