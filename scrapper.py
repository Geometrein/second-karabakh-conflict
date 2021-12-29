# -*- coding: utf-8 -*-

import requests
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def link_generator(start: int, end: int, page: int) -> str:
    """
    Generates links with appropriate query parameters.
    ---
    Args:
        start (int): start year of the query
        end (int): end year of the query
        page (int): page number

    Returns:
        link (str): final link for scrape requests
    """
    link = f"https://www.1000plus.am/hy/compensation?full_name=&status=all&date_from={start}-01-01&date_to={end}-01-01&page={page}"
    return link


def main():
    """
    Scrapes the search results and append to csv file.
    """
    for page in range(1,430):
        link = link_generator(2020, 2022, page)
        r = requests.get(link)
        html = r.content
        df = pd.DataFrame()
        df = pd.read_html(html, encoding='utf8')[0]
        df.to_csv('data.csv', mode='a', header=False)
        print(f"Page number: {page} scraped")


if __name__ == '__main__':
    main()