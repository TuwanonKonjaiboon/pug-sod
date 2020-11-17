CREATE TABLE user(
	user_id  int NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    pass varchar(255) NOT NULL,
	profile_pic_url varchar(512),
    primary key(user_id)
);