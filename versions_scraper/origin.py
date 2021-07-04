from enum import Enum

from .sources.minecraftversions import MinecraftVersionsSource

class ScraperSources(Enum):
    minecraftversions = MinecraftVersionsSource
    mcversions = None

SOURCES = {
    'minecraftversions.com': ScraperSources.minecraftversions,
    'mcversions.net': ScraperSources.mcversions
}