from matplotlib.pyplot import *
from collections import defaultdict
import random
import numpy as np
import pandas as pd
import Latitude
import Longitude
import CRH1 as crh
import CATD1 as catd
import CBS as exp
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

#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/near_point/109_Trans.csv',encoding="gbk"));
#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/near_point/142_Trans.csv',encoding="gbk"));
#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/near_point/370_Trans.csv',encoding="gbk"));
#df1 = pd.DataFrame(pd.read_csv('F:\PythonWorkplace/bus_station_with_subway_data/near_point/802_Trans.csv',encoding="gbk"));
df1 = pd.DataFrame(pd.read_csv('bus_station_with_subway_data/near_point/810_Trans.csv',encoding="gbk"));
value_142=df1.values;

all_points = []

for i in range(len(value_142)):
    temp=[];
    temp.append(value_142[i,2]*pow(10,-6));
    temp.append(value_142[i,3]*pow(10,-6));
    temp.append(value_142[i,0]);
    if not temp in all_points:
        all_points.append(temp);

        # take radius = 8 and min. points = 8
E = 30
minPts = 11

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
    if point[3] == 0:
        cluster_label += 1
        point[3] = cluster_label

    for point2 in plotted_points:
        distance = dist(point2, point)
        if point2[3] == 0 and distance <= E:
            print(point, point2);
            point2[3] = point[3]

            # after the points are asssigned correnponding labels, we group them
cluster_list = defaultdict(lambda: [[], [],[]])
for point in plotted_points:
    cluster_list[point[3]][0].append(point[0])
    cluster_list[point[3]][1].append(point[1])
    cluster_list[point[3]][2].append(point[2])

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

#bus_109_truth=pd.read_excel('F:/task/translation data/truth_line/109_truth.xlsx').values;
#bus_142_truth=pd.read_excel('F:/task/translation data/truth_line/142_truth.xlsx').values;
bus_370_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/293_truth.xlsx').values;
bus_802_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/802_truth.xlsx').values;
bus_810_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/810_truth.xlsx').values;
core_of_caluster=np.zeros(shape=[len(cluster_list),4]);

for value in cluster_list:
    Long_mean_temp=np.mean(cluster_list[value][0]);
    Lat_mean_temp=np.mean(cluster_list[value][1]);
    core_of_caluster[value-1,0]=value-1;
    core_of_caluster[value-1,1]=Long_mean_temp;
    core_of_caluster[value-1,2]=Lat_mean_temp;

station_of_109=[7];
station_of_142=[13,21,23,24,31];
station_of_370=[39,33,32,2,15];
station_of_802=[5,4,40,35,30,29,27];
station_of_810=[0,1,2,5,6,7,8,9,10,13,16,17,18,21,22,23];
near_142=np.zeros(shape=[len(station_of_142),3]);
dis_between_core_and_truth=[];
# min_dis_index_109=[11];
# min_dis_index_142=[31,28,9,34,12];
# min_dis_index_370=[43,39,19,32,9];
# min_dis_index_802=[25,51,71,81,34,63,29];
# min_dis_index_810=[22,35,15,26,36,38,31,0,29,34,1,14,30,20,25,6];

min_dis_index_109=[7];
min_dis_index_142=[31,28,9,34,12];
min_dis_index_370=[43,39,19,32,9];
min_dis_index_802=[34,52,69,79,35,62,29];
min_dis_index_810=[20,33,13,24,34,35,29,0,27,32,1,12,28,18,23,6];

# for i in range(len(station_of_109)):
#     temp_dis=[];
#     for j in range(len(core_of_caluster)):
#         temp_dis.append(LatAndLonToDis(bus_109_truth[station_of_109[i],2],bus_109_truth[station_of_109[i],1],
#                        core_of_caluster[j,2],core_of_caluster[j,1]));
#     min_dis_index_109.append(temp_dis.index(min(temp_dis)));

# for i in range(len(station_of_142)):
#     temp_dis=[];
#     for j in range(len(core_of_caluster)):
#         temp_dis.append(LatAndLonToDis(bus_142_truth[station_of_142[i],2],bus_142_truth[station_of_142[i],1],
#                        core_of_caluster[j,2],core_of_caluster[j,1]));
#     min_dis_index_142.append(temp_dis.index(min(temp_dis)));
#
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

# Mean_error_of_109=14.317821063276353;
# Mean_error_of_142=174.42085365191866;
# Mean_error_of_370=190.03975202620913;
# Mean_error_of_802=260.8213019963557;
# Mean_error_of_810=497.22349046955645;

Mean_error_of_109=527.5613708375548;
Mean_error_of_142=174.42085365191866;
Mean_error_of_370=191.27423810581524;
Mean_error_of_802=254.08881713022217;
Mean_error_of_810=507.7405857736514;

# for i in range(len(min_dis_index_109)):
#     Mean_error_of_109+=LatAndLonToDis(bus_109_truth[station_of_109[i],2],bus_109_truth[station_of_109[i],1],
#                         core_of_caluster[min_dis_index_109[i],2],core_of_caluster[min_dis_index_109[i],1]);

# for i in range(len(min_dis_index_142)):
#     Mean_error_of_142+=LatAndLonToDis(bus_142_truth[station_of_142[i],2],bus_142_truth[station_of_142[i],1],
#                         core_of_caluster[min_dis_index_142[i],2],core_of_caluster[min_dis_index_142[i],1]);
#
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

#Mean_error_of_109/=len(min_dis_index_109);
# Mean_error_of_142/=len(min_dis_index_142);
# Mean_error_of_370/=len(min_dis_index_370);
# Mean_error_of_802/=len(min_dis_index_802);
# Mean_error_of_810/=len(min_dis_index_802);

DBSCAN_mean_error=(Mean_error_of_142+Mean_error_of_370+Mean_error_of_802
                   +Mean_error_of_810+Mean_error_of_109)/34;

Coordinate_370_33=[112.99360076,28.1441561];
Coordinate_370_39=[112.99259552,28.16997148];
Coordinate_802_5=[113.00123718,28.084956];
Coordinate_802_4=[112.99833182,28.08115737];
Coordinate_810_8=[113.0371935,28.20150095];
Coordinate_810_9=[113.03713145,28.19838436];
Coordinate_810_16=[113.03630133,28.15907187];
dis_370_33_Coordinate=[];
dis_370_39_Coordinate=[];
dis_802_5_Coordinate=[];
dis_802_4_Coordinate=[];
dis_810_8_Coordinate=[];
dis_810_9_Coordinate=[];
dis_810_16_Coordinate=[];

dis_370_33_Coordinate.append(Lat.dis(Coordinate_370_33[1],Coordinate_370_33[0],
                          bus_370_truth[33,2],bus_370_truth[33,1]));
dis_370_33_Coordinate.append(Lon.dis(Coordinate_370_33[1],Coordinate_370_33[0],
                          bus_370_truth[33,2],bus_370_truth[33,1]));

dis_370_39_Coordinate.append(Lat.dis(Coordinate_370_39[1],Coordinate_370_39[0],
                          bus_370_truth[39,2],bus_370_truth[39,1]));
dis_370_39_Coordinate.append(Lon.dis(Coordinate_370_39[1],Coordinate_370_39[0],
                          bus_370_truth[39,2],bus_370_truth[39,1]));

dis_802_5_Coordinate.append(Lat.dis(Coordinate_802_5[1],Coordinate_802_5[0],
                          bus_802_truth[5,2],bus_802_truth[5,1]));
dis_802_5_Coordinate.append(Lon.dis(Coordinate_802_5[1],Coordinate_802_5[0],
                          bus_802_truth[5,2],bus_802_truth[5,1]));

dis_802_4_Coordinate.append(Lat.dis(Coordinate_802_4[1],Coordinate_802_4[0],
                          bus_802_truth[4,2],bus_802_truth[4,1]));
dis_802_4_Coordinate.append(Lon.dis(Coordinate_802_4[1],Coordinate_802_4[0],
                          bus_802_truth[4,2],bus_802_truth[4,1]));

dis_810_8_Coordinate.append(Lat.dis(Coordinate_810_8[1],Coordinate_810_8[0],
                          bus_810_truth[8,2],bus_810_truth[8,1]));
dis_810_8_Coordinate.append(Lon.dis(Coordinate_810_8[1],Coordinate_810_8[0],
                          bus_810_truth[8,2],bus_810_truth[8,1]));

dis_810_9_Coordinate.append(Lat.dis(Coordinate_810_9[1],Coordinate_810_9[0],
                          bus_810_truth[9,2],bus_810_truth[9,1]));
dis_810_9_Coordinate.append(Lon.dis(Coordinate_810_9[1],Coordinate_810_9[0],
                          bus_810_truth[9,2],bus_810_truth[9,1]));

dis_810_16_Coordinate.append(Lat.dis(Coordinate_810_16[1],Coordinate_810_16[0],
                          bus_810_truth[16,2],bus_810_truth[16,1]));
dis_810_16_Coordinate.append(Lon.dis(Coordinate_810_16[1],Coordinate_810_16[0],
                          bus_810_truth[16,2],bus_810_truth[16,1]));
