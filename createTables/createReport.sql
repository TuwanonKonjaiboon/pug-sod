CREATE TABLE report(
report_id int not null auto_increment,
user_id int not null,
report_title VARCHAR(30) not null,
description TEXT(300) not null,
primary key(report_id)
);