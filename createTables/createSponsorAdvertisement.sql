CREATE TABLE sponsorAdvertisement(
	advertisement_Id  INT NOT NULL auto_increment,
	sponsor_id INT NOT NULL,
	content_URL VARCHAR(255) NOT NULL,
	primary key(advertisement_Id)
)