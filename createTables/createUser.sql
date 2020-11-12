CREATE TABLE user(
	user_id  char(20) NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    pass varchar(255) NOT NULL,
	sex char(1),
    birth_date date,
    age int,
    primary key(user_id)
);