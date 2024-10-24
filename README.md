# SEO Automation Toolkit
This project contains five Python scripts designed to automate common SEO tasks, such as generating redirect maps, creating meta descriptions in bulk, analyzing keywords with N-grams, clustering keywords into topics, and matching keywords to predefined topics. This toolkit streamlines your SEO workflow, saves time, and improves efficiency.

# Project Overview
SEO tasks can be tedious, repetitive, and time-consuming. This project provides five Python scripts to automate key SEO activities, such as redirect maps, bulk meta description generation, keyword analysis, and keyword clustering. Each script is designed to handle large data sets efficiently by utilizing multi-core processors and Python libraries.

# Features
Automate Redirect Map: Automatically create redirect maps by comparing old and new URLs.
Bulk Meta Descriptions Generator: Generate meta descriptions for thousands of pages in bulk.
Keyword Analysis with N-Grams: Analyze keyword lists with unigrams, bigrams, and trigrams.
Group Keywords into Topic Clusters: Automatically group keywords into topic clusters.
Match Keywords to Predefined Topics: Match keywords to predefined topics for content categorization.

# Installation
Prerequisites
Python 3.7+ installed on your system.
Required Python packages listed in requirements.txt.

# Steps:
# Clone the repository:

git clone [repo_url]
cd SEO_Automation_Project

# Install dependencies:
pip install -r requirements.txt

# How to Use
You can run any of the scripts through main.py by specifying the desired task with the --task argument.

# Running a Task Example:
python main.py --task redirect

# Available Tasks:
# redirect: Automates the creation of a redirect map.
# meta: Bulk generates meta descriptions for URLs.
# ngrams: Analyzes keywords using N-Grams.
# clusters: Clusters keywords into topic groups.
# match: Matches keywords to predefined topics.

# Scripts Overview
# 1. Automate Redirect Map
# File: scripts/redirect_map.py

Automatically generates redirect maps by matching old and new URLs using content similarity.

# How to run:

python main.py --task redirect
# Input:

data/source_urls.txt
data/target_urls.txt
# Output:

results/redirect_map.csv
# 2. Bulk Meta Descriptions Generator
# File: scripts/bulk_meta_generator.py

Generates meta descriptions for multiple URLs in bulk using the Sumy LSA summarizer.

# How to run:

python main.py --task meta
# Input:

data/urls.txt
# Output:

results/meta_descriptions.csv
# 3. Keyword Analysis with N-Grams
# File: scripts/keyword_analysis_ngrams.py

Analyzes keywords and generates unigrams, bigrams, and trigrams to help identify common patterns in keyword strategies.

# How to run:

python main.py --task ngrams
# Input:

data/keywords.txt
# Output:

results/ngrams_results.txt

# 4. Group Keywords into Topic Clusters
# File: scripts/keyword_clustering.py

Groups keywords into topic clusters using TF-IDF and Affinity Propagation, helping organize keywords by topics for SEO.

# How to run:

python main.py --task clusters
Input:

data/keywords.txt
Output:

results/clusters.csv

# 5. Match Keywords to Predefined Topics
# File: scripts/match_keywords_to_topics.py

Matches a list of keywords to predefined topics using Spacy NLP, automating the categorization of keywords based on topic relevance.

# How to run:

python main.py --task match
# Input:

data/keywords.txt
data/topics.txt
# Output:

results/matched_keywords.csv

# Contributing
If you'd like to contribute to this project, feel free to submit a pull request or suggest improvements by opening an issue.

# Fork the repository.
# Create your feature branch:
git checkout -b feature/YourFeature
# Commit your changes:

git commit -m 'Add YourFeature'
# Push to the branch:
git push origin feature/YourFeature
Open a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
