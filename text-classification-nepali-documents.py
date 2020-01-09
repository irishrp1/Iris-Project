import dill
import nltk
import scipy as sp

from sklearn.datasets import load_mlcomp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB, BernoulliNB


MLCOMPDIR = r'16NepaliNews/16NepaliNews'

trainNews = load_mlcomp('NepaliData', 'train', mlcomp_root=MLCOMPDIR)
testNews = load_mlcomp('NepaliData', 'test', mlcomp_root=MLCOMPDIR)



stopWords = set(nltk.corpus.stopwords.words('nepali'))

''' Testing and Training Data '''
xTrain = trainNews.data
xTest = testNews.data
yTrain = trainNews.target
yTest = testNews.target


tfidfVectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(" "),
                                  sublinear_tf=True, encoding='utf-8',
                                  decode_error='ignore',
                                  stop_words=stopWords)

vectorised = tfidfVectorizer.fit_transform(xTrain)

with open('tfidf.pkl', 'wb') as f:
    dill.dump(tfidfVectorizer, f)

print('No of Samples , No. of Features ', vectorised.shape)
''' Classifier '''

clf1 = Pipeline([
    ('vect', tfidfVectorizer),
    ('clf', MultinomialNB(alpha=0.01, fit_prior=True))
])


# Bernoulli Naive Bayes Algorithm
clf3 = Pipeline([
    ('vect', tfidfVectorizer),
    ('clf', BernoulliNB(alpha=0.01))
])

def trainAndEvaluate(clf, xTrain, xTest, yTrain, yTest):
    model = clf.fit(xTrain, yTrain)
    with open('model.pkl', 'wb') as f:
        dill.dump(model, f)
    print("Accuracy on training Set : ")
    print(clf.score(xTrain, yTrain))
    print("Accuracy on Testing Set : ")
    print(clf.score(xTest, yTest))
    ''' --- START TEMPORARY ---'''
    print(str(xTest[0], encoding='utf-8'))
    print('Predicted Target ', clf.predict([xTest[0]])[0])
    print('Actual Target ', yTest[0])
    print('Predicted Target Name ', trainNews.target_names[clf.predict([xTest[0]])[0]])
    print('Actual Target Name ', trainNews.target_names[yTest[0]])

    print(str(xTest[600], encoding='utf-8'))
    print('Predicted Target ', clf.predict([xTest[600]])[0])
    print('Actual Target ', yTest[600])
    print('Predicted Target Name ', trainNews.target_names[clf.predict([xTest[600]])[0]])
    print('Actual Target Name ', trainNews.target_names[yTest[600]])

    print(str(xTest[1100], encoding='utf-8'))
    print('Predicted Target ', clf.predict([xTest[1100]])[0])
    print('Actual Target ', yTest[1100])
    print('Predicted Target Name ', trainNews.target_names[clf.predict([xTest[1100]])[0]])
    print('Actual Target Name ', trainNews.target_names[yTest[1100]])
    ''' --- END TEMPORARY ---'''
    print("Classification Report : ")
    print(metrics.classification_report(yTest, yPred))
    print("Confusion Matrix : ")
    print(metrics.confusion_matrix(yTest, yPred))


print(' Naive Bayes \n')
trainAndEvaluate(clf3, xTrain, xTest, yTrain, yTest)




def showTopFeatures(classifier, vectorizer, categories, number=25):
    featureNames = sp.asarray(vectorizer.get_feature_names())
    for i, category in enumerate(categories):
        topFeatures = sp.argsort(classifier.named_steps['clf'].coef_[i])[-number:]

        print('%s: %s' % (category, " ".join(featureNames[topFeatures])))



print('Bernoulli Naive Bayes \n')
showTopFeatures(clf3, tfidfVectorizer, trainNews.target_names)
