📰 Web Scraper for News Headlines
✅ Objective:
This project is a simple Python-based web scraper that fetches the latest news headlines from a website using requests and BeautifulSoup. It demonstrates basic web scraping and output handling.

🔧 Tools & Technologies Used:
Libraries: requests, beautifulsoup4
Text Editor: Python IDLE / VS Code
Platform: GitHub (for code hosting)

📂 Project Files:
web.py: Main Python script that fetches and prints headlines.
bbc_text.txt
README.md

🧑‍💻 Steps to Run the Project:
1. Install Python
2. Install Required Libraries
Open Command Prompt or Terminal and run:
pip install requests
pip install beautifulsoup4
3. Save the Python Code
Save the following code in a file named web.py:

Example code
import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all('h2')

print("Latest News Headlines:\n")
for i, headline in enumerate(headlines[:10], start=1):
    print(f"{i}. {headline.text.strip()}")
    
4. Run the Script
In your terminal or IDLE:

python news_scraper.py
You will see the top 10 news headlines printed from BBC News.

📷 Sample Output:
Latest News Headlines:

1. India wins historic cricket match
2. Global economic growth slows
3. New tech unveiled at conference
...
🔄 How It Works:
requests is used to get the HTML content of the website.
BeautifulSoup parses the HTML and extracts <h2> tags (headlines).
A loop prints the top 10 headlines cleanly.


The code can be customized to work with other news websites by changing the URL and HTML tags
