from bs4 import BeautifulSoup, SoupStrainer
from polyfuzz import PolyFuzz
import concurrent.futures
import csv
import pandas as pd
import requests

def read_urls(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]

def get_content(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            page_source = response.text
            strainer = SoupStrainer('p')
            soup = BeautifulSoup(page_source, 'lxml', parse_only=strainer)
            paragraph_list = [element.text for element in soup.find_all(strainer)]
            return " ".join(paragraph_list)
        else:
            return ""
    except requests.RequestException:
        return ""

def extract_content_in_parallel(urls, max_workers=None):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(get_content, urls))

def get_key_from_value(content_dictionary, value):
    return next((key for key, val in content_dictionary.items() if val == value), None)

def automate_redirect_map():
    source_urls = read_urls("data/source_urls.txt")
    target_urls = read_urls("data/target_urls.txt")
    
    content_list_a = extract_content_in_parallel(source_urls)
    content_list_b = extract_content_in_parallel(target_urls)

    content_dictionary = dict(zip(target_urls, content_list_b))

    model = PolyFuzz("TF-IDF")
    model.match(content_list_a, content_list_b)
    data = model.get_matches()

    result = [get_key_from_value(content_dictionary, to_val) for to_val in data["To"]]

    df = pd.DataFrame(list(zip(source_urls, result, data["Similarity"])))
    df.columns = ["From URL", "To URL", "% Identical"]
    df.to_csv("results/redirect_map.csv", index=False)

    print("Redirect map completed and saved to 'results/redirect_map.csv'")
