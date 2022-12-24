import pandas as pd
from flask import Flask, render_template, request, jsonify
from pandas import read_csv
from trol.hashtag import hashtag

from tweepy import tweet

from machinelearning import makineogren

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/searchpanel.html')


@app.route('/searchpanel', methods=['POST', 'GET'])
def mak_logic():
    keyword = request.form.get('keyword')
    sa = makineogren()
    predm, keyword1, follower, following, url, name, img = sa.DownloadData(keyword)
    return render_template('result.html', keyword=keyword1, pred=predm, follower=follower, following=following,
                           url=url,
                           name=name, img=img)


@app.route('/hashtag', methods=['POST', 'GET'])
def hashtagy():
    words = request.form.get('words')
    say = hashtag()
    df = pd.read_csv('data/sonsonuc.csv')

    result = df[["username", "text", "followers", "following", "troldurum"]]
    result2 = result.rename(columns={"username": "Kullanıcı Adı", "text": "Atılan Tweet", "followers": "Takipçi Sayısı",
                                     "following": "Takip Edilen Kİşi Sayısı", "troldurum": "Trol Durumu"})

    words = say.scrape(words)
    return render_template('hashtagresult.html', tables=[result2.to_html()],
                           titles=['İlgili Konu Hakkında Konuşan Hesaplar'])


if __name__ == '__main__':
    app.run(debug=True)
