direct to POSTGRESQL path C:\Program Files\PostgreSQL\14\bin> 

1.

psql -U postgres

2.

CREATE TABLE articles (
	id serial PRIMARY KEY NOT NULL,
	Author VARCHAR ( 900 ) NOT NULL,
	Title VARCHAR ( 255 ) NOT NULL,
	Year VARCHAR ( 255 ) NOT NULL,
	Journal VARCHAR ( 255 ) NOT NULL,
	H_Index VARCHAR ( 255 ) NOT NULL, 
	RefPerDoc VARCHAR ( 255 ) NOT NULL
);

3.

COPY articles FROM 'C:\datenbank_import\merged.csv' WITH CSV HEADER delimiter ';';


insert path where merged.csv is stored

4.
start webapp with:

python app.py