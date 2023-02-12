import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import time

SCRAPER_API_KEY = "scraper api key"
ID = 'steven gives me the id!'
DOMAIN = 'steven gives me the domain!'

URL = f"https://www.amazon.{DOMAIN}/product-reviews/{ID}/ref=cm_cr_getr_d_paging_btm_next_3?"


def bs_parser(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_response(params):
    response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
    return response


time_before = time.time()
reviews = []
params = []
links = []
for i in range(1, 10):
    links.append(f"{URL}&pageNumber={i}")
    params.append({'api_key': SCRAPER_API_KEY, 'url': f"{URL}pageNumber={i}"})

with ThreadPoolExecutor(max_workers=1000) as p:
    results = p.map(get_response, params)

with ThreadPoolExecutor(max_workers=2000) as p:
    soups = p.map(bs_parser, results)


stars_and_reviews = {1: [],
                     2: [],
                     3: [],
                     4: [],
                     5: []}
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

time_now = time.time()

print(f"\n{counter}")
print(time_now-time_before)

