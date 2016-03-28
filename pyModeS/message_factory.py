from objects.message import AdsbMessage
from objects.message import ModeSMessage
from util import bin2int
from util import crc
from util import hex2bin
from util import timestamp


class MessageFactory:
    @staticmethod
    def construct_message(hex_message):
        binary_message = hex2bin(hex_message)
        #TODO(watterso) do something with crc check
        parity_check = binary_message[88:112]
        crc(parity_check)

        downlink_format = binary_message[0:5]

        time = timestamp()
        transponder_capability = binary_message[5:8]
        aircraft_icao_address = binary_message[8:32]
        type_code = binary_message[32:37]
        data_frame = binary_message[37:88]
        if bin2int(downlink_format) == 17:
            return AdsbMessageFactory.construct_message(
                time,
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
            time,
            transponder_capability,
            aircraft_icao_address,
            type_code,
            data_frame
    ):
        return AdsbMessage()
