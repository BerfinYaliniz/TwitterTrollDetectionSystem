from flask import Flask, render_template, request
from machinelearning import makineogren

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('searchpanel.html')


@app.route('/searchpanel', methods=['POST', 'GET'])
def mak_logic():
    keyword = request.form.get('keyword')
    sa = makineogren()
    keyword1 = sa.DownloadData(keyword)
    return render_template('result.html', keyword=keyword1)


if __name__ == '__main__':
    app.run()
