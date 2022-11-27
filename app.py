from flask import Flask, render_template, request
from tweepy import tweet

from machinelearning import makineogren

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('searchpanel.html')


@app.route('/searchpanel', methods=['POST', 'GET'])
def mak_logic():
    keyword = request.form.get('keyword')
    sa = makineogren()
    pred, keyword1, follower, following, url, name, img, bg_image = sa.DownloadData(keyword)
    return render_template('result.html', keyword=keyword1, pred=pred, follower=follower, following=following,
                           url=url,
                           name=name, img=img, bg_image=bg_image)


@app.errorhandler(500)
def page_not_found(e):
    return render_template("searchpanel.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template("searchpanel.html")


if __name__ == '__main__':
    app.run()
