import requests
from bs4 import BeautifulSoup

def fetch_books(url):
    # Fetch and parse the HTML content of the page
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching the webpage:", e)
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    books = []

    # Extract book titles and authors
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        author = book.find('p', class_='author')
        if author:
            books.append((title, author.get_text(strip=True)))
        else:
            books.append((title, "Unknown"))

    return books

def scrape_multiple_pages(base_url, page_count):
    # Scrape books from multiple pages
    all_books = []
    for page_num in range(1, page_count + 1):
        print("Scraping page " + str(page_num) + "...")
        page_url = base_url + "/page-" + str(page_num) + ".html"
        all_books.extend(fetch_books(page_url))
    return all_books

def main():
    """
    This function scrapes book titles and authors from an online bookstore
    by navigating multiple pages and displays the results.
    """
    base_url = "http://books.toscrape.com/catalogue"
    num_pages = 1  # Number of pages to scrape
    all_books = scrape_multiple_pages(base_url, num_pages)

    # Display the scraped books
    if all_books:
        print("\nBooks Scraped:\n")
        index = 1
        for book in all_books:
            print(str(index) + ". Title: " + book[0] + ", Author: " + book[1])
            index += 1
    else:
        print("No books found or there was an error.")

main()
