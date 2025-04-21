import sys
import os
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)




from src.scraper import BaseScraper
from src.parser import JSONParser


class WeatherScraper(BaseScraper):
    """Scraper for Data.gov.sg weather API"""
    
    def __init__(self, **kwargs):
        # Override default parser type to json
        kwargs['parser_type'] = 'json'
        
        # Configure requester if needed
        requester_config = kwargs.get('requester_config', {})
        requester_config['respect_robots_txt'] = False  # API doesn't need robots.txt check
        
        super().__init__(requester_config=requester_config, **kwargs)
    
    def extract_data(self, parsed_content):
        """Extract weather data from the parsed JSON content.
        
        Args:
            parsed_content (dict): Parsed JSON content
            
        Returns:
            dict: Extracted weather data
        """
        try:
            # The data appears to be in parsed_content['data']['records']
            records = parsed_content.get('data', {}).get('records', [])
            
            if not records:
                return {
                    'error': "No weather records found in the API response",
                    'raw_data': parsed_content
                }
            
            # Get the first record (assuming there's only one, based on your sample)
            record = records[0]
            
            # Extract general forecast information
            general = record.get('general', {})
            temperature = general.get('temperature', {})
            valid_period = general.get('validPeriod', {})
            
            # Format the data
            result = {
                'forecast_date': record.get('date', ''),
                'updated_timestamp': record.get('updatedTimestamp', ''),
                'general_forecast': general.get('forecast', {}).get('text', ''),
                'temperature': {
                    'low': temperature.get('low', ''),
                    'high': temperature.get('high', ''),
                    'unit': temperature.get('unit', 'Degrees Celsius')
                },
                'humidity': {
                    'low': general.get('relativeHumidity', {}).get('low', ''),
                    'high': general.get('relativeHumidity', {}).get('high', ''),
                    'unit': general.get('relativeHumidity', {}).get('unit', 'Percentage')
                },
                'wind': {
                    'speed': {
                        'low': general.get('wind', {}).get('speed', {}).get('low', ''),
                        'high': general.get('wind', {}).get('speed', {}).get('high', '')
                    },
                    'direction': general.get('wind', {}).get('direction', '')
                },
                'valid_period': {
                    'start': valid_period.get('start', ''),
                    'end': valid_period.get('end', ''),
                    'text': valid_period.get('text', '')
                },
                'periods': []
            }
            
            # Add period-specific forecasts
            for period in record.get('periods', []):
                time_period = period.get('timePeriod', {})
                regions = period.get('regions', {})
                
                period_data = {
                    'time': {
                        'start': time_period.get('start', ''),
                        'end': time_period.get('end', ''),
                        'text': time_period.get('text', '')
                    },
                    'regions': {}
                }
                
                # Process each region
                for region, forecast in regions.items():
                    period_data['regions'][region] = {
                        'code': forecast.get('code', ''),
                        'text': forecast.get('text', '')
                    }
                
                result['periods'].append(period_data)
            
            return result
        except (KeyError, IndexError) as e:
            # Handle unexpected API response format
            return {
                'error': f"Failed to parse weather data: {str(e)}",
                'raw_data': parsed_content
            }
