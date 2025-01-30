import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin
from stopwords_removal import remove_stopwords  # Assuming stopword removal script is available

# Function to initialize the SQLite database
def initialize_db():
    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

    # Create table for storing crawled pages and their content
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE,
        content TEXT,
        cleaned_content TEXT,
        title TEXT,
        outgoing_links TEXT,
        pagerank REAL
    )
    """)
    conn.commit()
    conn.close()

# Function to crawl and store page content, along with outgoing links
def crawl_and_store_pages(seed_urls, max_pages=100):
    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

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
        title = soup.find("title").string if soup.find("title") else "No Title"
        content = soup.get_text()  # Full text content
        cleaned_content = remove_stopwords(content)  # Clean the content
        outgoing_links = [link.get("href") for link in soup.find_all("a") if link.get("href")]

    
        cursor.execute(
            "INSERT OR REPLACE INTO pages (url, content, cleaned_content, title, outgoing_links) VALUES (?, ?, ?, ?, ?)",
            (url, content, cleaned_content, title, ",".join(outgoing_links))
        )
        conn.commit()

        # Add outgoing links (URLs) to the frontier for further crawling
        for link in outgoing_links:
            full_link = urljoin(url, link)  # Convert relative URLs to absolute
            if full_link not in visited_pages and "http" in full_link:
                url_frontier.append(full_link)

        visited_pages.add(url)

    conn.close()
    print("Crawling complete.")

# Example usage: seed URLs to start crawling
seed_urls = ["https://www.bbc.co.uk/news", "https://www.cnn.com"]
initialize_db()  # Initialize the SQLite database with the proper table
crawl_and_store_pages(seed_urls, max_pages=50)
