from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
from dotenv import load_dotenv
import tools.sql_queries as esecuele
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

@app.route("/sql/<name>", )
def lines_from_characters (name):
    return jsonify(esecuele.get_everything_from_character(name))

@app.route("/sentiment_all" )
def sentiment ():
    everything = esecuele.get_all_speech()
    return jsonify([sia.polarity_scores(i["speech"])["compound"] for i in everything])

@app.route("/sentiment/<location>" )
def sentimentcity ():
    everything = esecuele.city_sentiment()
    return jsonify([sia.polarity_scores(i["speech"])["compound"] for i in everything])

@app.route("/sentiment/random")
def get_sentiment_one_random():
    df = esecuele.get_random_sentence()
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()

    def sa(x):
        try:
            return sia.polarity_scores(x)
        except:
            return x

    df["sentiment_all"] = df["speech"].apply(sa)

    return jsonify(df.to_dict(orient='records'))

####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    scene = my_params["scene"]
    character_name = my_params["character_name"]
    dialogue = my_params["dialogue"]

    # Passing to my function: do the inserr
    esecuele.insert_one_row(scene, character_name, dialogue)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)
