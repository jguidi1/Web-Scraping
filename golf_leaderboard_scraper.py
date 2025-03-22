import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL
url = "https://www.pgatour.com/leaderboard" # Example URL: "https://www.pgatour.com/leaderboard.html"

# Step 2: Send a GET request to fetch the HTML content
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page!")
    #print(response.text[:500])  # Print the first 500 characters of HTML
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")


# Step 4: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])  # First 1000 characters for a clean view