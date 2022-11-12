USE project_4;


LOAD DATA LOCAL INFILE '/Users/hugosaccount/Desktop/IronHack/Project_4/trump_speech_df.csv'
	INTO TABLE trump_rally_speeches
		FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (location, dates, years, speech);
        
-- Error Code: 1146. Table 'project_4.trump_speeches' doesn't exist
-- Error Code: 2068. LOAD DATA LOCAL INFILE file request rejected due to restrictions on access.
-- Error Code: 2. File '/workspace/SQL_Test/src/trump_speech_df.csv' not found (OS errno 2 - No such file or directory)
