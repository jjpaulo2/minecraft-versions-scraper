from bs4 import BeautifulSoup
from pytest import mark

from tests.fixtures.minecraftversions import *
from versions_getter.sources.minecraftversions import MinecraftVersionsSource


source = MinecraftVersionsSource()
p_soup = BeautifulSoup(PAGE, 'lxml')
source.parse_data(p_soup)


@mark.parametrize('key', KEYS)
def test_got_expected_keys(key):
    assert key in source.DATA.keys()


@mark.parametrize('version', STABLE_VERSIONS)
class TestStableVersions:
    VERSIONS_KEY = 'Stable Releases'

    def test_got_release_versions(self, version):
        assert version in source.DATA[self.VERSIONS_KEY].keys()

    def test_got_client_stable_jars(self, version):
        assert source.DATA[self.VERSIONS_KEY][version] is not None

    def test_got_server_stable_jars(self, version):
        server_version = source.DATA[self.VERSIONS_KEY][version]['server']

        if version not in STABLE_WITHOUT_SERVER:
            assert server_version is not None
        else:
            assert server_version is None


@mark.parametrize('version', SNAPSHOT_VERSIONS)
class TestSnapshotVersions:
    VERSIONS_KEY = 'Snapshot Preview'

    def test_got_snapshot_versions(self, version):
        assert version in source.DATA[self.VERSIONS_KEY].keys()

    def test_got_client_snapshot_jars(self, version):
        client_version = source.DATA[self.VERSIONS_KEY][version]['client']
        assert client_version is not None 

    def test_got_server_snapshot_jars(self, version):
        server_version = source.DATA[self.VERSIONS_KEY][version]['server']
        assert server_version is not None 


@mark.parametrize('version', BETA_VERSIONS)
class TestBetaVersions:
    VERSIONS_KEY = 'Beta'

    def test_got_beta_versions(self, version):
        assert version in source.DATA[self.VERSIONS_KEY].keys()

    def test_got_client_snapshot_jars(self, version):
        client_version = source.DATA[self.VERSIONS_KEY][version]['client']
        assert client_version is not None 

    def test_did_not_get_server_snapshot_jars(self, version):
        server_version = source.DATA[self.VERSIONS_KEY][version]['server']
        assert server_version is None 


@mark.parametrize('version', ALPHA_VERSIONS)
class TestAlphaVersions:
    VERSIONS_KEY = 'Alpha'

    def test_got_expected_alpha_versions(self, version):
        assert version in source.DATA[self.VERSIONS_KEY].keys()

    def test_got_client_snapshot_jars(self, version):
        client_version = source.DATA[self.VERSIONS_KEY][version]['client']
        assert client_version is not None 

    def test_did_not_get_server_snapshot_jars(self, version):
        server_version = source.DATA[self.VERSIONS_KEY][version]['server']
        assert server_version is None 