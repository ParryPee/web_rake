# Weather Scraper

A modular and extensible web scraping framework designed specifically for fetching and parsing weather data from Data.gov.sg's weather API.

## Features

- Robust HTTP requesting with built-in retry logic, rate limiting, and robots.txt compliance
- Multiple parser types (HTML, JSON, XML) with a unified interface
- Modular architecture allowing easy extension for different data sources
- Specific implementation for Data.gov.sg's weather API
- Configurable request parameters (headers, timeouts, user agent rotation)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/weather-scraper.git

# Navigate to the project directory
cd weather-scraper

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from examples.weather_scraper import WeatherScraper

# Create an instance of the weather scraper
scraper = WeatherScraper()

# Scrape the weather data
url = "https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast"
result = scraper.scrape(url)

# Process the results
print(result)
```

### Advanced Configuration

```python
from scrapers.weather_scraper import WeatherScraper

# Configure with custom settings
scraper = WeatherScraper(
    requester_config={
        'timeout': 60,
        'retry_count': 5,
        'retry_delay': 3,
        'user_agent_rotation': True,
        'rate_limit': 2  # seconds between requests
    }
)

# Scrape with custom parameters
result = scraper.scrape(
    "https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast",
    params={"date": "2023-04-20"}
)
```

## Project Structure

```
weather-scraper/
├── .gitignore
├── README.md
├── requirements.txt        # Project dependencies
├── examples/               # Specific scraper implementations
│   ├── __init__.py
│   └── weather_scraper.py  # Weather API scraper
└── src/                    # Core framework
    ├── __init__.py
    ├── parser.py           # Parser implementations (HTML, JSON, XML)
    ├── requester.py        # HTTP request handling
    └── scraper.py          # Base scraper class
```

## Core Components

### Requester (`src/requester.py`)

Handles all HTTP operations with features like:
- Retry logic with exponential backoff
- Rate limiting
- User-agent rotation
- Robots.txt compliance

### Parser (`src/parser.py`)

Provides parsers for different content types:
- `HTMLParser`: Uses BeautifulSoup for HTML parsing
- `JSONParser`: Parses JSON responses
- `XMLParser`: Handles XML content

### BaseScraper (`src/scraper.py`)

Abstract base class that integrates the requester and parser components and defines the core scraping workflow.

### WeatherScraper (`examples/weather_scraper.py`)

Implementation of the BaseScraper specific to Data.gov.sg's weather API, with custom data extraction logic.

## Requirements

- Python 3.6+
- BeautifulSoup4
- Requests
- (other dependencies should be listed in requirements.txt)

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

Your Name - larrylee2003@live.com

Project Link: [https://github.com/parrypee/weather-scraper](https://github.com/ParryPee/web_rake)