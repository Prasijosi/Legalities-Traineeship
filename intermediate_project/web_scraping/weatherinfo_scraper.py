import requests
from bs4 import BeautifulSoup

def fetch_weather(city):
    """
    Fetches and returns the current weather information for a given city.
    
    Args:
    city (str): The name of the city to fetch weather information for.

    Returns:
    str: A string containing the weather information.
    """
    try:
        # Build the URL using string concatenation
        url = "http://wttr.in/" + city + "?format=3" 
        
        # Make an HTTP GET request to fetch the weather data
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        return response.text
    except requests.RequestException as e:
        return "Error fetching weather data: " + str(e)

def main():
    """
    Main function to handle user input and fetch weather information.
    """
    print("Weather Information Scraper")
    
    city = input("Enter the city name: ").strip()
    
    weather_info = fetch_weather(city)
    
    print("\nWeather for "+ weather_info)

main()
