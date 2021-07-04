from argparse import ArgumentParser
from argparse import Namespace
from argparse import RawTextHelpFormatter

from typing import NoReturn
from simple_term_menu import TerminalMenu

from . import __version__
from .scraper import VersionsScraper
from .origin import ScraperSources
from .origin import SOURCES


DESCRIPTION = f'''\u001b[32m
___  ____           ______          _____                     
|  \/  (_)          |  _  \        /  __ \                    
| .  . |_ _ __   ___| | | |___  ___| /  \/_ __ __ _ _____   _ 
| |\/| | | '_ \ / _ \ | | / _ \/ __| |   | '__/ _` |_  / | | |
| |  | | | | | |  __/ |/ / (_) \__ \ \__/\ | | (_| |/ /| |_| |
\_|  |_/_|_| |_|\___|___/ \___/|___/\____/_|  \__,_/___|\__, |
                                                         __/ |
                                                        |___/ 
\u001b[0m'''


class ModuleExecutor:

    def __init__(self):
        self.source = self.select_source()
        self.scraper = VersionsScraper(self.source)

    def select_source(self) -> ScraperSources:
        print('\nSelecione a fonte de onde os dados serão extraídos:')
        options = list(SOURCES.keys())
        select_source = TerminalMenu(options)
        selected = select_source.show()
        print(f'> \u001b[32m{options[selected]}\u001b[0m\n')
        return SOURCES[options[selected]]

    def run_scraper(self):
        self.scraper.get_website()
        self.scraper.parse_source_data()
        self.scraper.write_parsed_data()
        print('\nScraping finalizado com sucesso!\n')
    

class ModuleCLI:

    def __init__(self):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args()


    def create_parser(self) -> ArgumentParser:
        parser = ArgumentParser(
            prog='versions-scraper',
            description=DESCRIPTION,
            formatter_class=RawTextHelpFormatter,
        )

        parser.add_argument(
            '-v', '--version', 
            action='store_true', 
            help='show module version'
        )
        
        actions = parser.add_argument_group('project actions')
        actions.add_argument(
            '-s', '--scrape',
            action='store_true',
            help='scrape versions from suported website sources'
        )

        return parser


    def parse_args(self) -> NoReturn:
        if self.args.version:
            print(f'v{__version__}')

        if self.args.scrape:
            executor = ModuleExecutor()
            executor.run_scraper()


def main() -> NoReturn:
    try:
        cli = ModuleCLI()
        cli.parse_args()

    except TypeError:
        print('Fonte não implementada ainda!\n')
