import math


def tiletodegree(x, y, z):
    n = 2.0 ** z
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    lon = x / n * 360.0 - 180.0
    return lat, lon
