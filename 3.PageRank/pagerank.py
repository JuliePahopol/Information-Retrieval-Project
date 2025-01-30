import sqlite3
import networkx as nx
from bs4 import BeautifulSoup
import requests

# Function to crawl and store page content and links in the database
def crawl_and_store_pages(seed_urls, max_pages=100):
    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

    # Create the table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE,
        content TEXT,
        outgoing_links TEXT
    )
    """)
    conn.commit()

    visited_pages = set()
    url_frontier = seed_urls

    while url_frontier and len(visited_pages) < max_pages:
        url = url_frontier.pop(0)
        
        if url in visited_pages:
            continue

        print(f"Crawling {url}")
        response = requests.get(url)
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.get_text()
        links = [link.get("href") for link in soup.find_all("a") if link.get("href")]

        cursor.execute(
            "INSERT OR IGNORE INTO pages (url, content, outgoing_links) VALUES (?, ?, ?)",
            (url, content, ",".join(links))
        )
        conn.commit()

        for link in links:
            if "http" in link and link not in visited_pages:
                url_frontier.append(link)

        visited_pages.add(url)

    conn.close()
    print("Crawling complete.")

# Function to calculate PageRank using the crawled data
def calculate_pagerank():
    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

    cursor.execute("SELECT url, outgoing_links FROM pages")
    rows = cursor.fetchall()

    # Create a directed graph using NetworkX
    G = nx.DiGraph()

    for row in rows:
        url = row[0]
        outgoing_links = row[1].split(",") if row[1] else []
        for link in outgoing_links:
            if link:  # Only add non-empty links
                G.add_edge(url, link)

    # Calculate PageRank using NetworkX
    pagerank = nx.pagerank(G, weight=None)

    # Update the pages table with the calculated pagerank values
    for url, rank in pagerank.items():
        cursor.execute("UPDATE pages SET pagerank = ? WHERE url = ?", (rank, url))
    conn.commit()
    conn.close()

    print("PageRank calculation complete.")

# Example usage
seed_urls = ["https://www.bbc.co.uk/news", "https://www.cnn.com"]
crawl_and_store_pages(seed_urls, max_pages=50)
calculate_pagerank()
