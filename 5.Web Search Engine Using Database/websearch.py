from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, template_folder="./static")

@app.route("/")
def home():
    return render_template("websearch.html")

@app.route("/websearch", methods=["GET", "POST"])
def search():
    query = request.form.get("query", "")

    if query == "":
        return render_template("websearch.html")

    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT url, title FROM pages WHERE cleaned_content LIKE ? ORDER BY pagerank DESC",
        ("%" + query + "%",)
    )

    urls = cursor.fetchall()

    conn.close()

    return render_template("results.html", urls=urls, query=query)

if __name__ == "__main__":
    app.run(debug=True)
