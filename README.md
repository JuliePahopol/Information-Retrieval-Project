# Descipline: Information Retrieval Report
### Student: Iulia Pahopol

# Web Search Using Database
The Web Search Using Database folder contains a fully functional web search engine implementation that integrates a web crawler, PageRank computation, and a user-facing search interface. The system uses a database to store crawled pages and their metadata, enabling efficient query handling. Below is a detailed description of each file and its purpose.
The structure of our project looks like this:
┣ 1.Information Retrieval/ 
┃ ┗ stopwords_removal.py 
┣ 2.Web Spidering/
┃ ┣ crawled_pages.db 
┃ ┗ web_spider.py
┣ 3.PageRank/
┃ ┣ pagerank.py
┣ 5.Web Search Engine Using Database/
┃ ┣ static/
┃ ┗ crawled_pages.db
┃ ┗ pagerank.py
┃ ┗ web_spider.py
┃ ┗ websearch.py



# Files and their usage:
## 1.Information Retrieval
### stopwords_removal.py
Purpose of Stopwords Removal
The purpose of the stopwords removal module in this project is to enhance the efficiency and relevance of the Information Retrieval system by eliminating common words (known as stopwords) that do not contribute significant meaning to the search or retrieval process. Examples of stopwords include "is," "the," "of," and "an." Removing these words reduces noise in the data and focuses the analysis on meaningful terms.
This module is essential for achieving:
1.	Data Cleaning: It removes unnecessary terms that do not add value to search queries or document indexing.
2.	Improved Retrieval Accuracy: By filtering out non-informative words, the system focuses on more relevant terms, improving the quality of search results.
3.	Reduced Index Size: Eliminating stopwords decreases the size of the inverted index and other data structures, making the retrieval system more efficient.
4.	Efficiency in Query Processing: Reducing the number of terms processed speeds up search operations.
How It Works
•	Stopwords Identification: The module uses a predefined set of English stopwords from the Natural Language Toolkit (NLTK).
•	Tokenization: The input text is tokenized into individual words using NLTK's word_tokenize method.
•	Filtering: Each word is checked against the stopwords set. Words not present in the stopwords list are retained.
•	Reconstruction: The filtered words are combined back into a cleaned text string.



## 2.Web Spidering 
### web_spider.py
Purpose of Web Spider
The purpose of the web_spider.py module in this project is to automate the process of crawling and extracting data from web pages. This is an essential component of the Information Retrieval and Search Engine system, as it gathers the raw data required for indexing and further processing. The web spider systematically navigates through web pages, collects their content, and stores it in a database for later use.
This module is crucial for:
1.	Data Collection: It retrieves web content, which serves as the foundation for indexing, ranking, and searching.
2.	Scalability: By automating the crawling process, it allows the system to handle large-scale web data efficiently.
3.	Content Storage: The spider stores the crawled pages' URLs and content in a SQLite database, ensuring the data is organized and accessible for subsequent modules like PageRank and InvertedIndex.
4.	Extensibility: The modular design enables easy adaptation to additional functionality, such as filtering specific domains or extracting only relevant portions of web pages.
How It Works
1.	Initialization:
o	The SQLite database (crawled_pages.db) is created (or connected to), and a table named pages is set up to store page URLs and their content.
2.	URL Frontier:
o	A queue-like structure (url_frontier) is initialized with a seed URL.
o	Crawling continues until the queue is empty or the maximum page limit (max_pages) is reached.
3.	Crawling and Parsing:
o	Each URL is fetched using the requests library.
o	The page's HTML content is parsed using BeautifulSoup, and the data is stored in the database.
4.	Link Extraction:
o	All hyperlinks (<a> tags) are extracted from the page.
o	Valid, unvisited links are added to the url_frontier, ensuring that the crawler explores new pages.
5.	Storage and Deduplication:
o	URLs and content are stored in the database with INSERT OR IGNORE to prevent duplicate entries.
6.	Completion:
o	The process ends when all pages are visited or the maximum page limit is reached, and the database connection is closed.
Example Usage
In the provided example:
•	The spider starts crawling from the seed URL (https://www.bbc.co.uk/news/topics/c4y26wwj72zt).
•	It retrieves up to 50 pages, storing their URLs and content in the SQLite database for further analysis.
Benefits to the Project
The web_spider.py module is a foundational component of the system. It gathers raw data for other components, such as PageRank (for ranking pages), InvertedIndex (for indexing terms), and the search engine application (for serving user queries). Its ability to collect, parse, and store web data ensures the project has a robust and scalable data pipeline.






## 3.PageRank
### pagerank.py
Purpose of PageRank
The purpose of the pagerank.py module in this project is to rank web pages based on their importance and connectivity using the PageRank algorithm. PageRank evaluates the significance of a web page by considering both the quantity and quality of links pointing to it. This algorithm is a key component for ranking pages in search engines, ensuring that more authoritative and relevant pages appear higher in search results.
This module contributes to the project by:
1.	Calculating Page Importance: It assigns a numerical score (PageRank score) to each page, reflecting its importance in the web graph.
2.	Improving Search Results: Higher-ranked pages can be prioritized in search engine results, enhancing the relevance of retrieved documents.
3.	Simulating Web Graphs: The module models the structure of the web using a directed graph, where nodes represent web pages, and edges represent hyperlinks between them.
4.	Supporting Scalability: By leveraging a graph-based algorithm, the module can handle large-scale web crawled data.
How It Works
1.	Link Extraction:
o	For each URL in the urls list, the module fetches the web page using the requests library.
o	BeautifulSoup is used to parse the HTML and extract all hyperlinks (<a> tags).
o	Outgoing links for each page are stored in a dictionary (outgoing_links).
2.	Graph Construction:
o	A directed graph (nx.DiGraph) is created using the NetworkX library.
o	Nodes represent web pages, and directed edges represent links between pages.
3.	PageRank Calculation:
o	The nx.pagerank function computes the PageRank score for each node in the graph.
o	The scores are weighted by the number and importance of incoming links to ensure fair distribution.
4.	Ranking Results:
o	The computed PageRank scores are sorted in descending order, producing a 
o	ranked list of pages based on their importance.


## 5.Web Search Using Database
The Web Search Engine Using Database project consists of components that work together to provide a functional search engine. The results.html and websearch.html files are templates used to display the user interface and query results, while the css folder contains stylesheets that define the visual design of the web pages.

### style.css 
The css folder contains stylesheets (e.g., style.css) that define the visual appearance of the search engine pages.
•	Examples of Styling:
o	Input fields, buttons, and layout spacing.
o	A clean and modern interface for better user experience.
o	Ensures consistency in the design of websearch.html and results.html.
pagerank.py
The pagerank.py script is responsible for calculating PageRank scores for websites stored in the SQLite database (crawled_pages.db). PageRank is an algorithm used to rank web pages based on the number and quality of links pointing to them.
________________________________________
### Steps and Explanation
1.	Import Required Libraries
o	sqlite3: Used to connect to and interact with the SQLite database (crawled_pages.db) where crawled web pages are stored.
o	networkx: A Python library used to create and analyze graphs, such as the directed graph required for PageRank calculation.
2.	Connect to the SQLite Database
conn = sqlite3.connect("crawled_pages.db")
cursor = conn.cursor()
o	Establishes a connection to the database crawled_pages.db.
o	Creates a cursor object to execute SQL queries.

3.	Retrieve URLs from the Database

cursor.execute("SELECT url FROM pages")
urls = [row[0] for row in cursor.fetchall()]
Queries the pages table to fetch all stored URLs.
Stores the URLs in a list for further processing.

4.	Create a Directed Graph

graph = nx.DiGraph()
for url in urls:
    graph.add_node(url)

  Initializes an empty directed graph using NetworkX (DiGraph).
 Adds each URL as a node in the graph.

5.	Add Edges (Outgoing Links) to the Graph
for url in urls:
    cursor.execute("SELECT outgoing_links FROM pages WHERE url = ?", (url,))
    outgoing_links = cursor.fetchone()[0].split(",")
    for link in outgoing_links:
        if link.startswith("http"):
            graph.add_edge(url, link)

For each URL (node):
•	Retrieves its outgoing links (hyperlinks to other pages).
•	Splits the links into a list and adds a directed edge from the current URL to each outgoing link.

6.	Calculate PageRank

pagerank = nx.pagerank(graph)
Uses the pagerank() function from NetworkX to calculate the PageRank scores of all nodes in the graph.
Each node (URL) is assigned a score based on the number and quality of incoming links.

7.	Store PageRank Scores in the Database

for url in urls:
cursor.execute("UPDATE pages SET pagerank = ? WHERE url = ?", (pagerank[url], url))
Updates the pages table by storing the PageRank score of each URL in the pagerank column.
Ensures that PageRank data is available for search engine queries.

8.	Commit Changes and Close the Connection
conn.commit()
conn.close()
•	Saves all changes to the database.
•	Closes the connection to free up resources.

Purpose of the Script
•	To compute the PageRank scores of web pages stored in the database.
•	To update the database (crawled_pages.db) with the calculated scores, enabling the search engine to rank and display results based on PageRank.
web_spider.py
The web_spider.py script is designed to crawl web pages starting from a given URL, gather relevant information, and store it in a SQLite database (crawled_pages.db). This script is used to retrieve and store web content such as page titles, outgoing links, and the content of the page for further processing, such as indexing or ranking.
How the Script Works
•	Step 1: Create the Database
The script first connects to an SQLite database (crawled_pages.db) and creates a pages table if it doesn't already exist. The table structure includes:
o	id: Unique identifier for each page (auto-incremented).
o	url: URL of the crawled page.
o	content: Raw HTML content of the page.
o	cleaned_content: Plain text content of the page (no HTML tags).
o	title: Title of the web page (extracted from the <title> tag).
o	outgoing_links: Comma-separated list of links found on the page.
•	Step 2: Start Crawling
The crawler starts with the seed URLs and iterates over them using a breadth-first search approach (FIFO). It fetches each URL, checks if it's already been visited, and retrieves the page content.
•	Step 3: Extract Content
The crawler extracts the following:
o	Page Title: Retrieved from the <title> tag.
o	Outgoing Links: Extracts all the links from the page (<a> tags).
o	Content: Retrieves the raw HTML content of the page and also extracts the plain text (removing HTML tags).
•	Step 4: Store Data
The extracted data is stored in the pages table of the SQLite database, using the INSERT OR REPLACE SQL command to avoid inserting duplicate entries.
•	Step 5: Continue Crawling
The crawler continues following the links found on each page and repeats the process for each new page. It stops when either:
o	It reaches the maximum number of pages to crawl (default is 100).
o	There are no more unvisited pages in the list of links to crawl.
•	Step 6: End Crawling
Once the crawling process is complete, the script closes the database connection and prints Crawling complete.
5. Output
•	After the crawling is completed, the results are stored in the crawled_pages.db database. This includes the URLs, titles, content, and outgoing links.
•	You can use this database to retrieve and process the crawled data further (e.g., indexing, ranking).
•	 
 

### Websearch.py
The websearch.py script is part of a simple web search engine built using Flask. It allows users to input a search query, then queries an SQLite database (crawled_pages.db) containing crawled web pages, and returns relevant results based on the query. It then displays the results in a user-friendly HTML page.

#### How to Use websearch.py
1. Preparation
Before running the websearch.py script, make sure the following are installed:
•	Python
•	Flask library
•	SQLite database (crawled_pages.db should exist with crawled data)
You can install Flask with the following command:
pip install flask

2. Running the Script
To start the Flask application, open a terminal and run the script by using the following command:
python websearch.py
This will start a development server and the web application will be available locally, usually at http://127.0.0.1:5000/.
3. Functionality and Parameters
The script is designed to do the following:
•	Allow the user to input a search query on the home page (websearch.html).
•	On submission, the query is processed, and the Flask app searches the database for matching results in the cleaned_content field of the pages table.
•	The results are ordered by pagerank to show the most relevant pages first.
Steps in the Flow:
•	Home Route (/): Displays the search page where users can input their search query. It renders the websearch.html template.
•	Search Route (/websearch): Processes the search form. When the user submits a search query, the app:
1.	Connects to the SQLite database.
2.	Executes a SQL query to search for URLs where the cleaned_content contains the search query.
3.	Orders the results by the Pagerank value to return the most relevant results.
4.	Renders the results.html template, displaying the search results.
4. How the Script Works
•	Step 1: Initialize Flask Application
The app is initialized with Flask(__name__, template_folder="./static"), specifying that templates (HTML files) are stored in the static folder.
•	Step 2: Home Route (/)
The home route is handled by the home() function, which simply renders the websearch.html template, allowing the user to enter a query.
•	Step 3: Search Route (/websearch)
The search() function processes the search query submitted via the form:
o	It retrieves the query using request.form["query"].
o	It connects to the crawled_pages.db database using sqlite3.connect("crawled_pages.db").
o	It executes a SQL query to search for pages whose cleaned_content contains the query, using the LIKE SQL operator. The query is also case-insensitive due to the % wildcards around the query string.
o	The results are ordered by the pagerank column, showing the highest-ranked results first.
o	The results are returned in the form of a list of tuples containing the URL and title of matching pages.
o	The connection to the database is closed.
o	The results.html template is rendered with the search results passed as a context variable.
5. Rendering the Templates
•	websearch.html: The search form in the websearch.html template allows users to enter a search query. The form submits the query to the /websearch endpoint.
<form method="post" action="/websearch">
    <input type="text" placeholder="Search..." name="query">
    <button type="submit">Search</button>
</form>
results.html: The results.html template is responsible for displaying the search results. If there are results, it will display the URLs and titles of matching pages. If no results are found, a message is displayed indicating that no results were found for the query.
{% if urls %}
    {% for url in urls %}
    <div class="results">
        <div class="result">
            <h3>{{url[1]}}</h3>
            <a href="{{url[0]}}">{{url[0]}}</a>
        </div>
    </div>
    {% endfor %}
{% else %}
    <h1>No results found for your query</h1>
{% endif %}
6. Output
•	The Flask app runs a local server where users can enter a search query. Once the search is submitted, it returns the most relevant results based on the cleaned_content field and sorted by pagerank.
•	The results are displayed as clickable URLs with the page title.

Conclusion
websearch.py is a simple web application that uses Flask to provide a search interface. It connects to an SQLite database (crawled_pages.db) to retrieve web page data, processes a search query, and returns results sorted by pagerank. The application serves as a foundation for creating a web-based search engine.






## How to start the program:
1.	Open the terminal 
2.	Type in terminal terminal:  cd “5.Web Search Engine Using Database”
3.	Then type : python web_spider.py
4.	Open another terminal
5.	Type in terminal  : cd “5.Web Search Engine Using Database”
6.	Then run : python websearch.py in order to start the server

### Description of Commands
1.	Open the terminal
o	This step involves launching a terminal or command prompt window to execute the commands required for the project. The terminal allows users to interact with the system via a command-line interface.
2.	Type in terminal:
cd "5.Web Search Engine Using Database"
o	The cd (change directory) command navigates to the specified folder, which in this case is the 5.Web Search Engine Using Database directory. This directory contains the necessary scripts (web_spider.py and websearch.py) and associated files for the web search engine.
3.	Then type:
python web_spider.py
o	This command executes the web_spider.py script using Python.
o	What it does:
	Starts the web crawler, which navigates through web pages starting from a seed URL, collects their content, and stores the information in a database (crawled_pages.db).
	It prepares the raw data needed for the search engine by creating a database of crawled web pages.
 
4.	Open another terminal
o	This step involves opening a second terminal or command prompt window to run another part of the project concurrently. This is necessary because the crawler and search engine server are separate processes and must run simultaneously.
5.	Type in terminal:
cd "5.Web Search Engine Using Database"
o	Similar to step 2, this navigates to the 5.Web Search Engine Using Database directory in the new terminal. This ensures the commands are executed in the correct folder, where the websearch.py script is located.
6.	Then run:
python websearch.py
o	This command starts the websearch.py script using Python.
o	What it does:
	Launches the web search engine server.
	The server uses the data collected and stored by web_spider.py in the database to process user queries.
	It listens for incoming requests (queries) and provides relevant search results based on the database content and ranking algorithms like PageRank.
 
## Summary
•	Steps 1–3: Run the web spider to crawl web pages and build a database.
•	Steps 4–6: Start the search engine server to handle queries and display results. This workflow ensures the web search engine is fully functional, with data collected by the crawler and served by the search engine application.

This is the final page we should be seeing on the Web page. 

![Screenshot 2025-01-07 204910](https://github.com/user-attachments/assets/d8332011-b8ef-4059-9bb3-76b225583020)


![Screenshot 2025-01-07 204924](https://github.com/user-attachments/assets/034c1881-3a87-41cb-a62c-b37798eba49a)
 
 
