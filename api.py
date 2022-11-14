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

# Returns the sentiment score of all cities
@app.route("/sentiment_all" )
def sentiment ():
    everything = esecuele.get_all_speech()
    return jsonify([sia.polarity_scores(i["speech"])["compound"] for i in everything])

# Returns sentiment of given location
@app.route("/sentiment/<location>" )
def sentimentcity (location):
    everything = esecuele.city_sentiment(location)
    return jsonify([sia.polarity_scores(i["speech"])["compound"] for i in everything])

# Returns random Speech
@app.route("/random")
def get_sentiment_one_random_original():
    return jsonify(esecuele.get_random_sentence())


# Returns random phrase with sentiment 
@app.route("/random-sentiment")
def get_sentiment_one_random():
    '''sentiment del discurso aleatorio
    y frase aleatoria dentro del discurso (para saber de d'onde viene)'''
    random_sentence = esecuele.get_random_sentence()
    sent = sia.polarity_scores(random_sentence[0]['speech'])

    dict_ = {
        'pos': sent['pos'],
        'Speech': np.random.choice(random_sentence[0]['speech'].split('.'))
    }

    return jsonify(dict_)
    
#Random Speech with Sentiment 
@app.route("/random/sentiment")
def get_sentiment_one_random_speech():
    df = esecuele.get_random_sentence()
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    df["sentiment_all"] = df["speech"].apply(sa)
    print(df)

    try:
        df["sentiment_all"] = df["speech"].apply(sia.polarity_scores())
    except:
        pass
    print(df)
    return jsonify(df)
    
    #(df.to_dict(orient='records'))

####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    location = my_params["location"]
    dates = my_params["dates"]
    years = my_params["years"]
    speech = my_params["speech"]

    # Passing to my function: do the inserr
    esecuele.insert_one_row(location, dates, years, speech)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)
