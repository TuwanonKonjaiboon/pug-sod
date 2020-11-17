CREATE TABLE report(
report_id int not null,
report_title VARCHAR(30) not null,
report_description TEXT(300) not null,
user_id int not null,
primary key(report_id)
);