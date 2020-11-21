#!/bin/bash
MYSQL_USER=root
MYSQL_HOST=localhost
MYSQL_PASSWORD=
MYSQL_DATABASE=pugsod

# setup database
mysql --local-infile=1 --show-warnings -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSWORD} << EOF
  -- SHOW FULL PROCESSLIST;

  -- create database if not exist, then use it.
  CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};
  USE ${MYSQL_DATABASE};

  -- set foreign key check = 0 (turn off).
  SET FOREIGN_KEY_CHECKS = 0;

  -- drop all tables if exists
  DROP TABLE IF EXISTS \
    user, client, customer, seller, \
    admin, sponsor, address, \
    ordert, orderItem, \
    product, pictureURL, productCategory, category,\
    promotion, payment, report, review, \
    sellerAdvertisement, sponsorAdvertisement, \
    shopContact;

  -- set foreign key check back to 1
  SET FOREIGN_KEY_CHECKS = 1;
EOF

# execute createTable script
for file in "./createTables"/*.sql
do
  if [[ -f $file ]]; then
    mysql --local-infile=1 --show-warnings -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} < ${file}
  fi 
done

# execute alter
for file in "./alter"/*.sql
do
  if [[ -f $file ]]; then
    mysql --local-infile=1 --show-warnings -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} < ${file}
  fi 
done

mysql --local-infile=1 --show-warnings -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSWORD} << EOF

SET GLOBAL local_infile=1;
SET FOREIGN_KEY_CHECKS = 0;

EOF

echo $PWD

# import csv files to tables
for file_csv in "${PWD}/data"/*.csv
do
  filename="$(basename ${file_csv} .csv)"
  echo $file_csv
  echo $filename
  if [[ -f $file_csv ]]; then
    mysql --silent --local-infile=1 --show-warnings -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE}<< EOF

      SET FOREIGN_KEY_CHECKS = 0;    
      LOAD DATA LOCAL INFILE "${file_csv}" 
      INTO TABLE ${filename} 
      FIELDS TERMINATED BY ',' 
      LINES TERMINATED BY "\n" 
      IGNORE 1 ROWS;
      SET FOREIGN_KEY_CHECKS = 1;    
EOF
  fi

done

mysql --local-infile=1 --show-warnings -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSWORD} << EOF

SET GLOBAL local_infile=0;
SET FOREIGN_KEY_CHECKS = 1;

EOF