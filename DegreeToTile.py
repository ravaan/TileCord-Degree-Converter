import math


def degreetotile(lat, lon, z):
    lat = math.radians(lat)
    n = 2.0 ** z
    y = int((1.0 - math.log(math.tan(lat) + (1 / math.cos(lat)))))
    x = int((lon + 180.0) / 360.0 * n)
    return x, y
