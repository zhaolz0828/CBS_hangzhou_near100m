import math

import numpy as np
import pandas as pd

import Latitude as Lat
import Longitude as Lon


#经纬度转化
def LatAndLonToDis(lat1,lon1,lat2,lon2):
    Lat_dis = Lat.dis(lat1, lon1, lat2, lon2);
    Lon_dis = Lon.dis(lat1, lon1, lat2, lon2);
    dis=math.sqrt(Lat_dis**2+Lon_dis**2);
    return dis;

def Latdis(lat1,lon1,lat2,lon2):
    Lat_dis = Lat.dis(lat1, lon1, lat2, lon2);
    return Lat_dis;

def Londis(lat1,lon1,lat2,lon2):
    Lon_dis = Lon.dis(lat1, lon1, lat2, lon2);
    return Lon_dis;


# #data
# bus_109_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_CATD.csv',
#                          header=None,encoding='gbk').values;
# bus_109_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_CRH.csv',
#                          header=None,encoding='gbk').values;
# bus_109_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_GTM.csv',
#                          header=None,encoding='gbk').values;
# bus_109_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_TMVD.csv',
#                          header=None,encoding='gbk').values;
# bus_109_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_KDEm.csv',
#                          header=None,encoding='gbk').values;
# bus_109_Mean=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_Mean.csv',
#                          header=None,encoding='gbk').values;
# bus_109_Median=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_Median.csv',
#                          header=None,encoding='gbk').values;
# bus_802_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_CATD.csv',
#                          header=None,encoding='gbk').values;
# bus_802_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_CRH.csv',
#                          header=None,encoding='gbk').values;
# bus_802_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_GTM.csv',
#                          header=None,encoding='gbk').values;
# bus_802_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_TMVD.csv',
#                          header=None,encoding='gbk').values;
# bus_802_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_KDEm.csv',
#                          header=None,encoding='gbk').values;



#data
bus_109_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_CATD.csv',
                         header=None,encoding='gbk').values;
bus_109_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_CRH.csv',
                         header=None,encoding='gbk').values;
bus_109_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_GTM.csv',
                         header=None,encoding='gbk').values;
bus_109_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_TMVD.csv',
                         header=None,encoding='gbk').values;
bus_109_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_KDEm.csv',
                         header=None,encoding='gbk').values;
bus_109_Mean=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_Mean.csv',
                         header=None,encoding='gbk').values;
bus_109_Median=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/109_Median.csv',
                         header=None,encoding='gbk').values;
bus_802_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_CATD.csv',
                         header=None,encoding='gbk').values;
bus_802_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_CRH.csv',
                         header=None,encoding='gbk').values;
bus_802_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_GTM.csv',
                         header=None,encoding='gbk').values;
bus_802_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_TMVD.csv',
                         header=None,encoding='gbk').values;
bus_802_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_KDEm.csv',
                         header=None,encoding='gbk').values;
bus_802_Mean=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_Mean.csv',
                         header=None,encoding='gbk').values;
bus_802_Median=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/802_Median.csv',
                         header=None,encoding='gbk').values;
bus_370_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_CATD.csv',
                         header=None,encoding='gbk').values;
bus_370_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_CRH.csv',
                         header=None,encoding='gbk').values;
bus_370_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_GTM.csv',
                         header=None,encoding='gbk').values;
bus_370_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_KDEm.csv',
                         header=None,encoding='gbk').values;
bus_370_Mean=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_Mean.csv',
                         header=None,encoding='gbk').values;
bus_370_Median=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_Median.csv',
                         header=None,encoding='gbk').values;
bus_370_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/370_TMVD.csv',
                         header=None,encoding='gbk').values;
bus_142_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_CATD.csv',
                         header=None,encoding='gbk').values;
bus_142_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_CRH.csv',
                         header=None,encoding='gbk').values;
bus_142_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_GTM.csv',
                         header=None,encoding='gbk').values;
bus_142_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_KDEm.csv',
                         header=None,encoding='gbk').values;
bus_142_Mean=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_Mean.csv',
                         header=None,encoding='gbk').values;
bus_142_Median=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_Median.csv',
                         header=None,encoding='gbk').values;
bus_142_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/142_TMVD.csv',
                         header=None,encoding='gbk').values;
bus_810_CATD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_CATD.csv',
                         header=None,encoding='gbk').values;
bus_810_CRH=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_CRH.csv',
                         header=None,encoding='gbk').values;
bus_810_GTM=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_GTM.csv',
                         header=None,encoding='gbk').values;
bus_810_KDEm=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_KDEm.csv',
                         header=None,encoding='gbk').values;
bus_810_Mean=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_Mean.csv',
                         header=None,encoding='gbk').values;
bus_810_Median=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_Median.csv',
                         header=None,encoding='gbk').values;
bus_810_TMVD=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/near_point/810_TMVD.csv',
                         header=None,encoding='gbk').values;



#truth
bus_109_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/109_truth.xlsx').values;
bus_370_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/293_truth.xlsx').values;
bus_142_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/142_truth.xlsx').values;
bus_802_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/802_truth.xlsx').values;
bus_810_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/810_truth.xlsx').values;

#caculate
dis_109_CATD=[];dis_109_CRH=[];dis_109_GTM=[];dis_109_KDEm=[];dis_109_Mean=[];dis_109_Median=[];dis_109_TMVD=[];
dis_370_CATD=[];dis_370_CRH=[];dis_370_GTM=[];dis_370_KDEm=[];dis_370_Mean=[];dis_370_Median=[];dis_370_TMVD=[];
dis_142_CATD=[];dis_142_CRH=[];dis_142_GTM=[];dis_142_KDEm=[];dis_142_Mean=[];dis_142_Median=[];dis_142_TMVD=[];
dis_802_CATD=[];dis_802_CRH=[];dis_802_GTM=[];dis_802_KDEm=[];dis_802_Mean=[];dis_802_Median=[];dis_802_TMVD=[];
dis_810_CATD=[];dis_810_CRH=[];dis_810_KDEm=[];dis_810_GTM=[];dis_810_Mean=[];dis_810_Median=[];dis_810_TMVD=[];
#109
#a=bus_109_truth[1,0]
for i in range(len(bus_109_CATD)):
    for j in range(len(bus_109_truth)):
        if(bus_109_CATD[i][0]==bus_109_truth[j][0]):
            dis_109_CATD.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,float(bus_109_CATD[i,2])*pow(10,-6),float(bus_109_CATD[i,1])*pow(10,-6)))
            break;
for i in range(len(bus_109_CRH)):
    for j in range(len(bus_109_truth)):
        if(bus_109_CRH[i,0]==bus_109_truth[j,0]):
            dis_109_CRH.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,bus_109_CRH[i,2]*pow(10,-6),bus_109_CRH[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_109_GTM)):
    for j in range(len(bus_109_truth)):
        if(bus_109_GTM[i,0]==bus_109_truth[j,0]):
            dis_109_GTM.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,bus_109_GTM[i,2]*pow(10,-6),bus_109_GTM[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_109_KDEm)):
    for j in range(len(bus_109_truth)):
        if(bus_109_KDEm[i,0]==bus_109_truth[j,0]):
            dis_109_KDEm.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,bus_109_KDEm[i,2]*pow(10,-6),bus_109_KDEm[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_109_Mean)):
    for j in range(len(bus_109_truth)):
        if(bus_109_Mean[i,0]==bus_109_truth[j,0]):
            dis_109_Mean.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,bus_109_Mean[i,2]*pow(10,-6),bus_109_Mean[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_109_Median)):
    for j in range(len(bus_109_truth)):
        if(bus_109_Median[i,0]==bus_109_truth[j,0]):
            dis_109_Median.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,bus_109_Median[i,2]*pow(10,-6),bus_109_Median[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_109_TMVD)):
    for j in range(len(bus_109_truth)):
        if(bus_109_TMVD[i,0]==bus_109_truth[j,0]):
            dis_109_TMVD.append(LatAndLonToDis(bus_109_truth[j,2],bus_109_truth[j,1]
                ,bus_109_TMVD[i,2]*pow(10,-6),bus_109_TMVD[i,1]*pow(10,-6)))
            break;
#370
for i in range(len(bus_370_CATD)):
    for j in range(len(bus_370_truth)):
        if(bus_370_CATD[i,0]==bus_370_truth[j,0]):
            dis_370_CATD.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_CATD[i,2]*pow(10,-6),bus_370_CATD[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_370_CRH)):
    for j in range(len(bus_370_truth)):
        if(bus_370_CRH[i,0]==bus_370_truth[j,0]):
            dis_370_CRH.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_CRH[i,2]*pow(10,-6),bus_370_CRH[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_370_GTM)):
    for j in range(len(bus_370_truth)):
        if(bus_370_GTM[i,0]==bus_370_truth[j,0]):
            dis_370_GTM.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_GTM[i,2]*pow(10,-6),bus_370_GTM[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_370_KDEm)):
    for j in range(len(bus_370_truth)):
        if(bus_370_KDEm[i,0]==bus_370_truth[j,0]):
            dis_370_KDEm.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_KDEm[i,2]*pow(10,-6),bus_370_KDEm[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_370_Mean)):
    for j in range(len(bus_370_truth)):
        if(bus_370_Mean[i,0]==bus_370_truth[j,0]):
            dis_370_Mean.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_Mean[i,2]*pow(10,-6),bus_370_Mean[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_370_Median)):
    for j in range(len(bus_370_truth)):
        if(bus_370_Median[i,0]==bus_370_truth[j,0]):
            dis_370_Median.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_Median[i,2]*pow(10,-6),bus_370_Median[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_370_TMVD)):
    for j in range(len(bus_370_truth)):
        if(bus_370_TMVD[i,0]==bus_370_truth[j,0]):
            dis_370_TMVD.append(LatAndLonToDis(bus_370_truth[j,2],bus_370_truth[j,1]
                ,bus_370_TMVD[i,2]*pow(10,-6),bus_370_TMVD[i,1]*pow(10,-6)))
            break;
#802
for i in range(len(bus_802_CATD)):
    for j in range(len(bus_802_truth)):
        if(bus_802_CATD[i,0]==bus_802_truth[j,0]):
            dis_802_CATD.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_CATD[i,2]*pow(10,-6),bus_802_CATD[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_802_CRH)):
    for j in range(len(bus_802_truth)):
        if(bus_802_CRH[i,0]==bus_802_truth[j,0]):
            dis_802_CRH.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_CRH[i,2]*pow(10,-6),bus_802_CRH[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_802_GTM)):
    for j in range(len(bus_802_truth)):
        if(bus_802_GTM[i,0]==bus_802_truth[j,0]):
            dis_802_GTM.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_GTM[i,2]*pow(10,-6),bus_802_GTM[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_802_KDEm)):
    for j in range(len(bus_802_truth)):
        if(bus_802_KDEm[i,0]==bus_802_truth[j,0]):
            dis_802_KDEm.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_KDEm[i,2]*pow(10,-6),bus_802_KDEm[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_802_Mean)):
    for j in range(len(bus_802_truth)):
        if(bus_802_Mean[i,0]==bus_802_truth[j,0]):
            dis_802_Mean.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_Mean[i,2]*pow(10,-6),bus_802_Mean[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_802_Median)):
    for j in range(len(bus_802_truth)):
        if(bus_802_Median[i,0]==bus_802_truth[j,0]):
            dis_802_Median.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_Median[i,2]*pow(10,-6),bus_802_Median[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_802_TMVD)):
    for j in range(len(bus_802_truth)):
        if(bus_802_TMVD[i,0]==bus_802_truth[j,0]):
            dis_802_TMVD.append(LatAndLonToDis(bus_802_truth[j,2],bus_802_truth[j,1]
                ,bus_802_TMVD[i,2]*pow(10,-6),bus_802_TMVD[i,1]*pow(10,-6)))
            break;

#142
for i in range(len(bus_142_CATD)):
    for j in range(len(bus_142_truth)):
        if(bus_142_CATD[i,0]==bus_142_truth[j,0]):
            dis_142_CATD.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_CATD[i,2]*pow(10,-6),bus_142_CATD[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_142_CRH)):
    for j in range(len(bus_142_truth)):
        if(bus_142_CRH[i,0]==bus_142_truth[j,0]):
            dis_142_CRH.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_CRH[i,2]*pow(10,-6),bus_142_CRH[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_142_GTM)):
    for j in range(len(bus_142_truth)):
        if(bus_142_GTM[i,0]==bus_142_truth[j,0]):
            dis_142_GTM.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_GTM[i,2]*pow(10,-6),bus_142_GTM[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_142_KDEm)):
    for j in range(len(bus_142_truth)):
        if(bus_142_KDEm[i,0]==bus_142_truth[j,0]):
            dis_142_KDEm.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_KDEm[i,2]*pow(10,-6),bus_142_KDEm[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_142_Mean)):
    for j in range(len(bus_142_truth)):
        if(bus_142_Mean[i,0]==bus_142_truth[j,0]):
            dis_142_Mean.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_Mean[i,2]*pow(10,-6),bus_142_Mean[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_142_Median)):
    for j in range(len(bus_142_truth)):
        if(bus_142_Median[i,0]==bus_142_truth[j,0]):
            dis_142_Median.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_Median[i,2]*pow(10,-6),bus_142_Median[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_142_TMVD)):
    for j in range(len(bus_142_truth)):
        if(bus_142_TMVD[i,0]==bus_142_truth[j,0]):
            dis_142_TMVD.append(LatAndLonToDis(bus_142_truth[j,2],bus_142_truth[j,1]
                ,bus_142_TMVD[i,2]*pow(10,-6),bus_142_TMVD[i,1]*pow(10,-6)))
            break;
#810
for i in range(len(bus_810_CATD)):
    for j in range(len(bus_810_truth)):
        if(bus_810_CATD[i,0]==bus_810_truth[j,0]):
            dis_810_CATD.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_CATD[i,2]*pow(10,-6),bus_810_CATD[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_810_CRH)):
    for j in range(len(bus_810_truth)):
        if(bus_810_CRH[i,0]==bus_810_truth[j,0]):
            dis_810_CRH.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_CRH[i,2]*pow(10,-6),bus_810_CRH[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_810_GTM)):
    for j in range(len(bus_810_truth)):
        if(bus_810_GTM[i,0]==bus_810_truth[j,0]):
            dis_810_GTM.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_GTM[i,2]*pow(10,-6),bus_810_GTM[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_810_KDEm)):
    for j in range(len(bus_810_truth)):
        if(bus_810_KDEm[i,0]==bus_810_truth[j,0]):
            dis_810_KDEm.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_KDEm[i,2]*pow(10,-6),bus_810_KDEm[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_810_Mean)):
    for j in range(len(bus_810_truth)):
        if(bus_810_Mean[i,0]==bus_810_truth[j,0]):
            dis_810_Mean.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_Mean[i,2]*pow(10,-6),bus_810_Mean[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_810_Median)):
    for j in range(len(bus_810_truth)):
        if(bus_810_Median[i,0]==bus_810_truth[j,0]):
            dis_810_Median.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_Median[i,2]*pow(10,-6),bus_810_Median[i,1]*pow(10,-6)))
            break;
for i in range(len(bus_810_TMVD)):
    for j in range(len(bus_810_truth)):
        if(bus_810_TMVD[i,0]==bus_810_truth[j,0]):
            dis_810_TMVD.append(LatAndLonToDis(bus_810_truth[j,2],bus_810_truth[j,1]
                ,bus_810_TMVD[i,2]*pow(10,-6),bus_810_TMVD[i,1]*pow(10,-6)))
            break;

min_109_of_TMVD=[];
min_370_of_TMVD=[];
min_142_of_TMVD=[];
min_810_of_TMVD=[];
min_802_of_TMVD=[];

for i in range(len(dis_109_CATD)):
    if(dis_109_TMVD[i]==min(dis_109_CATD[i],dis_109_TMVD[i],dis_109_CRH[i],dis_109_GTM[i]
            ,dis_109_KDEm[i],dis_109_Mean[i],dis_109_Median[i])):
        min_109_of_TMVD.append(i);

for i in range(len(dis_370_CATD)):
    if(dis_370_TMVD[i]==min(dis_370_CATD[i],dis_370_TMVD[i],dis_370_CRH[i],dis_370_GTM[i]
            ,dis_370_KDEm[i],dis_370_Mean[i],dis_370_Median[i])):
        min_370_of_TMVD.append(i);

for i in range(len(dis_142_CATD)):
    if(dis_142_TMVD[i]==min(dis_142_CATD[i],dis_142_TMVD[i],dis_142_CRH[i],dis_142_GTM[i]
            ,dis_142_KDEm[i],dis_142_Mean[i],dis_142_Median[i])):
        min_142_of_TMVD.append(i);

for i in range(len(dis_810_CATD)):
    if(dis_810_TMVD[i]==min(dis_810_CATD[i],dis_810_TMVD[i],dis_810_CRH[i],dis_810_GTM[i]
            ,dis_810_KDEm[i],dis_810_Mean[i],dis_810_Median[i])):
        min_810_of_TMVD.append(i);

for i in range(len(dis_802_CATD)):
    if(dis_802_TMVD[i]==min(dis_802_CATD[i],dis_802_TMVD[i],dis_802_CRH[i],dis_802_GTM[i]
            ,dis_802_KDEm[i],dis_802_Mean[i],dis_802_Median[i])):
        min_802_of_TMVD.append(i);


dis_bt_109_and_truth_CATD=np.zeros(shape=[len(min_109_of_TMVD),2]);
dis_bt_109_and_truth_CRH=np.zeros(shape=[len(min_109_of_TMVD),2]);
dis_bt_109_and_truth_GTM=np.zeros(shape=[len(min_109_of_TMVD),2]);
dis_bt_109_and_truth_KDEm=np.zeros(shape=[len(min_109_of_TMVD),2]);
dis_bt_109_and_truth_TMVD=np.zeros(shape=[len(min_109_of_TMVD),2]);
dis_bt_109_and_truth_Mean=np.zeros(shape=[len(min_109_of_TMVD),2]);
dis_bt_109_and_truth_Median=np.zeros(shape=[len(min_109_of_TMVD),2]);

for i in range(len(min_109_of_TMVD)):
    for j in range(len(bus_109_truth)):
        if(bus_109_CATD[min_109_of_TMVD[i],0]==bus_109_truth[j,0]):
            dis_bt_109_and_truth_CATD[i,0]=Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                           , bus_109_CATD[min_109_of_TMVD[i], 2] * pow(10, -6), bus_109_CATD[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_CATD[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                    , bus_109_CATD[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                    bus_109_CATD[min_109_of_TMVD[i], 1] * pow(10, -6));
        if (bus_109_CRH[min_109_of_TMVD[i], 0] == bus_109_truth[j, 0]):
            dis_bt_109_and_truth_CRH[i, 0] = Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_CRH[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_CRH[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_CRH[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_CRH[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_CRH[min_109_of_TMVD[i], 1] * pow(10, -6));
        if (bus_109_GTM[min_109_of_TMVD[i], 0] == bus_109_truth[j, 0]):
            dis_bt_109_and_truth_GTM[i, 0] = Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_GTM[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_GTM[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_GTM[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_GTM[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_GTM[min_109_of_TMVD[i], 1] * pow(10, -6));
        if (bus_109_KDEm[min_109_of_TMVD[i], 0] == bus_109_truth[j, 0]):
            dis_bt_109_and_truth_KDEm[i, 0] = Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_KDEm[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_KDEm[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_KDEm[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_KDEm[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_KDEm[min_109_of_TMVD[i], 1] * pow(10, -6));
        if (bus_109_TMVD[min_109_of_TMVD[i], 0] == bus_109_truth[j, 0]):
            dis_bt_109_and_truth_TMVD[i, 0] = Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_TMVD[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_TMVD[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_TMVD[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_TMVD[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_TMVD[min_109_of_TMVD[i], 1] * pow(10, -6));
        if (bus_109_Mean[min_109_of_TMVD[i], 0] == bus_109_truth[j, 0]):
            dis_bt_109_and_truth_Mean[i, 0] = Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_Mean[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_Mean[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_Mean[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_Mean[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_Mean[min_109_of_TMVD[i], 1] * pow(10, -6));
        if (bus_109_Median[min_109_of_TMVD[i], 0] == bus_109_truth[j, 0]):
            dis_bt_109_and_truth_Median[i, 0] = Latdis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_Median[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_Median[min_109_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_109_and_truth_Median[i, 1] = Londis(bus_109_truth[j, 2], bus_109_truth[j, 1]
                                                     , bus_109_Median[min_109_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_109_Median[min_109_of_TMVD[i], 1] * pow(10, -6));




dis_bt_142_and_truth_CATD=np.zeros(shape=[len(min_142_of_TMVD),2]);
dis_bt_142_and_truth_CRH=np.zeros(shape=[len(min_142_of_TMVD),2]);
dis_bt_142_and_truth_GTM=np.zeros(shape=[len(min_142_of_TMVD),2]);
dis_bt_142_and_truth_KDEm=np.zeros(shape=[len(min_142_of_TMVD),2]);
dis_bt_142_and_truth_TMVD=np.zeros(shape=[len(min_142_of_TMVD),2]);
dis_bt_142_and_truth_Mean=np.zeros(shape=[len(min_142_of_TMVD),2]);
dis_bt_142_and_truth_Median=np.zeros(shape=[len(min_142_of_TMVD),2]);




for i in range(len(min_142_of_TMVD)):
    for j in range(len(bus_142_truth)):
        if(bus_142_CATD[min_142_of_TMVD[i],0]==bus_142_truth[j,0]):
            dis_bt_142_and_truth_CATD[i,0]=Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                           , bus_142_CATD[min_142_of_TMVD[i], 2] * pow(10, -6), bus_142_CATD[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_CATD[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                    , bus_142_CATD[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                    bus_142_CATD[min_142_of_TMVD[i], 1] * pow(10, -6));
        if (bus_142_CRH[min_142_of_TMVD[i], 0] == bus_142_truth[j, 0]):
            dis_bt_142_and_truth_CRH[i, 0] = Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_CRH[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_CRH[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_CRH[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_CRH[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_CRH[min_142_of_TMVD[i], 1] * pow(10, -6));
        if (bus_142_GTM[min_142_of_TMVD[i], 0] == bus_142_truth[j, 0]):
            dis_bt_142_and_truth_GTM[i, 0] = Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_GTM[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_GTM[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_GTM[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_GTM[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_GTM[min_142_of_TMVD[i], 1] * pow(10, -6));
        if (bus_142_KDEm[min_142_of_TMVD[i], 0] == bus_142_truth[j, 0]):
            dis_bt_142_and_truth_KDEm[i, 0] = Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_KDEm[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_KDEm[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_KDEm[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_KDEm[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_KDEm[min_142_of_TMVD[i], 1] * pow(10, -6));
        if (bus_142_TMVD[min_142_of_TMVD[i], 0] == bus_142_truth[j, 0]):
            dis_bt_142_and_truth_TMVD[i, 0] = Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_TMVD[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_TMVD[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_TMVD[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_TMVD[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_TMVD[min_142_of_TMVD[i], 1] * pow(10, -6));
        if (bus_142_Mean[min_142_of_TMVD[i], 0] == bus_142_truth[j, 0]):
            dis_bt_142_and_truth_Mean[i, 0] = Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_Mean[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_Mean[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_Mean[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_Mean[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_Mean[min_142_of_TMVD[i], 1] * pow(10, -6));
        if (bus_142_Median[min_142_of_TMVD[i], 0] == bus_142_truth[j, 0]):
            dis_bt_142_and_truth_Median[i, 0] = Latdis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_Median[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_Median[min_142_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_142_and_truth_Median[i, 1] = Londis(bus_142_truth[j, 2], bus_142_truth[j, 1]
                                                     , bus_142_Median[min_142_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_142_Median[min_142_of_TMVD[i], 1] * pow(10, -6));

dis_bt_370_and_truth_CATD=np.zeros(shape=[len(min_370_of_TMVD),2]);
dis_bt_370_and_truth_CRH=np.zeros(shape=[len(min_370_of_TMVD),2]);
dis_bt_370_and_truth_GTM=np.zeros(shape=[len(min_370_of_TMVD),2]);
dis_bt_370_and_truth_KDEm=np.zeros(shape=[len(min_370_of_TMVD),2]);
dis_bt_370_and_truth_TMVD=np.zeros(shape=[len(min_370_of_TMVD),2]);
dis_bt_370_and_truth_Mean=np.zeros(shape=[len(min_370_of_TMVD),2]);
dis_bt_370_and_truth_Median=np.zeros(shape=[len(min_370_of_TMVD),2]);

for i in range(len(min_370_of_TMVD)):
    for j in range(len(bus_370_truth)):
        if(bus_370_CATD[min_370_of_TMVD[i],0]==bus_370_truth[j,0]):
            dis_bt_370_and_truth_CATD[i,0]=Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                           , bus_370_CATD[min_370_of_TMVD[i], 2] * pow(10, -6), bus_370_CATD[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_CATD[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                    , bus_370_CATD[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                    bus_370_CATD[min_370_of_TMVD[i], 1] * pow(10, -6));
        if (bus_370_CRH[min_370_of_TMVD[i], 0] == bus_370_truth[j, 0]):
            dis_bt_370_and_truth_CRH[i, 0] = Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_CRH[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_CRH[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_CRH[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_CRH[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_CRH[min_370_of_TMVD[i], 1] * pow(10, -6));
        if (bus_370_GTM[min_370_of_TMVD[i], 0] == bus_370_truth[j, 0]):
            dis_bt_370_and_truth_GTM[i, 0] = Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_GTM[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_GTM[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_GTM[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_GTM[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_GTM[min_370_of_TMVD[i], 1] * pow(10, -6));
        if (bus_370_KDEm[min_370_of_TMVD[i], 0] == bus_370_truth[j, 0]):
            dis_bt_370_and_truth_KDEm[i, 0] = Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_KDEm[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_KDEm[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_KDEm[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_KDEm[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_KDEm[min_370_of_TMVD[i], 1] * pow(10, -6));
        if (bus_370_TMVD[min_370_of_TMVD[i], 0] == bus_370_truth[j, 0]):
            dis_bt_370_and_truth_TMVD[i, 0] = Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_TMVD[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_TMVD[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_TMVD[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_TMVD[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_TMVD[min_370_of_TMVD[i], 1] * pow(10, -6));
        if (bus_370_Mean[min_370_of_TMVD[i], 0] == bus_370_truth[j, 0]):
            dis_bt_370_and_truth_Mean[i, 0] = Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_Mean[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_Mean[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_Mean[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_Mean[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_Mean[min_370_of_TMVD[i], 1] * pow(10, -6));
        if (bus_370_Median[min_370_of_TMVD[i], 0] == bus_370_truth[j, 0]):
            dis_bt_370_and_truth_Median[i, 0] = Latdis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_Median[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_Median[min_370_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_370_and_truth_Median[i, 1] = Londis(bus_370_truth[j, 2], bus_370_truth[j, 1]
                                                     , bus_370_Median[min_370_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_370_Median[min_370_of_TMVD[i], 1] * pow(10, -6));

dis_bt_802_and_truth_CATD=np.zeros(shape=[len(min_802_of_TMVD),2]);
dis_bt_802_and_truth_CRH=np.zeros(shape=[len(min_802_of_TMVD),2]);
dis_bt_802_and_truth_GTM=np.zeros(shape=[len(min_802_of_TMVD),2]);
dis_bt_802_and_truth_KDEm=np.zeros(shape=[len(min_802_of_TMVD),2]);
dis_bt_802_and_truth_TMVD=np.zeros(shape=[len(min_802_of_TMVD),2]);
dis_bt_802_and_truth_Mean=np.zeros(shape=[len(min_802_of_TMVD),2]);
dis_bt_802_and_truth_Median=np.zeros(shape=[len(min_802_of_TMVD),2]);

for i in range(len(min_802_of_TMVD)):
    for j in range(len(bus_802_truth)):
        if(bus_802_CATD[min_802_of_TMVD[i],0]==bus_802_truth[j,0]):
            dis_bt_802_and_truth_CATD[i,0]=Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                           , bus_802_CATD[min_802_of_TMVD[i], 2] * pow(10, -6), bus_802_CATD[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_CATD[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                    , bus_802_CATD[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                    bus_802_CATD[min_802_of_TMVD[i], 1] * pow(10, -6));
        if (bus_802_CRH[min_802_of_TMVD[i], 0] == bus_802_truth[j, 0]):
            dis_bt_802_and_truth_CRH[i, 0] = Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_CRH[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_CRH[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_CRH[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_CRH[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_CRH[min_802_of_TMVD[i], 1] * pow(10, -6));
        if (bus_802_GTM[min_802_of_TMVD[i], 0] == bus_802_truth[j, 0]):
            dis_bt_802_and_truth_GTM[i, 0] = Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_GTM[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_GTM[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_GTM[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_GTM[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_GTM[min_802_of_TMVD[i], 1] * pow(10, -6));
        if (bus_802_KDEm[min_802_of_TMVD[i], 0] == bus_802_truth[j, 0]):
            dis_bt_802_and_truth_KDEm[i, 0] = Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_KDEm[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_KDEm[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_KDEm[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_KDEm[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_KDEm[min_802_of_TMVD[i], 1] * pow(10, -6));
        if (bus_802_TMVD[min_802_of_TMVD[i], 0] == bus_802_truth[j, 0]):
            dis_bt_802_and_truth_TMVD[i, 0] = Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_TMVD[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_TMVD[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_TMVD[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_TMVD[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_TMVD[min_802_of_TMVD[i], 1] * pow(10, -6));
        if (bus_802_Mean[min_802_of_TMVD[i], 0] == bus_802_truth[j, 0]):
            dis_bt_802_and_truth_Mean[i, 0] = Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_Mean[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_Mean[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_Mean[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_Mean[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_Mean[min_802_of_TMVD[i], 1] * pow(10, -6));
        if (bus_802_Median[min_802_of_TMVD[i], 0] == bus_802_truth[j, 0]):
            dis_bt_802_and_truth_Median[i, 0] = Latdis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_Median[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_Median[min_802_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_802_and_truth_Median[i, 1] = Londis(bus_802_truth[j, 2], bus_802_truth[j, 1]
                                                     , bus_802_Median[min_802_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_802_Median[min_802_of_TMVD[i], 1] * pow(10, -6));

dis_bt_810_and_truth_CATD=np.zeros(shape=[len(min_810_of_TMVD),2]);
dis_bt_810_and_truth_CRH=np.zeros(shape=[len(min_810_of_TMVD),2]);
dis_bt_810_and_truth_GTM=np.zeros(shape=[len(min_810_of_TMVD),2]);
dis_bt_810_and_truth_KDEm=np.zeros(shape=[len(min_810_of_TMVD),2]);
dis_bt_810_and_truth_TMVD=np.zeros(shape=[len(min_810_of_TMVD),2]);
dis_bt_810_and_truth_Mean=np.zeros(shape=[len(min_810_of_TMVD),2]);
dis_bt_810_and_truth_Median=np.zeros(shape=[len(min_810_of_TMVD),2]);

for i in range(len(min_810_of_TMVD)):
    for j in range(len(bus_810_truth)):
        if(bus_810_CATD[min_810_of_TMVD[i],0]==bus_810_truth[j,0]):
            dis_bt_810_and_truth_CATD[i,0]=Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                           , bus_810_CATD[min_810_of_TMVD[i], 2] * pow(10, -6), bus_810_CATD[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_CATD[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                    , bus_810_CATD[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                    bus_810_CATD[min_810_of_TMVD[i], 1] * pow(10, -6));
        if (bus_810_CRH[min_810_of_TMVD[i], 0] == bus_810_truth[j, 0]):
            dis_bt_810_and_truth_CRH[i, 0] = Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_CRH[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_CRH[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_CRH[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_CRH[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_CRH[min_810_of_TMVD[i], 1] * pow(10, -6));
        if (bus_810_GTM[min_810_of_TMVD[i], 0] == bus_810_truth[j, 0]):
            dis_bt_810_and_truth_GTM[i, 0] = Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_GTM[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_GTM[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_GTM[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_GTM[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_GTM[min_810_of_TMVD[i], 1] * pow(10, -6));
        if (bus_810_KDEm[min_810_of_TMVD[i], 0] == bus_810_truth[j, 0]):
            dis_bt_810_and_truth_KDEm[i, 0] = Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_KDEm[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_KDEm[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_KDEm[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_KDEm[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_KDEm[min_810_of_TMVD[i], 1] * pow(10, -6));
        if (bus_810_TMVD[min_810_of_TMVD[i], 0] == bus_810_truth[j, 0]):
            dis_bt_810_and_truth_TMVD[i, 0] = Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_TMVD[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_TMVD[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_TMVD[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_TMVD[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_TMVD[min_810_of_TMVD[i], 1] * pow(10, -6));
        if (bus_810_Mean[min_810_of_TMVD[i], 0] == bus_810_truth[j, 0]):
            dis_bt_810_and_truth_Mean[i, 0] = Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_Mean[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_Mean[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_Mean[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_Mean[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_Mean[min_810_of_TMVD[i], 1] * pow(10, -6));
        if (bus_810_Median[min_810_of_TMVD[i], 0] == bus_810_truth[j, 0]):
            dis_bt_810_and_truth_Median[i, 0] = Latdis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_Median[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_Median[min_810_of_TMVD[i], 1] * pow(10, -6));
            dis_bt_810_and_truth_Median[i, 1] = Londis(bus_810_truth[j, 2], bus_810_truth[j, 1]
                                                     , bus_810_Median[min_810_of_TMVD[i], 2] * pow(10, -6),
                                                     bus_810_Median[min_810_of_TMVD[i], 1] * pow(10, -6));

#在最优点的平均距离误差
mean_of_TMVD_dis=0;
mean_of_CATD_dis=0;
mean_of_CRH_dis=0;
mean_of_GTM_dis=0;
mean_of_KDEm_dis=0;
mean_of_Mean_dis=0;
mean_of_Median_dis=0;
count_GTM=0;
#mean_of_TMVD_dis
for i in min_109_of_TMVD:
    mean_of_TMVD_dis+=dis_109_TMVD[i];
    mean_of_CATD_dis+=dis_109_CATD[i];
    mean_of_CRH_dis+=dis_109_CRH[i];
    if(dis_109_GTM[i]<300):
        mean_of_GTM_dis+=dis_109_GTM[i];
        count_GTM+=1;
    mean_of_KDEm_dis+=dis_109_KDEm[i];
    mean_of_Mean_dis+=dis_109_Mean[i];
    mean_of_Median_dis+=dis_109_Median[i];

for i in min_142_of_TMVD:
    mean_of_TMVD_dis += dis_142_TMVD[i];
    mean_of_CATD_dis += dis_142_CATD[i];
    mean_of_CRH_dis += dis_142_CRH[i];
    if (dis_142_GTM[i] < 300):
        mean_of_GTM_dis += dis_142_GTM[i];
        count_GTM += 1;
    mean_of_KDEm_dis += dis_142_KDEm[i];
    mean_of_Mean_dis += dis_142_Mean[i];
    mean_of_Median_dis += dis_142_Median[i];

for i in min_370_of_TMVD:
    mean_of_TMVD_dis += dis_370_TMVD[i];
    mean_of_CATD_dis += dis_370_CATD[i];
    mean_of_CRH_dis += dis_370_CRH[i];
    if (dis_370_GTM[i] < 300):
        mean_of_GTM_dis += dis_370_GTM[i];
        count_GTM += 1;
    mean_of_KDEm_dis += dis_370_KDEm[i];
    mean_of_Mean_dis += dis_370_Mean[i];
    mean_of_Median_dis += dis_370_Median[i];

for i in min_802_of_TMVD:
    mean_of_TMVD_dis += dis_802_TMVD[i];
    mean_of_CATD_dis += dis_802_CATD[i];
    mean_of_CRH_dis += dis_802_CRH[i];
    if (dis_802_GTM[i] < 300):
        mean_of_GTM_dis += dis_802_GTM[i];
        count_GTM += 1;
    mean_of_KDEm_dis += dis_802_KDEm[i];
    mean_of_Mean_dis += dis_802_Mean[i];
    mean_of_Median_dis += dis_802_Median[i];

for i in min_810_of_TMVD:
    mean_of_TMVD_dis += dis_810_TMVD[i];
    mean_of_CATD_dis += dis_810_CATD[i];
    mean_of_CRH_dis += dis_810_CRH[i];
    if (dis_810_GTM[i] < 300):
        mean_of_GTM_dis += dis_810_GTM[i];
        count_GTM += 1;
    mean_of_KDEm_dis += dis_810_KDEm[i];
    mean_of_Mean_dis += dis_810_Mean[i];
    mean_of_Median_dis += dis_810_Median[i];
mean_of_TMVD_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
                   +len(min_802_of_TMVD)+len(min_810_of_TMVD));
mean_of_CATD_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
                   +len(min_802_of_TMVD)+len(min_810_of_TMVD));
mean_of_CRH_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
                   +len(min_802_of_TMVD)+len(min_810_of_TMVD));
mean_of_GTM_dis /=count_GTM;
# mean_of_GTM_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
#                    +len(min_802_of_TMVD)+len(min_810_of_TMVD));
mean_of_KDEm_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
                   +len(min_802_of_TMVD)+len(min_810_of_TMVD));
mean_of_Mean_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
                   +len(min_802_of_TMVD)+len(min_810_of_TMVD));
mean_of_Median_dis/=(len(min_109_of_TMVD)+len(min_142_of_TMVD)+len(min_370_of_TMVD)
                   +len(min_802_of_TMVD)+len(min_810_of_TMVD));





#统计接收率
count_less_of_10_CATD=0;
count_less_of_10_CRH=0;
count_less_of_10_GTM=0;
count_less_of_10_KDEm=0;
count_less_of_10_TMVD=0;
count_less_of_10_Mean=0;
count_less_of_10_Median=0;

for i in min_142_of_TMVD:
    if(dis_142_TMVD[i]<=30):
        count_less_of_10_TMVD+=1;
    if (dis_142_CATD[i] <= 30):
        count_less_of_10_CATD += 1;
    if (dis_142_CRH[i] <= 30):
        count_less_of_10_CRH += 1;
    if (dis_142_GTM[i] <= 30):
        count_less_of_10_GTM += 1;
    if (dis_142_KDEm[i] <= 30):
        count_less_of_10_KDEm += 1;
    if (dis_142_Mean[i] <= 30):
        count_less_of_10_Mean += 1;
    if (dis_142_Median[i] <= 30):
        count_less_of_10_Median += 1;

for i in min_370_of_TMVD:
    if(dis_370_TMVD[i]<=30):
        count_less_of_10_TMVD+=1;
    if (dis_370_CATD[i] <= 30):
        count_less_of_10_CATD += 1;
    if (dis_370_CRH[i] <= 30):
        count_less_of_10_CRH += 1;
    if (dis_370_GTM[i] <= 30):
        count_less_of_10_GTM += 1;
    if (dis_370_KDEm[i] <= 30):
        count_less_of_10_KDEm += 1;
    if (dis_370_Mean[i] <= 30):
        count_less_of_10_Mean += 1;
    if (dis_370_Median[i] <= 30):
        count_less_of_10_Median += 1;

for i in min_802_of_TMVD:
    if(dis_802_TMVD[i]<=30):
        count_less_of_10_TMVD+=1;
    if (dis_802_CATD[i] <= 30):
        count_less_of_10_CATD += 1;
    if (dis_802_CRH[i] <= 30):
        count_less_of_10_CRH += 1;
    if (dis_802_GTM[i] <= 30):
        count_less_of_10_GTM += 1;
    if (dis_802_KDEm[i] <= 30):
        count_less_of_10_KDEm += 1;
    if (dis_802_Mean[i] <= 30):
        count_less_of_10_Mean += 1;
    if (dis_802_Median[i] <= 30):
        count_less_of_10_Median += 1;

for i in min_810_of_TMVD:
    if(dis_810_TMVD[i]<=30):
        count_less_of_10_TMVD+=1;
    if (dis_810_CATD[i] <= 30):
        count_less_of_10_CATD += 1;
    if (dis_810_CRH[i] <= 30):
        count_less_of_10_CRH += 1;
    if (dis_810_GTM[i] <= 30):
        count_less_of_10_GTM += 1;
    if (dis_810_KDEm[i] <= 30):
        count_less_of_10_KDEm += 1;
    if (dis_810_Mean[i] <= 30):
        count_less_of_10_Mean += 1;
    if (dis_810_Median[i] <= 30):
        count_less_of_10_Median += 1;

count_less_of_10_CATD/=34;
count_less_of_10_CRH/=34;
count_less_of_10_GTM/=34;
count_less_of_10_KDEm/=34;
count_less_of_10_TMVD/=34;
count_less_of_10_Mean/=34;
count_less_of_10_Median/=34;

