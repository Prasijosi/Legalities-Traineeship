from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    """
    Sets up the Selenium WebDriver with Chrome.
    
    Returns:
    WebDriver instance: Configured Selenium WebDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)
    
    # Provide the path 
    service = Service("C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def fetch_books(driver, url):
    """
    Fetches book titles and authors from the specified URL.
    
    Args:
    driver (WebDriver): The Selenium WebDriver instance.
    url (str): The URL of the page to scrape.
    
    Returns:
    list: A list of tuples containing book titles and authors.
    """
    driver.get(url)
    time.sleep(5) 
    
    books = []
    book_elements = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
    
    for book in book_elements:
        title = book.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('title')
        author = book.find_element(By.XPATH, './/p[@class="author"]').text
        books.append((title, author))
    
    return books

def main():
    """
    Main function to set up the WebDriver, scrape book details, and print them.
    """
    url = "http://books.toscrape.com/catalogue"
    
    # Set up WebDriver
    driver = setup_driver()
    
    try:
        books = fetch_books(driver, url)
        for idx, (title, author) in enumerate(books, 1):
            print(idx, ". Title: ", title, ", Author: ", author)
    finally:
        driver.quit()

main()
