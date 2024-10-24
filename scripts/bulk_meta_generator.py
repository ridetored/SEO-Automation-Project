from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import concurrent.futures
import csv
import requests

def generate_meta_description(url):
    try:
        parser = HtmlParser.from_url(url, Tokenizer("english"))
        summarizer = LsaSummarizer()
        description = summarizer(parser.document, 3)
        description = " ".join([sentence._text for sentence in description])
        if len(description) > 155:
            description = description[:152] + '...'
        return {'url': url, 'description': description}
    except:
        return {'url': url, 'description': 'Error fetching content'}

def bulk_generate_meta_descriptions():
    with open('data/urls.txt') as f:
        urls = [line.strip() for line in f]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(generate_meta_description, urls))

    with open('results/meta_descriptions.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'description'])
        writer.writeheader()
        writer.writerows(results)

    print("Bulk meta descriptions completed and saved to 'results/meta_descriptions.csv'")
