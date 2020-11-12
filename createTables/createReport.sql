CREATE TABLE report(
report_id CHAR(20) not null,
report_title VARCHAR(30) not null,
report_description TEXT(300) not null,
user_id char(20) not null,
primary key(report_id),
foreign key(user_id) references user(user_id)
on delete cascade
);