import csv
from flask import Flask, jsonify, request

all_articles = []
liked_articles = []
disliked_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route('/get-articles')
def get_articles():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route('/like-articles')
def like_articles():
    all_articles = data[1:]
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'status':'success'
    }), 201

@app.route('/dislike-articles')
def dislike_articles():
    all_articles = data[1:]
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        'status':'success'
    }), 201

if __name__ == '__main__':
    app.run()

