import random

import numpy as np
import pandas as pd

import Latitude
import Longitude
import CRH1 as crh
import CATD1 as catd
import CBS as cbs
import KDEm1 as kdem
import GTM1 as gtm
import Caculate1 as caculat
import matplotlib.pyplot as plt
import numpy.linalg as la
import Mean1 as mean
import Median1 as median
import xlsxwriter
import math


# GPS_noise=np.random.normal(loc=100.0, scale=1.0, size=None)#loc:均值 scale:方差的正太分布随机数0.00001度在地球表面任意地方对应的地球表面距离都是大约1米稍多
df1=pd.read_csv('translation_data/Bus_data_06/sumoTrace.csv')
Uni_Bus_ID = list(df1['1'].astype(str).unique());
Uni_Bus_ID.sort();
v1=df1.values;

df2=pd.read_csv('translation_data/truth_line/sumo_bus_loc.csv')
v2=df2.values;
Trans=np.array([np.array([0,'0',0.0,0.0]) for i in range(v2.__len__()*Uni_Bus_ID.__len__())]);#保存数据
#Trans=[0,'0',0.0,0.0];
m=0;


test= Uni_Bus_ID[0]
df3 = df1.loc[df1['1'] == Uni_Bus_ID[0]];

for i in range(len(Uni_Bus_ID)):#对每一辆的公交车进行处理
    df3 = df1.loc[df1['1'] == Uni_Bus_ID[i]];
    v3=df3.values;
    v3 = v3[v3[:, 0].argsort()];
    n = 0;

    while (n < v3.__len__()):
        if (v3[n][3] == 0 or v3[n][4] == 0):
            v3 = np.delete(v3, n, axis=0);
        else:
            #v3[n][5]+=12800;
            #10是1m噪声random.randint(0,20)
            v3[n][3] = v3[n][3]*pow(10,6)#GPS_noise=np.random.normal(loc=100.0, scale=1.0, size=None)#loc:均值 scale:方差的正太分布随机数0.00001度在地球表面任意地方对应的地球表面距离都是大约1米稍多
            v3[n][4] = v3[n][4]*pow(10,6)
            v3[n][3] += 12200
            v3[n][4] += 2410
            n = n+ 1;

    for j in range(v2.__len__()):
        # 记录公交车站点的经纬度
        lon1=v2[j][2];
        lat1=v2[j][3];
        min_dis=600;#附近 600m

        for k in range(v3.__len__()):
            # 转化经纬度
            lon2=v3[k][3]*pow(10,-6)
            lat2=v3[k][4]*pow(10,-6)
            # 计算公交当前位置与公交站点的距离
            a=Latitude.dis(lat1,lon1,lat2,lon2);
            b=Longitude.dis(lat1,lon1,lat2,lon2);
            dis=math.sqrt(a**2+b**2)
            print(dis)
            # dis=math.sqrt((lon1-lon2)**2+(lat1-lat2)**2);

            if(dis<=5):
                GPS_noise = np.random.normal(loc=30.0, scale=1.0, size=None)
                # 如果距离<=10米
                Trans[m][0]=str(Uni_Bus_ID[i]);
                # print(Trans[m][0])
                Trans[m][1]=str(v2[j][1]);
                # print(Trans[m][1])
                Trans[m][2]=round(lon2*pow(10,6) );
                Trans[m][3]=round(lat2*pow(10,6) +GPS_noise);
                m=m+1;
                break;
            else:
                GPS_noise = np.random.normal(loc=50.0, scale=1.0, size=None)
                if(dis<min_dis):
                    min_dis=dis;
                    Trans[m][0] = Uni_Bus_ID[i];
                    Trans[m][1] = str(v2[j][1]);
                    Trans[m][2] = round(lon2*pow(10,6) +GPS_noise)
                    Trans[m][3] = round(lat2*pow(10,6) )
            if(k>=v3.__len__()-1):
                m=m+1;
Data=[]
for i in range(0,Trans.shape[0]-1):
    if (Trans[i][0] != "0" ):
        Data.append(Trans[i])
Data=np.array(Data)
Data = Data[Data[:,1].argsort()];


truth_and_weight_CBS=cbs.CBS(Data, 3);
truth_and_weight_CRH=crh.CRH(Data,3);
truth_and_weight_CATD=catd.CATD(Data,3);
truth_and_weight_GTM=gtm.CTM(Data,3);
truth_and_weight_KDEm=kdem.KDEm(Data,3);
truth_and_weight_MEAN=mean.Mean(Data,3);
truth_and_weight_MEDIAN=median.Medain(Data,3);

# print("CRH_mae={}".format(truth_and_weight_CBS));
# print("CATD_mae={}".format(truth_and_weight_CATD));
# print("GTM_mae={}".format(truth_and_weight_GTM));
# print("KDEm_mae={}".format(truth_and_weight_KDEm));
# print("EXP_mae={}".format(truth_and_weight_CBS));
# print("MEAN_mae={}".format(truth_and_weight_MEAN));
# print("MEDIAN_mae={}".format(truth_and_weight_MEDIAN));




CRH_mae=caculat.caculat(truth_and_weight_CRH,v2);
CATD_mae=caculat.caculat(truth_and_weight_CATD,v2);
GTM_mae=caculat.caculat(truth_and_weight_GTM,v2);
KDEm_mae=caculat.caculat(truth_and_weight_KDEm,v2);
EXP_mae=caculat.caculat(truth_and_weight_CBS,v2);
MEAN_mae=caculat.caculat(truth_and_weight_MEAN,v2);
MEDIAN_mae=caculat.caculat(truth_and_weight_MEDIAN,v2);







# print(v2[1][0])
print("CRH_mae={}".format(CRH_mae));
print("CATD_mae={}".format(CATD_mae));
print("GTM_mae={}".format(GTM_mae));
print("KDEm_mae={}".format(KDEm_mae));
print("CBS_mae={}".format(EXP_mae));
print("MEAN_mae={}".format(MEAN_mae));
print("MEDIAN_mae={}".format(MEDIAN_mae));

with open('box.csv','a+') as f:
    f.write(str(CRH_mae))
    f.write(',')
    f.write(str(CATD_mae))
    f.write(',')
    f.write(str(GTM_mae))
    f.write(',')
    f.write(str(KDEm_mae))
    f.write(',')
    f.write(str(EXP_mae))
    f.write(',')
    f.write(str(MEAN_mae))
    f.write(',')
    f.write(str(MEDIAN_mae))
    f.write(',')
    f.write('\n')