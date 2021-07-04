from typing import NoReturn
from json import dumps

from requests import get
from bs4 import BeautifulSoup

from .sources import Source
from .origin import ScraperSources


class VersionsScraper:

    def __init__(self, source: ScraperSources):
        self.source = source.value()
        
    def get_website(self) -> NoReturn:
        site = get(self.source.URL)
        self.soup = BeautifulSoup(site.content, 'lxml')

    def parse_source_data(self) -> NoReturn:
        self.data = self.source.parse_data(self.soup)

    def write_parsed_data(self) -> NoReturn:
        with open('versions.json', 'w') as file:
            file_content = dumps(self.source.DATA, indent=4)
            file.write(file_content)
