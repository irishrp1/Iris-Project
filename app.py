
from flask import Flask
from flask import render_template
from flask import request
import dill
from unicode import convertunicode

from sklearn.datasets import load_mlcomp


MLCOMPDIR = r'16NepaliNews/16NepaliNews'

trainNews = load_mlcomp('16NepaliNews', 'train', mlcomp_root=MLCOMPDIR)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        result = request.form
        newsText = result.get('inputText')
        newsText = [newsText]
        tfidf = dill.load(open("tfidf.pkl", 'rb'))
        tfidf.fit_transform(newsText)
        model = dill.load(open("model.pkl", 'rb'))
        predictedClass = model.predict(newsText)[0]
        result = trainNews.target_names[predictedClass]
        result = convertunicode(result)
        print (result)

    return render_template('index.html', predictedClass= result)


if __name__ == "__main__":
    app.run(debug=True)
