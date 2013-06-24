import math


def earth_dist(lat1, lat2, lon1, lon2):
    print lat1, lat2, lon1, lon2
    print dir(lat1)
    lat1 = float(lat1)
    lat2 = float(lat2)
    lon1 = float(lon1)
    lon2 = float(lon2)
    
    piover180 = math.pi / 180
    earth_radius = 6372.795477598
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin((dlat / 2) * piover180) ** 2 + math.cos(lat1 * piover180) * math.cos(lat2 * piover180) * math.sin((dlon / 2) * piover180) ** 2
    c = math.asin(min(1, math.sqrt(a)))
    d = 2 * earth_radius * c
    return d
