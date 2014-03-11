# -*- coding: utf-8 -*-
from __future__ import division
import nltk, re, codecs
from nltk import Text
from nltk import FreqDist

def lemmas_distribution_rus(dist):
    dict_file = codecs.open('literature/processed_vocabulary',encoding='utf-8')
    dict_text = dict_file.readlines()
    dict_file.close()
    dict_dict = {}
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    from collections import defaultdict
    lemmas_dist = defaultdict(int)    
    for line in dict_text:
        line_list = line.split(':')
        dict_dict[line_list[0]] = line_list[1]
    for word in dist.keys():
        if word in dict_dict:
            lemmas_dist[dict_dict[word]] += 1
        else:
            p = morph.parse(word)
            if len(p) > 0:
                print word
                print p[0].normal_form
                lemmas_dist[p[0].normal_form] += 1
                print lemmas_dist[p[0].normal_form]
    lemmas_dist = FreqDist(lemmas_dist)
    lemmas_dist.plot(100)

def get_text(text):
    raw_text_file = codecs.open('raw_texts/'+text, encoding='utf-8')
    raw_text = raw_text_file.read()
    raw_text_file.close()
    print type(raw_text)
    tokens = nltk.word_tokenize(raw_text)
    return tokens

def create_dist(nltk_text, stopwords):
    dist = FreqDist(w.lower() for w in nltk_text if len(w)>=3 and w.isalnum() and w.lower() not in stopwords)
    dist.plot(50)
    print "Number of wordforms"+str(len(dist))
    return dist

def fourchan():
    print "Fourchan"
    f_text = get_text('4chan_text')
    print "text got, creating distribution"
    stopwords = nltk.corpus.stopwords.words('english')
    f_dist = create_dist(f_text, stopwords)

def iichan():
    print "Iichan"
    tokens = get_text('iichan_text')
    print "text got, creating distribution"
    stopwords = nltk.corpus.stopwords.words('english')+nltk.corpus.stopwords.words('russian')
    stopwords = map(unicode,(el.decode('utf-8') for el in stopwords))
    i_dist = create_dist(tokens, stopwords)
    lemmas_distribution_rus(i_dist)


def main():
    #fourchan()
    iichan()

main()


