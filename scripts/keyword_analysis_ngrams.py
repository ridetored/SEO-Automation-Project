import re
from collections import Counter
import concurrent.futures

def clean_word(word):
    return re.sub(r'[^a-zA-Z]', '', word)

def count_ngrams(words):
    unigrams, bigrams, trigrams = Counter(), Counter(), Counter()
    for i in range(len(words)):
        unigrams[words[i]] += 1
        if i < len(words) - 1:
            bigram = f"{words[i]} {words[i + 1]}"
            bigrams[bigram] += 1
        if i < len(words) - 2:
            trigram = f"{words[i]} {words[i + 1]} {words[i + 2]}"
            trigrams[trigram] += 1
    return unigrams, bigrams, trigrams

def keyword_analysis_ngrams():
    with open('data/keywords.txt') as f:
        words = [clean_word(word) for word in f.read().split()]

    unigrams, bigrams, trigrams = count_ngrams(words)

    with open('results/ngrams_results.txt', 'w') as f:
        f.write("Most common unigrams:\n")
        for unigram, count in unigrams.most_common(10):
            f.write(f"{unigram}: {count}\n")
        f.write("\nMost common bigrams:\n")
        for bigram, count in bigrams.most_common(10):
            f.write(f"{bigram}: {count}\n")
        f.write("\nMost common trigrams:\n")
        for trigram, count in trigrams.most_common(10):
            f.write(f"{trigram}: {count}\n")

    print("N-grams analysis completed and saved to 'results/ngrams_results.txt'")
