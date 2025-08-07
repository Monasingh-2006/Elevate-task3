import requests
from bs4 import BeautifulSoup

# Website link for news
url = "https://www.bbc.com/news"

# Send request to website
response = requests.get(url)

# Parse the website content
soup = BeautifulSoup(response.text, "html.parser")

# Find all headlines (BBC uses h3 for headlines)
headlines = soup.find_all('h2')

headline_List=[]
for h in headlines:
    text = h.get_text(strip=True)
    if text and text not in headline_List:
        headline_List.append(text)

# Print the first 10 headlines
print("Latest News Headlines:\n")
for i, headline in enumerate(headlines[:10], start=1):
    print(f"{i}. {headline.text.strip()}")

with open("headlines_output.txt", "w",encoding="utf-8") as file:
    file.write("Top news heading from BBC:\n\n")
    for i, headline in enumerate(headlines[:10], start=1):
        file.write(f"{i}. {headline.text.strip()}\n")
        
