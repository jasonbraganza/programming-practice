"""
The idea, is for me to crawl the poetry foundation’s, poem of the day page at
https://www.poetryfoundation.org/poems/poem-of-the-day and put it into an rss
file for me, so that i can read it in my RSS reader
"""

from datetime import date, datetime

import requests
from bs4 import BeautifulSoup
import PyRSS2Gen


def main():
    poempage = "https://www.poetryfoundation.org/poems/poem-of-the-day"
    reply = get_page_from_pf(poempage)
    if reply == poempage:
        create_rss_feed(poempage)


def get_page_from_pf(link):
    rawhtml = requests.get(link)
    soup = BeautifulSoup(rawhtml.text, "html.parser")

    date_of_poem_str = soup.find("meta", {"name": "dcterms.Date"}).get("content")

    date_of_poem = datetime.strptime(date_of_poem_str, "%Y-%m-%d")
    date_of_poem = date_of_poem.date()
    today_date = date.today()

    if date_of_poem == today_date:
        return link
    else:
        return "No new poem yet!"


def create_rss_feed(poemlink):
    rss = PyRSS2Gen.RSS2(
        title="Jason's PF feed",
        link=poemlink,
        description="Poem of the day",
        lastBuildDate=datetime.now(),
        items=[
            PyRSS2Gen.RSSItem(
                title=f"Poem for {date.today()}",
                link=poemlink,
                guid=PyRSS2Gen.Guid(f"Poem for {date.today()}"),
                pubDate=datetime.now(),
            ),
        ],
    )

    rss.write_xml(open("poem.xml", "w"))


#   create and write_to_rss_feed
if __name__ == "__main__":
    main()
