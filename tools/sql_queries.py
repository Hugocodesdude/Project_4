from config.sql_connection import engine
import pandas as pd
import random

# Function to return all content
def get_everything ():
    query = """SELECT * FROM trump_rally_speeches;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# Function to return 
def get_everything_from_speech (name):
    query = f"""SELECT * 
    FROM trump_rally_speeches
    WHERE speech = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

#Return all speeches 
def get_all_speech():
    query = f"""SELECT speech 
    FROM trump_rally_speeches;"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

#City Sentiment on Location 
def city_sentiment(location):
    query = f"""SELECT speech 
    FROM trump_rally_speeches
    WHERE location = '{location}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

#Return Random Location 
def get_just_location (name):
    query = f"""SELECT dialogue 
    FROM trump_rally_speeches
    WHERE location = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

#POST
def insert_one_row (location, dates, years, speech):
        query = f"""INSERT INTO trump_rally_speeches
        (location, dates, years, speech) 
            VALUES ('{location}', '{dates}', '{years}','{speech}');
        """
        engine.execute(query)
        return f"Correctly introduced!"

#
def get_random_sentence():
    query = (f"""SELECT speech FROM trump_rally_speeches
    ORDER BY RAND()
    LIMIT 1;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient="records")