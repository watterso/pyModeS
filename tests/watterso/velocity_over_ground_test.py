from pyModeS.util import bin2int
from pyModeS.util import hex2bin
from pyModeS.watterso.velocity_over_ground import subsonic_velocit_conversion
from pyModeS.watterso.velocity_over_ground import Velocity



VELOCITY_HEX = '8D485020994409940838175B284F'
MESSAGE_BODY = hex2bin(VELOCITY_HEX)[32:88]

def test_something():
    print('E/W: {}'.format(
        subsonic_velocit_conversion(bin2int(MESSAGE_BODY[14:24]))
    ))