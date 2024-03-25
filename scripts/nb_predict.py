#! /usr/bin/env python3

import os, sys
import sklearn.svm, sklearn.feature_extraction.text, sklearn.utils, sklearn.naive_bayes
from sklearn.metrics import matthews_corrcoef

def classify(train_x, train_y, eval_x):
    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(analyzer='char', ngram_range=(2, 6), min_df=2)
    cl = sklearn.naive_bayes.MultinomialNB()

    print("  Training")
    train_x_grams = vectorizer.fit_transform(train_x)
    cl.fit(train_x_grams, train_y)

    print("  Predicting")
    eval_x_grams = vectorizer.transform(eval_x)
    s = cl.predict(eval_x_grams)
    
    f = open(sys.argv[3], 'w')
    for line in s:
        f.write(line + "\n")
        
    f.close()

x, y = [], []
for line in open(sys.argv[1], 'r', encoding='utf-8'):
    x.append(line.split("\t")[1].strip())
    y.append(line.split("\t")[0].strip())

z = []
for line in open(sys.argv[2], 'r', encoding='utf-8'):
    z.append(line.strip())
    
classify(x, y, z)
