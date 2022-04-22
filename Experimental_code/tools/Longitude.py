# import math
# EARTH_RADIUS = 6371393; # 地球半径, 单位米
# def rad(d):
#     return d * math.pi / 180.0;
# def getDistance(lat1,lng1,lat2,lng2):
#     radLat1 = rad(lat1);
#     radLat2 = rad(lat2);
#     a = radLat1 - radLat2;
#     b = rad(lng1) - rad(lng2);
#     s = 2 * math.asin(math.sqrt(math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)));
#     s = s * EARTH_RADIUS;
#     s = s * 10000 / 10000;
#     return round(s);
import math
def dis(lat1,lng1,lat2,lng2):
    dx = lng1 - lng2    #经度差值
    dy = lat1 - lat2    #纬度差值
    b = (lat1+lat2)/2   #平均纬度
    lx = math.radians(dx)*6371391*math.cos(math.radians(b))
    ly = 6371391*math.radians(dy)
    return round(lx);