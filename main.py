
from scrapers.weather_scraper import WeatherScraper


scraper = WeatherScraper()
url = "https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast"

result = scraper.scrape(url)

# Print the result