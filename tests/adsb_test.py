from pyModeS import adsb
from pyModeS.objects.speed import AirSpeed
from pyModeS.objects.speed import GroundSpeed


def test_adsb_icao():
    assert adsb.icao('8D406B902015A678D4D220AA4BDA') == '406B90'


def test_adsb_category():
    assert adsb.category('8D406B902015A678D4D220AA4BDA') == 5


def test_adsb_callsign():
    assert adsb.callsign('8D406B902015A678D4D220AA4BDA') == 'EZY85MH_'


def test_adsb_position():
    pos = adsb.position('8D40058B58C901375147EFD09357',
                        '8D40058B58C904A87F402D3B8C59',
                        1446332400, 1446332405)
    assert pos == (49.81755, 6.08442)


def test_adsb_alt():
    assert adsb.altitude('8D40058B58C901375147EFD09357') == 39000


def test_nic():
    assert adsb.nic('8D3C70A390AB11F55B8C57F65FE6') == 0
    assert adsb.nic('8DE1C9738A4A430B427D219C8225') == 1
    assert adsb.nic('8D44058880B50006B1773DC2A7E9') == 2
    assert adsb.nic('8D44058881B50006B1773DC2A7E9') == 3
    assert adsb.nic('8D4AB42A78000640000000FA0D0A') == 4
    assert adsb.nic('8D4405887099F5D9772F37F86CB6') == 5
    assert adsb.nic('8D4841A86841528E72D9B472DAC2') == 6
    assert adsb.nic('8D44057560B9760C0B840A51C89F') == 7
    assert adsb.nic('8D40621D58C382D690C8AC2863A7') == 8
    assert adsb.nic('8F48511C598D04F12CCF82451642') == 9
    assert adsb.nic('8DA4D53A50DBF8C6330F3B35458F') == 10
    assert adsb.nic('8D3C4ACF4859F1736F8E8ADF4D67') == 11


class TestAdsbVelocity:

    def test_ground_speed(self):
        vgs = adsb.velocity('8D485020994409940838175B284F')
        assert vgs == (159, 182.9, -263, 'GS')

    def test_air_speed(self):
        vas = adsb.velocity('8DA05F219B06B6AF189400CBC33F')
        assert vas == (376, 244.0, -274, 'AS')

    def assert_speed_obj_type(self, hex_msg, expected_type):
        assert isinstance(adsb.extract_speed(hex_msg), expected_type)

    def test_air_speed_obj(self):
        self.assert_speed_obj_type(
            '8DA05F219B06B6AF189400CBC33F',
            AirSpeed
        )

    def test_ground_speed_obj(self):
        self.assert_speed_obj_type(
            '8D485020994409940838175B284F',
            GroundSpeed
        )
