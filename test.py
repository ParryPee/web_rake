from src.scraper import BaseScraper


class Example(BaseScraper):
    def __init__(self, requester=None, requester_config=None, parser=None, parser_type="html.parser"):
        parser_type = "json"
        if requester_config == None:
            requester_config = {}
            requester_config['respect_robots_txt'] = False  # API doesn't need robots.txt check
        super().__init__(requester, requester_config, parser, parser_type)
    
    
    def extract_data(self, parsed_content):
        return super().extract_data(parsed_content)
    