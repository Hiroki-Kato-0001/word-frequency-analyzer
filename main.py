import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

#Read the text file
with open("data/sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

#Convert the text to lower cases and tokenize them
tokens = word_tokenize(text.lower())

#Eliminate stopwords, numbers, and symbols
words = [w for w in tokens if w.isalpha() and w not in stopwords.words("english")]

#Count frequency of the words
freq = Counter(words)

#Show top 10 most frequent words
print("Top 10 most frequent words:\n")
for word, count in freq.most_common(10):
    print(f"{word}: {count}")