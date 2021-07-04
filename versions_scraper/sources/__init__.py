from abc import ABC
from abc import abstractmethod
from abc import abstractproperty

from bs4 import BeautifulSoup


class Source(ABC):

    @abstractproperty
    def URL(self) -> str:
        '''
        URL de onde os dados serão extraídos.
        '''
        ...

    @abstractproperty
    def DATA(self) -> dict:
        '''
        Dados extraídos da página.
        '''
        ...

    @abstractmethod
    def parse_data(self, soup: BeautifulSoup) -> dict:
        '''
        Método que extrai os dados da página.
        '''
        ...
