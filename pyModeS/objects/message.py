class ModeSMessage(object):
    pass


class AdsbMessage(ModeSMessage):
    downlink_format = 17

    def __init__(
            self,
            transponder_capability,
            aircraft_icao_address,
    ):
        self.transponder_capability = transponder_capability
        self.aircraft_icao_address = aircraft_icao_address


class AdsbVelocityMessage(AdsbMessage):

    def __init__(self, ca, icao, speed):
        super(AdsbVelocityMessage, self).__init__(ca, icao)
        self.speed = speed
