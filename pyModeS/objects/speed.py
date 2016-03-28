class Speed:
    # speed - in knots
    # heading - in degrees
    # rate_of_climb - in ft/min
    def __init__(self, speed, heading, rate_of_climb):
        self.speed = speed
        self.heading = heading
        self.rate_of_climb = rate_of_climb


class AirSpeed(Speed):
    # Speed of aircraft relative to the air
    pass


class GroundSpeed(Speed):
    # Speed of aircraft relative to the ground
    pass