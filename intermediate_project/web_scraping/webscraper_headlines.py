import requests
from bs4 import BeautifulSoup

def fetch_headline(url):
    """
    Fetches and prints headlines from a news website.
    
    This function takes a URL of a news website, retrieves the HTML content of the page,
    and extracts headlines based on the HTML structure. It uses the BeautifulSoup library
    to parse the HTML and find the headlines within specific HTML tags.
    """
    try:
        # Make an HTTP GET request to fetch the HTML content of the webpage
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = []
    for headline in soup.find_all('h2'):
        # Get the text from each <h2> tag and strip any extra whitespace
        headlines.append(headline.get_text(strip=True))

    return headlines

def main():
    """
    Main function to run the web scraper.
    
    This function provides a URL to the fetch_headlines function, retrieves the headlines,
    and prints them to the console.
    """
    url = 'https://ekantipur.com/news'
    headlines = fetch_headline(url)
    
    if headlines:
        print("Headlines from Ekantipur News:")
        # Prints each headline with a number
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
    else:
        print("No headlines found or there was an error.")

main()
