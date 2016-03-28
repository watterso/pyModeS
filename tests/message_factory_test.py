from pyModeS.message_factory import AdsbMessageFactory
from pyModeS.message_factory import MessageFactory
from pyModeS.objects.message import AdsbMessage
from pyModeS.objects.message import AdsbVelocityMessage
from pyModeS.util import hex2bin

hex_string = '8D485020994409940838175B284F'
binary_string = hex2bin(hex_string)


def test_message_factory():
    construct = MessageFactory.construct_message(hex_string)
    assert isinstance(construct, AdsbMessage)

binary_message = binary_string
transponder_capability = binary_message[5:8]
aircraft_icao_address = binary_message[8:32]
type_code = binary_message[32:37]
data_frame = binary_message[37:88]


def test_adsb_message_factory():
    msg = AdsbMessageFactory.construct_message(
        transponder_capability,
        aircraft_icao_address,
        type_code,
        data_frame
    )
    assert isinstance(msg, AdsbMessage)


def test_adsb_message_factory_velocity():
    msg = AdsbMessageFactory.construct_message(
        transponder_capability,
        aircraft_icao_address,
        type_code,
        data_frame
    )
    assert isinstance(msg, AdsbVelocityMessage)
