import nltk
from nltk import FreqDist
from nltk.text import Text
import matplotlib.pyplot as plt


filename = "tell-tale-heart.txt"

with open(filename, "r", encoding="utf-8") as f:
    raw = f.read()

tokens = nltk.word_tokenize(raw)
text = Text(tokens)

print("Sample from the text:")
print(raw[:200], "...")   


def lexical_diversity(tokens):
    return len(set(tokens)) / len(tokens)

lex = lexical_diversity(tokens)
print(f"\nLexical diversity of {filename}: {lex:.3f}")


from nltk.book import text1   
lex2 = lexical_diversity(text1)
print(f"Lexical diversity of NLTK text1 (Moby Dick): {lex2:.3f}")


fdist = FreqDist(tokens)
print("\nMost common words in the story:")
for word, freq in fdist.most_common(15):
    print(f"{word}: {freq}")


print("\nWords similar to 'mad' (distributional similarity):")
text.similar("mad")


words_of_interest = ["mad", "eye", "heart", "night", "old"]

plt.figure(figsize=(8,4))
counts = [fdist[w] for w in words_of_interest]
plt.bar(words_of_interest, counts)
plt.title("Frequency of Selected Words in 'The Tell-Tale Heart'")
plt.xlabel("Word")
plt.ylabel("Count")
plt.show()


fdist.plot(30, cumulative=False)