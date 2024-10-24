import argparse
from scripts.redirect_map import automate_redirect_map
from scripts.bulk_meta_generator import bulk_generate_meta_descriptions
from scripts.keyword_analysis_ngrams import keyword_analysis_ngrams
from scripts.keyword_clustering import group_keywords_into_clusters
from scripts.match_keywords_to_topics import match_keywords_to_topics

def main():
    parser = argparse.ArgumentParser(description="SEO Automation Toolkit")
    parser.add_argument("--task", required=True, choices=["redirect", "meta", "ngrams", "clusters", "match"],
                        help="Choose the SEO task to automate: redirect, meta, ngrams, clusters, match")

    args = parser.parse_args()

    if args.task == "redirect":
        automate_redirect_map()
    elif args.task == "meta":
        bulk_generate_meta_descriptions()
    elif args.task == "ngrams":
        keyword_analysis_ngrams()
    elif args.task == "clusters":
        group_keywords_into_clusters()
    elif args.task == "match":
        match_keywords_to_topics()
    else:
        print("Invalid task. Choose one from: redirect, meta, ngrams, clusters, match")

if __name__ == "__main__":
    main()
