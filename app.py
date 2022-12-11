from flask import Flask, render_template, request
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
    predm, keyword1, follower, following, url, name, img, bg_image = sa.DownloadData(keyword)
    return render_template('result.html', keyword=keyword1, pred=predm, follower=follower, following=following,
                           url=url,
                           name=name, img=img, bg_image=bg_image)


@app.route('/hashtag', methods=['POST', 'GET'])
def hashtagy():
    words = request.form.get('words')
    say = hashtag()
    predm, words, follower, following, url, name, img, bg_image = say.scrape(words)
    return render_template('hashtagresult.html', words=words, predm=predm, follower=follower, following=following,
                           url=url, name=name, img=img, bg_image=bg_image)




if __name__ == '__main__':
    app.run()
