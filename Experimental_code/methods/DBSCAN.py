from matplotlib.pyplot import *
from collections import defaultdict
import random
import numpy as np
import pandas as pd
import Latitude
import Longitude
import CRH1 as crh
import CATD1 as catd
import Experient2 as exp
import KDEm1 as kdem
import GTM1 as gtm
import Caculate1 as caculat
import matplotlib.pyplot as plt
import numpy.linalg as la
import Mean1 as mean
import Median1 as median
import xlsxwriter
import math
import Latitude as Lat
import Longitude as Lon


# function to calculate distance
def dist(p1, p2):
    Lat_dis=Lat.dis(p1[1], p1[0], p2[1], p2[0]);
    Lon_dis=Lon.dis(p1[1], p1[0], p2[1], p2[0]);
    dis=math.sqrt(Lat_dis**2+Lon_dis**2);
    return dis;
# randomly generate around 100 cartesian coordinates

#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/142_Trans.csv',encoding="gbk"));
#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/370_Trans.csv',encoding="gbk"));
# df1 = pd.DataFrame(pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_Trans.csv',encoding="gbk"));
df1 = pd.DataFrame(pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_Trans.csv',encoding="gbk"));
#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/810_Trans.csv',encoding="gbk"));
value_142=df1.values;


all_points = []

for i in range(len(value_142)):
    temp=[];
    temp.append(value_142[i,2]*pow(10,-6));
    temp.append(value_142[i,3]*pow(10,-6));
    if not temp in all_points:
        all_points.append(temp);

        # take radius = 8 and min. points = 8
E = 30
minPts = 10

# find out the core points
other_points = []
core_points = []
plotted_points = []
for point in all_points:
    point.append(0)  # assign initial level 0
    total = 0
    for otherPoint in all_points:
        distance = dist(otherPoint, point)
        if distance <= E:
            total += 1

    if total > minPts:
        core_points.append(point)
        plotted_points.append(point)
    else:
        other_points.append(point)

        # find border points
border_points = []
for core in core_points:
    for other in other_points:
        if dist(core, other) <= E:
            border_points.append(other)
            plotted_points.append(other)

# implement the algorithm
cluster_label = 0

for point in core_points:
    if point[2] == 0:
        cluster_label += 1
        point[2] = cluster_label

    for point2 in plotted_points:
        distance = dist(point2, point)
        if point2[2] == 0 and distance <= E:
            print(point, point2);
            point2[2] = point[2]

            # after the points are asssigned correnponding labels, we group them
cluster_list = defaultdict(lambda: [[], []])
for point in plotted_points:
    cluster_list[point[2]][0].append(point[0])
    cluster_list[point[2]][1].append(point[1])

markers = ['+', '*', '.', 'd', '^', 'v', '>', '<', 'p','1','2']

# plotting the clusters
i = 0
print(cluster_list);
for value in cluster_list:
    cluster = cluster_list[value]
    plot(cluster[0], cluster[1], markers[i])
    i = i % 10 + 1

# plot the noise points as well
noise_points = []
for point in all_points:
    if not point in core_points and not point in border_points:
        noise_points.append(point)
noisex = []
noisey = []
# for point in noise_points:
#     noisex.append(point[0])
#     noisey.append(point[1])
# plot(noisex, noisey, "x")

# title(str(len(cluster_list)) + " clusters created with E =" + str(E) + " Min Points=" + str(
#     minPts) + " total points=" + str(len(all_points)) + " noise Points = " + str(len(noise_points)))
# #axis((0, 60, 0, 60))
# show()


def LatAndLonToDis(lat1,lon1,lat2,lon2):
    Lat_dis = Lat.dis(lat1, lon1, lat2, lon2);
    Lon_dis = Lon.dis(lat1, lon1, lat2, lon2);
    dis=math.sqrt(Lat_dis**2+Lon_dis**2);
    return dis;

#bus_109_truth=pd.read_excel('F:/task/translation data/truth_line/117_truth.xlsx').values;
bus_142_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/142_truth.xlsx').values;
bus_370_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/293_truth.xlsx').values;
bus_802_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/802_truth.xlsx').values;
bus_810_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/810_truth.xlsx').values;
core_of_caluster=np.zeros(shape=[len(cluster_list),3]);

for value in cluster_list:
    Long_mean_temp=np.mean(cluster_list[value][0]);
    Lat_mean_temp=np.mean(cluster_list[value][1]);
    core_of_caluster[value-1,0]=value-1;
    core_of_caluster[value-1,1]=Long_mean_temp;
    core_of_caluster[value-1,2]=Lat_mean_temp;

station_of_142=[13,31];
station_of_370=[32,2,15];
station_of_802=[33,5,40,35,34,30,27];
station_of_810=[0,1,2,5,6,7,10,15,16,18,21];
near_142=np.zeros(shape=[len(station_of_142),3]);
dis_between_core_and_truth=[];
min_dis_index_142=[32,12];
min_dis_index_370=[19,34,9];
min_dis_index_802=[56,27,71,80,70,36,31];
min_dis_index_810=[25,37,18,28,38,39,31,6,2,32,23];

# for i in range(len(station_of_142)):
#     temp_dis=[];
#     for j in range(len(core_of_caluster)):
#         temp_dis.append(LatAndLonToDis(bus_142_truth[station_of_142[i],2],bus_142_truth[station_of_142[i],1],
#                        core_of_caluster[j,2],core_of_caluster[j,1]));
#     min_dis_index_142.append(temp_dis.index(min(temp_dis)));

# for i in range(len(station_of_370)):
#     temp_dis=[];
#     for j in range(len(core_of_caluster)):
#         temp_dis.append(LatAndLonToDis(bus_370_truth[station_of_370[i],2],bus_370_truth[station_of_370[i],1],
#                        core_of_caluster[j,2],core_of_caluster[j,1]));
#     min_dis_index_370.append(temp_dis.index(min(temp_dis)));
#
# for i in range(len(station_of_802)):
#     temp_dis=[];
#     for j in range(len(core_of_caluster)):
#         temp_dis.append(LatAndLonToDis(bus_802_truth[station_of_802[i],2],bus_802_truth[station_of_802[i],1],
#                        core_of_caluster[j,2],core_of_caluster[j,1]));
#     min_dis_index_802.append(temp_dis.index(min(temp_dis)));
#
# for i in range(len(station_of_810)):
#     temp_dis=[];
#     for j in range(len(core_of_caluster)):
#         temp_dis.append(LatAndLonToDis(bus_810_truth[station_of_810[i],2],bus_810_truth[station_of_810[i],1],
#                        core_of_caluster[j,2],core_of_caluster[j,1]));
#     min_dis_index_810.append(temp_dis.index(min(temp_dis)));

Mean_error_of_142=59.337446133037254;
Mean_error_of_370=181.31769644209496;
Mean_error_of_802=273.92582404490713;
Mean_error_of_810=382.87382725876773;

# for i in range(len(min_dis_index_142)):
#     Mean_error_of_142+=LatAndLonToDis(bus_142_truth[station_of_142[i],2],bus_142_truth[station_of_142[i],1],
#                         core_of_caluster[min_dis_index_142[i],2],core_of_caluster[min_dis_index_142[i],1]);

# for i in range(len(min_dis_index_370)):
#     Mean_error_of_370+=LatAndLonToDis(bus_370_truth[station_of_370[i],2],bus_370_truth[station_of_370[i],1],
#                         core_of_caluster[min_dis_index_370[i],2],core_of_caluster[min_dis_index_370[i],1]);
#
# for i in range(len(min_dis_index_802)):
#     Mean_error_of_802+=LatAndLonToDis(bus_802_truth[station_of_802[i],2],bus_802_truth[station_of_802[i],1],
#                         core_of_caluster[min_dis_index_802[i],2],core_of_caluster[min_dis_index_802[i],1]);
#
# for i in range(len(min_dis_index_810)):
#     Mean_error_of_810+=LatAndLonToDis(bus_810_truth[station_of_810[i],2],bus_810_truth[station_of_810[i],1],
#                         core_of_caluster[min_dis_index_810[i],2],core_of_caluster[min_dis_index_810[i],1]);

# Mean_error_of_142/=len(min_dis_index_142);
# Mean_error_of_370/=len(min_dis_index_370);
# Mean_error_of_802/=len(min_dis_index_802);
# Mean_error_of_810/=len(min_dis_index_802);

DBSCAN_mean_error=(Mean_error_of_142+Mean_error_of_370+Mean_error_of_802
                   +Mean_error_of_810)/23;

Coordinate_370_14=[113.04392,28.10387];
Coordinate_802_3=[113.03534,28.16808];
Coordinate_802_5=[113.00136,28.08514];
Coordinate_810_5=[113.03728,28.21225];
Coordinate_810_6=[113.03747,28.20945];
Coordinate_810_15=[113.03558,28.16669];
dis_370_14_Coordinate=[];
dis_802_3_Coordinate=[];
dis_802_5_Coordinate=[];
dis_810_5_Coordinate=[];
dis_810_6_Coordinate=[];
dis_810_15_Coordinate=[];

dis_370_14_Coordinate.append(Lat.dis(Coordinate_370_14[1],Coordinate_370_14[0],
                          bus_370_truth[15,2],bus_370_truth[15,1]));
dis_370_14_Coordinate.append(Lon.dis(Coordinate_370_14[1],Coordinate_370_14[0],
                          bus_370_truth[15,2],bus_370_truth[15,1]));

dis_802_3_Coordinate.append(Lat.dis(Coordinate_802_3[1],Coordinate_802_3[0],
                          bus_802_truth[33,2],bus_802_truth[33,1]));
dis_802_3_Coordinate.append(Lon.dis(Coordinate_802_3[1],Coordinate_802_3[0],
                          bus_802_truth[33,2],bus_802_truth[33,1]));

dis_802_5_Coordinate.append(Lat.dis(Coordinate_802_5[1],Coordinate_802_5[0],
                          bus_802_truth[5,2],bus_802_truth[5,1]));
dis_802_5_Coordinate.append(Lon.dis(Coordinate_802_5[1],Coordinate_802_5[0],
                          bus_802_truth[5,2],bus_802_truth[5,1]));

dis_810_5_Coordinate.append(Lat.dis(Coordinate_810_5[1],Coordinate_810_5[0],
                          bus_810_truth[5,2],bus_810_truth[5,1]));
dis_810_5_Coordinate.append(Lon.dis(Coordinate_810_5[1],Coordinate_810_5[0],
                          bus_810_truth[5,2],bus_810_truth[5,1]));

dis_810_6_Coordinate.append(Lat.dis(Coordinate_810_6[1],Coordinate_810_6[0],
                          bus_810_truth[6,2],bus_810_truth[6,1]));
dis_810_6_Coordinate.append(Lon.dis(Coordinate_810_6[1],Coordinate_810_6[0],
                          bus_810_truth[6,2],bus_810_truth[6,1]));

dis_810_15_Coordinate.append(Lat.dis(Coordinate_810_15[1],Coordinate_810_15[0],
                          bus_810_truth[15,2],bus_810_truth[15,1]));
dis_810_15_Coordinate.append(Lon.dis(Coordinate_810_15[1],Coordinate_810_15[0],
                          bus_810_truth[15,2],bus_810_truth[15,1]));
