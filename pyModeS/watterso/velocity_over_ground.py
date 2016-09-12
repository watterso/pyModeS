from collections import namedtuple

Velocity = namedtuple(
    'Velocity',
    ['east_west', 'north_south']
)


def subsonic_velocit_conversion(velocity):
    if velocity < 1023:
        return velocity - 1
    else:
        return velocity