from bs4 import BeautifulSoup
from pytest import mark

from tests.fixtures.minecraftversions import PAGE
from tests.fixtures.minecraftversions import KEYS
from tests.fixtures.minecraftversions import STABLE_VERSIONS
from tests.fixtures.minecraftversions import SNAPSHOT_VERSIONS
from tests.fixtures.minecraftversions import BETA_VERSIONS
from tests.fixtures.minecraftversions import ALPHA_VERSIONS

from versions_getter.sources.minecraftversions import MinecraftVersionsSource


source = MinecraftVersionsSource()
p_soup = BeautifulSoup(PAGE, 'lxml')
source.parse_data(p_soup)


@mark.parametrize('key', KEYS)
def test_got_expected_keys(key):
    assert key in source.DATA.keys()

@mark.parametrize('version', STABLE_VERSIONS)
def test_got_expected_release_versions(version):
    assert version in source.DATA['Stable Releases'].keys()

@mark.parametrize('version', SNAPSHOT_VERSIONS)
def test_got_expected_snapshot_versions(version):
    assert version in source.DATA['Snapshot Preview'].keys()

@mark.parametrize('version', BETA_VERSIONS)
def test_got_expected_beta_versions(version):
    assert version in source.DATA['Beta'].keys()

@mark.parametrize('version', ALPHA_VERSIONS)
def test_got_expected_alpha_versions(version):
    assert version in source.DATA['Alpha'].keys()