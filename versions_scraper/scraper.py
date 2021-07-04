from typing import NoReturn
from json import dumps

from requests import get
from bs4 import BeautifulSoup

from .sources import Source
from .origin import ScraperSources


class VersionsScraper:

    def __init__(self, source: ScraperSources):
        print('Definindo a origem dos dados...')
        self.source = source.value()
        
    def get_website(self) -> NoReturn:
        print('Fazendo download da página...')
        site = get(self.source.URL)
        self.soup = BeautifulSoup(site.content, 'lxml')

    def parse_source_data(self) -> NoReturn:
        print('Obtendo os dados necessários...')
        self.data = self.source.parse_data(self.soup)

    def write_parsed_data(self) -> NoReturn:
        print('Gravando os dados no arquivo \u001b[33mversions.json\u001b[0m...')
        with open('versions.json', 'w') as file:
            file_content = dumps(self.source.DATA, indent=4)
            file.write(file_content)
