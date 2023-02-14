from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup
from server.parser.cohere_handler import run_cohere


def bs_parser(params):
    webpage = requests.get(params['url'], headers=params['header'])
    return BeautifulSoup(webpage.text, 'html.parser')


def scrape(domain, asin):

    print("scrape start")

    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    url = f"https://www.amazon.{domain}/product-reviews/{asin}/ref=cm_cr_getr_d_paging_btm_next_3?"
    
    params = []

    for i in range(1, 20):
        params.append({'url': f"{url}pageNumber={i}", 'header': HEADERS})

    with ThreadPoolExecutor(max_workers=100) as p:
        soups = p.map(bs_parser, params)

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
