from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams

sentence = "It is Day two in Malibu and Two more days to 60. I hope what I leanrend a lot in Malibu will help me in the future Day"
sentence = sentence.lower()
tokenizer = RegexpTokenizer(r"\w+")

tokens = tokenizer.tokenize(sentence)

unigrams = []

for i in tokens:
    if i not in stopwords.words('english'):
        unigrams.append(i)

unigrams_dict = {}
for i in unigrams:
    unigrams_dict[i] = 0
for i in unigrams:
    unigrams_dict[i] += 1

bigrams = ngrams(unigrams,2)

print(unigrams_dict)