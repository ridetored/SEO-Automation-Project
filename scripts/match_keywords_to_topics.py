import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import concurrent.futures

nlp = spacy.load("en_core_web_sm")

def categorize_keyword(keyword, topics_df):
    tokens = nlp(keyword.lower())
    tokens = [token.text for token in tokens if not token.is_stop and not token.is_punct]
    best_topic = "Other"
    max_overlap = 0
    for topic in topics_df["topic"]:
        topic_tokens = nlp(topic.lower())
        overlap = len(set(tokens).intersection(set([t.text for t in topic_tokens])))
        if overlap > max_overlap:
            max_overlap = overlap
            best_topic = topic
    return {"keyword": keyword, "category": best_topic}

def match_keywords_to_topics():
    keywords_df = pd.read_csv("data/keywords.txt", header=None, names=["keyword"])
    topics_df = pd.read_csv("data/topics.txt", header=None, names=["topic"])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(categorize_keyword, keywords_df["keyword"], [topics_df] * len(keywords_df)))

    results_df = pd.DataFrame(results)
    results_df.to_csv("results/matched_keywords.csv", index=False)

    print("Keyword matching completed and saved to 'results/matched_keywords.csv'")
