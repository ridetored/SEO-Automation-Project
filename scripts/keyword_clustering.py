import csv
import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer

def group_keywords_into_clusters():
    with open("data/keywords.txt", "r") as f:
        keywords = f.read().splitlines()

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(keywords)

    af = AffinityPropagation().fit(X)
    labels = af.labels_

    with open("results/clusters.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Cluster", "Keyword"])
        for i in range(len(np.unique(labels))):
            for j, label in enumerate(labels):
                if label == i:
                    writer.writerow([i, keywords[j]])

    print("Keyword clustering completed and saved to 'results/clusters.csv'")
