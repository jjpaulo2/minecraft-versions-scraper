from bs4 import BeautifulSoup
from . import Source


class MinecraftVersionsSource(Source):

    URL = 'https://www.minecraftversions.com/'
    DATA = {}

    def parse_data(self, soup: BeautifulSoup) -> dict:
        divs = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-3')
        for div in divs:
            title_tag = div.select('span[class*="btn btn-lg btn-title"]')
            title = title_tag[0].string

            self.DATA[title] = {}

            versions = div.find_all('li', class_='list-group-item release')
            for version_tag in versions:
                version = version_tag.attrs['id']
                download_tag = version_tag.find('a', class_='btn btn-xs btn-info client')

                self.DATA[title][version] = download_tag.attrs['href']
        
        return self.DATA
