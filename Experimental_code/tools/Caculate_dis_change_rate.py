import math

import pandas as pd

import Changable_learn_rate as exp
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


#data
Trans_142_Data=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/142_Trans.csv',
                         header=None,encoding='gbk').values;
Trans_370_Data=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/370_Trans.csv',
                         header=None,encoding='gbk').values;
Trans_802_Data=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/802_Trans.csv',
                         header=None,encoding='gbk').values;
Trans_810_Data=pd.read_csv('C:/Users/zhaol/Desktop/赵凌子/bus_station_with_subway_data/810_Trans.csv',
                         header=None,encoding='gbk').values;
#truth
bus_370_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/293_truth.xlsx').values;
bus_142_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/142_truth.xlsx').values;
bus_802_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/802_truth.xlsx').values;
bus_810_truth=pd.read_excel('C:/Users/zhaol/Desktop/赵凌子/translation data/truth_line/810_truth.xlsx').values;

#min of station in TMVD
min_142_of_TMVD=[0,7];
min_370_of_TMVD=[9,10,14];
min_802_of_TMVD=[3,5,8,10,11,12,15];
min_810_of_TMVD=[0,1,2,5,6,7,10,15,16,18,20];
#相关站点
bus_station_with_subway_142=['蓉园路口','洪西村','芙蓉区卫计局','省血液中心','朝阳村','马栏山','月湖公园',
                            '机电职院西','荣盛花语城体育公园'];
bus_station_with_subway_802=['远大路口','万家丽广场','芙蓉区政府','石坝路口','中城丽景香山',
                            '新屋里','湘府中学','大托铺','陶家山','市交通运输局',
                            '高桥大市场东','长沙大道口','曲塘路口','豆花塘','湖南联通',
                            '师家老屋'];
bus_station_with_subway_810=['甘家老屋','马栏山','朝阳村','省血液中心','火炬村','省老干所',
                            '马王堆医院','马王堆汽配大市场','远大路口','万家丽广场','芙蓉区政府',
                            '市交通运输局','高桥大市场东','长沙大道口','石坝路口','劳动东路口',
                            '中城丽景香山','曲塘路口','豆花塘','湖南联通','煤田地质局','省环保厅',
                            '唐湘电器市场'];
bus_station_with_subway_370=['长郡中学','侯家塘','侯家塘南','黄土岭','涂家冲','麻园塘',
                            '浦沅','竹塘路口','莲花山','林大路芙蓉路口','环保大道芙蓉南路口',
                            '侯家塘北','板塘村','天际岭隧道北','天际岭隧道南'];



Mean_error_of_changable_rate=[];
Reception_rate_of_changable_rate=[];
#change rate
for rate in range(5,16,1):
    truth_142_TMVD=exp.CATD(Trans_142_Data,50,rate*0.01);
    truth_370_TMVD = exp.CATD(Trans_370_Data, 50, rate*0.01);
    truth_802_TMVD = exp.CATD(Trans_802_Data, 50, rate*0.01);
    truth_810_TMVD = exp.CATD(Trans_810_Data, 50, rate*0.01);
    count_error=0;
    count_received=0;

    for i in min_142_of_TMVD:
        for j in range(len(truth_142_TMVD)):
            if(truth_142_TMVD[j,0]==bus_station_with_subway_142[i]):
                temp_j=j;
                break;
        for k in range(len(bus_142_truth)):
            if (bus_142_truth[k, 0] == bus_station_with_subway_142[i]):
                temp_k = k;
                break;

        count_error+=LatAndLonToDis(bus_142_truth[temp_k, 2], bus_142_truth[temp_k, 1]
                                                   , truth_142_TMVD[temp_j, 2] * pow(10, -6),
                                                   truth_142_TMVD[temp_j, 1] * pow(10, -6));
        if(LatAndLonToDis(bus_142_truth[temp_k, 2], bus_142_truth[temp_k, 1]
                                                   , truth_142_TMVD[temp_j, 2] * pow(10, -6),
                                                   truth_142_TMVD[temp_j, 1] * pow(10, -6))<=30):
            count_received+=1;

    for i in min_370_of_TMVD:
        for j in range(len(truth_370_TMVD)):
            if (truth_370_TMVD[j, 0] == bus_station_with_subway_370[i]):
                temp_j = j;
                break;
        for k in range(len(bus_370_truth)):
            if (bus_370_truth[k, 0] == bus_station_with_subway_370[i]):
                temp_k = k;
                break;

        count_error += LatAndLonToDis(bus_370_truth[temp_k, 2], bus_370_truth[temp_k, 1]
                                      , truth_370_TMVD[temp_j, 2] * pow(10, -6),
                                      truth_370_TMVD[temp_j, 1] * pow(10, -6));
        if (LatAndLonToDis(bus_370_truth[temp_k, 2], bus_370_truth[temp_k, 1]
                                      , truth_370_TMVD[temp_j, 2] * pow(10, -6),
                                      truth_370_TMVD[temp_j, 1] * pow(10, -6)) <=30):
            count_received += 1;

    for i in min_802_of_TMVD:
        for j in range(len(truth_802_TMVD)):
            if (truth_802_TMVD[j, 0] == bus_station_with_subway_802[i]):
                temp_j = j;
                break;
        for k in range(len(bus_802_truth)):
            if (bus_802_truth[k, 0] == bus_station_with_subway_802[i]):
                temp_k = k;
                break;

        count_error += LatAndLonToDis(bus_802_truth[temp_k, 2], bus_802_truth[temp_k, 1]
                                      , truth_802_TMVD[temp_j, 2] * pow(10, -6),
                                      truth_802_TMVD[temp_j, 1] * pow(10, -6));
        if (LatAndLonToDis(bus_802_truth[temp_k, 2], bus_802_truth[temp_k, 1]
                                      , truth_802_TMVD[temp_j, 2] * pow(10, -6),
                                      truth_802_TMVD[temp_j, 1] * pow(10, -6)) <=30):
            count_received += 1;

    for i in min_810_of_TMVD:
        for j in range(len(truth_810_TMVD)):
            if (truth_810_TMVD[j, 0] == bus_station_with_subway_810[i]):
                temp_j = j;
                break;
        for k in range(len(bus_810_truth)):
            if (bus_810_truth[k, 0] == bus_station_with_subway_810[i]):
                temp_k = k;
                break;

        count_error += LatAndLonToDis(bus_810_truth[temp_k, 2], bus_810_truth[temp_k, 1]
                                      , truth_810_TMVD[temp_j, 2] * pow(10, -6),
                                      truth_810_TMVD[temp_j, 1] * pow(10, -6));
        if (LatAndLonToDis(bus_810_truth[temp_k, 2], bus_810_truth[temp_k, 1]
                                      , truth_810_TMVD[temp_j, 2] * pow(10, -6),
                                      truth_810_TMVD[temp_j, 1] * pow(10, -6)) <=30):
            count_received += 1;

    Mean_error_of_changable_rate.append(count_error/23);
    Reception_rate_of_changable_rate.append(count_received/23);

with open('C:/Users/zhaol/Desktop/赵凌子/trans Experience Data/Mean_error_of_changable_rate.csv','w+') as ft:
    for i in range(len(Mean_error_of_changable_rate)):
        ft.write(str(Mean_error_of_changable_rate[i])+',');

with open('C:/Users/zhaol/Desktop/赵凌子/trans Experience Data/Reception_rate_of_changable_rate.csv','w+') as ft:
    for i in range(len(Reception_rate_of_changable_rate)):
        ft.write(str(Reception_rate_of_changable_rate[i])+',');