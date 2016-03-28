from pyModeS.adsb import extract_speed_from_data_frame
from pyModeS.adsb_type_codes import VELOCITY
from pyModeS.objects.message import AdsbMessage
from pyModeS.objects.message import AdsbVelocityMessage
from pyModeS.objects.message import ModeSMessage
from pyModeS.util import bin2int
from pyModeS.util import crc
from pyModeS.util import hex2bin


class MessageFactory:
    @staticmethod
    def construct_message(hex_message):
        binary_message = hex2bin(hex_message)
        #TODO(watterso) do something with crc check
        parity_check = binary_message[88:112]
        crc(parity_check)

        downlink_format = binary_message[0:5]
        transponder_capability = binary_message[5:8]
        aircraft_icao_address = binary_message[8:32]
        type_code = binary_message[32:37]
        data_frame = binary_message[37:88]
        if bin2int(downlink_format) == 17:
            return AdsbMessageFactory.construct_message(
                transponder_capability,
                aircraft_icao_address,
                type_code,
                data_frame
            )
        return ModeSMessage()


class AdsbMessageFactory:
    @classmethod
    def construct_message(
            cls,
            transponder_capability,
            aircraft_icao_address,
            type_code,
            data_frame
    ):

        type_code_int = bin2int(type_code)
        if type_code_int == VELOCITY:
            return AdsbVelocityMessage(
                transponder_capability,
                aircraft_icao_address,
                extract_speed_from_data_frame(data_frame)
            )
        return AdsbMessage(transponder_capability, aircraft_icao_address)
