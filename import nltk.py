import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

with open('tell-tale-heart.txt', 'r') as file:
    text = file.read().lower() 

tokens = word_tokenize(text)


stop_words = set(stopwords.words('english'))
filtered_words = [w for w in tokens if w.isalnum() and w not in stop_words]

word_counts = Counter(filtered_words)

print("--- Top 10 Most Frequent Words ---")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")