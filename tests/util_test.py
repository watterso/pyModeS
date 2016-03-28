from pyModeS import util


def test_hex2bin():
    assert util.hex2bin('6E406B') == "011011100100000001101011"


def test_crc_decode():
    checksum = util.crc("8D406B902015A678D4D220AA4BDA")
    assert checksum == "000000000000000000000000"


def test_crc_encode():
    parity = util.crc("8D406B902015A678D4D220AA4BDA", encode=True)
    assert util.hex2bin("AA4BDA") == parity


def test_downlink_format():
    message = '8D485020994409940838175B284F'
    assert util.downlink_format(message) == 17


def test_transponder_capability():
    message = '8D485020994409940838175B284F'
    assert util.transponder_capability(message) == 5
