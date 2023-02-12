from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup
from server.env import SCRAPER_API_KEY
from server.parser.cohere_handler import run_cohere


def bs_parser(response):

    return BeautifulSoup(response.text, "html.parser")


def get_response(params):

    return requests.get("https://api.scraperapi.com/", params=urlencode(params))


def scrape(domain, asin):

    print("scrape start")

    url = f"https://www.amazon.{domain}/product-reviews/{asin}/ref=cm_cr_getr_d_paging_btm_next_3?"
    
    params = []
    links = []

    for i in range(1, 10):
        links.append(f"{url}&pageNumber={i}")
        params.append({"api_key": SCRAPER_API_KEY, "url": f"{url}pageNumber={i}"})

    with ThreadPoolExecutor(max_workers=1000) as p:
        results = p.map(get_response, params)

    with ThreadPoolExecutor(max_workers=2000) as p:
        soups = p.map(bs_parser, results)

    stars_and_reviews = {1: [], 2: [], 3: [], 4: [], 5: []}
    counter = 0

    for soup in soups:
        review_sections = []

        for item in soup.find_all("div", {"class": "a-section celwidget"}):
            review_sections.append(item)

        for review in review_sections:
            review_stars = review.find("span", {"class": "a-icon-alt"}).get_text()
            star_rating = int(review_stars[0])
            review_body = review.find("span", {"data-hook": "review-body"}).get_text().strip("\n")
            stars_and_reviews[star_rating].append(review_body)
            counter += 1

    print("scrape end")

    return run_cohere(stars_and_reviews)
