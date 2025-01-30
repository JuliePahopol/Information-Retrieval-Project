import sqlite3

def search(query):
    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT url, title FROM pages WHERE cleaned_content LIKE ? ORDER BY pagerank DESC",
        ("%" + query + "%",)
    )

    results = cursor.fetchall()

    conn.close()
    return results

if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = search(query)

    if results:
        for idx, (url, title) in enumerate(results, 1):
            print(f"{idx}. {title} - {url}")
    else:
        print("No results found.")
