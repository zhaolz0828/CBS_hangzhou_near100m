import math

import CATD1 as catd
import CRH1 as crh
import CBS as exp
import GTM1 as gtm
import KDEm1 as kdem
import Mean1 as mean
import Median1 as median
import numpy as np
import pandas as pd

import Caculate1 as caculat
import Latitude
import Longitude


def take2(elem):
    return elem[1];

df1 = pd.DataFrame(pd.read_excel('../translation_data/Bus_data_06/_293.xlsx'));
Uni_Bus_ID = list(df1['BUS_ID'].unique());
Uni_Bus_ID.sort();
v1=df1.values;
df2=pd.DataFrame(pd.read_excel('../translation_data/truth_line/293_truth.xlsx'));
v2=df2.values;
Trans=np.array([np.array([0,'0',0.0,0.0]) for i in range(v2.__len__()*21)]);#保存数据
#Trans=[0,'0',0.0,0.0];
m=0;

for i in range(len(Uni_Bus_ID)):
    if(Uni_Bus_ID[i]==222163 or Uni_Bus_ID[i]==222168 or Uni_Bus_ID[i]==222176 or Uni_Bus_ID[i]==222178 or Uni_Bus_ID[i]==222179 or Uni_Bus_ID[i]==222187):
        continue;
    df3 = df1.loc[df1['BUS_ID'] == Uni_Bus_ID[i]];
    v3=df3.values;
    v3 = v3[v3[:, 1].argsort()];
    n = 0;
    #平移数据
    while (n < v3.__len__()):
        if (v3[n][2] == 0 or v3[n][3] == 0):
            v3 = np.delete(v3, n, axis=0);
        else:
            #v3[n][5]+=12800;
            v3[n][2]+=12000;
            #v3[n][3] += 3025; #对应10
            v3[n][3] +=3015;  #对应30
            n = n+ 1;
    #计算数据输入值
    for j in range(v2.__len__()):
        lon1=v2[j][1];
        lat1=v2[j][2];
        min_dis=1000000;

        tmep_dis_letter_200 = [];
        tmep_dis_letter_min = np.array([np.array([0, '0', 0.0, 0.0])]);

        for k in range(v3.__len__()):
            lon2=v3[k][2]*pow(10,-6);
            lat2=v3[k][3]*pow(10,-6);
            a=Latitude.dis(lat1,lon1,lat2,lon2);
            b=Longitude.dis(lat1,lon1,lat2,lon2);
            dis=math.sqrt(a**2+b**2);
            #dis=math.sqrt((lon1-lon2)**2+(lat1-lat2)**2);
            if (dis <= 30):
                tmep_dis_letter_200.append(list(v3[k, :]));
            else:
                if (dis <= min_dis):
                    min_dis = dis;
                    tmep_dis_letter_min[0][0] = Uni_Bus_ID[i];
                    tmep_dis_letter_min[0][1] = v2[j][0];
                    tmep_dis_letter_min[0][2] = round(lon2 * pow(10, 6));
                    tmep_dis_letter_min[0][3] = round(lat2 * pow(10, 6));

        tmep_dis_letter_200 = np.array(tmep_dis_letter_200);

        if (len(tmep_dis_letter_200) != 0):
            Trans[m][0] = Uni_Bus_ID[i];
            Trans[m][1] = v2[j][0];
            #a = np.mean(tmep_dis_letter_200[:, 2].astype(float));
            Trans[m][2] = round(np.mean(tmep_dis_letter_200[:, 2].astype(float)));
            Trans[m][3] = round(np.mean(tmep_dis_letter_200[:, 3].astype(float)));
            m = m + 1;
        else:
            Trans[m][0] = Uni_Bus_ID[i];
            Trans[m][1] = v2[j][0];
            Trans[m][2] = tmep_dis_letter_min[0, 2];
            Trans[m][3] = tmep_dis_letter_min[0, 3];
            m = m + 1;

#得到输入数据
Data = Trans[Trans[:,1].argsort()];

# with open('F:\PythonWorkplace/bus_station_with_subway_data/370_Trans.csv','w+') as f:
#     for i in range(Data.__len__()):
#         f.write(Data[i][0]+","+Data[i][1]+","+Data[i][2]+","+Data[i][3]+"\n");




# l=1;
# l=[];
# l1=[];
# df2 = df1.loc[df1['BUS_ID'] == Uni_Bus_ID[1]];
# v3=df2.values;
#
# i=0;
# while(i<v3.__len__()):
#     if(v3[i][5]==0 or v3[i][6]==0):
#         v3=np.delete(v3,i,axis=0);
#     else:
#         i=i+1;
#
# for i in range(v2.__len__()):
#         l.append(v2[i][1]*1000000-12000);
#         l1.append(v2[i][2]*1000000-3000);
#
# # for i in range(Trans.__len__()):
# #     if(Trans[i][0]=='222159'):
# #         l.append(Trans[i][2]);
# #         l1.append(Trans[i][3]);
# #l=Trans[0:47,2];
# #l1=Trans[0:47,3];
# #l=l.astype(np.int);
# #l1=l1.astype(np.int);
# plt.scatter(l, l1, label='frist label', color='g', s=10);
# plt.scatter(v3[:,5],v3[:,6], label='frist label',color='r', s=5);
# help(plt.scatter);
# plt.xlabel('x');
# plt.ylabel('y');
# plt.title('Interesting Graph\nCheck it out');
# plt.legend();
# plt.show();
# l=1;
# column_v_enty=1;
# column_v_source=0;
# nof=Data.__len__();
# list_entry, entry_ia, entry_ic = np.unique(Data[:, column_v_enty], return_index=True, return_inverse=True);
# entry_ia.sort();
# list_entry.sort();
# list_source, source_ia, source_ic = np.unique(Data[:, column_v_source], return_index=True, return_inverse=True);
# nos=list_source.__len__();
# num = np.zeros((nos, 1));
#
# # 统计每个源声明的实体数
# for i in range(nof):
#     num[source_ic[i]] = num[source_ic[i]] + 1;
#
# # 加噪声
# for i in range(6):  # 取5个源，对其加上高斯噪声
#     s = list_source[i + 2];  # 被选用的源
#     l = np.random.normal(10000, np.sqrt(1000), size=(1, int(num[i + 5][0])));
#     # l=list(l[0]);
#     # n, bins, patches = plt.hist(l, bins=10, normed=0, facecolor='green', alpha=0.75);
#     # plt.show();
#     k = 0;
#     for j in range(Data.__len__()):  # 对该源的所有声明值加上高斯噪声，v1为总体数据
#         if (Data[j][0] == s):
#             Data[j][2] = l[0][k] + float(Data[j][2]);
#             k = k + 1;

#计算真值
truth_and_weight_EXP=exp.PTBS(Data, 50);
truth_and_weight_CRH=crh.CRH(Data,3);
truth_and_weight_CATD=catd.CATD(Data,3);
truth_and_weight_GTM=gtm.CTM(Data,3);
truth_and_weight_KDEm=kdem.KDEm(Data,3);
truth_and_weight_MEAN=mean.Mean(Data,3);
truth_and_weight_MEDIAN=median.Medain(Data,3);
#
with open('test/bus_station_with_subway_data/all_bus_stop/370_CRH.csv', 'w') as f:
    for j in range(len(truth_and_weight_CRH)):
            f.write(truth_and_weight_CRH[j][0]+','+truth_and_weight_CRH[j,1]+','
                    +truth_and_weight_CRH[j,2]+'\n');

with open('test/bus_station_with_subway_data/all_bus_stop/370_CATD.csv', 'w') as f:
    for j in range(len(truth_and_weight_CATD)):
            f.write(truth_and_weight_CATD[j][0]+','+truth_and_weight_CATD[j,1]+','
                    +truth_and_weight_CATD[j,2]+'\n');

with open('test/bus_station_with_subway_data/all_bus_stop/370_TMVD.csv', 'w') as f:
    for j in range(len(truth_and_weight_EXP)):
            f.write(truth_and_weight_EXP[j][0]+','+truth_and_weight_EXP[j,1]+','
                    +truth_and_weight_EXP[j,2]+'\n');

with open('test/bus_station_with_subway_data/all_bus_stop/370_GTM.csv', 'w') as f:
    for j in range(len(truth_and_weight_GTM)):
            f.write(truth_and_weight_GTM[j][0]+','+truth_and_weight_GTM[j,1]+','
                    +truth_and_weight_GTM[j,2]+'\n');

with open('test/bus_station_with_subway_data/all_bus_stop/370_KDEm.csv', 'w') as f:
    for j in range(len(truth_and_weight_KDEm)):
            f.write(truth_and_weight_KDEm[j][0]+','+truth_and_weight_KDEm[j,1]+','
                    +truth_and_weight_KDEm[j,2]+'\n');

with open('test/bus_station_with_subway_data/all_bus_stop/370_Mean.csv', 'w') as f:
    for j in range(len(truth_and_weight_MEAN)):
            f.write(truth_and_weight_MEAN[j][0]+','+truth_and_weight_MEAN[j,1]+','
                    +truth_and_weight_MEAN[j,2]+'\n');

with open('test/bus_station_with_subway_data/all_bus_stop/370_MEDIAN.csv', 'w') as f:
    for j in range(len(truth_and_weight_MEDIAN)):
            f.write(truth_and_weight_MEDIAN[j][0]+','+truth_and_weight_MEDIAN[j,1]+','
                    +truth_and_weight_MEDIAN[j,2]+'\n');



#提取相关站点
bus_station_with_subway=['长郡中学','侯家塘','侯家塘南','黄土岭','涂家冲','麻园塘',
                         '浦沅','竹塘路口','莲花山','林大路芙蓉路口','环保大道芙蓉南路口',
                         '侯家塘北','板塘村','天际岭隧道北','天际岭隧道南'];

#bus_station_with_subway_data=np.array([np.array(['0',0.0,0.0]) for i in range(len(bus_station_with_subway))]);
with open('test/bus_station_with_subway_data/370_CRH.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_CRH)):
            if(truth_and_weight_CRH[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_CRH[j,1]+','
                        +truth_and_weight_CRH[j,2]+'\n');

with open('test/bus_station_with_subway_data/370_CATD.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_CATD)):
            if(truth_and_weight_CATD[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_CATD[j,1]+','
                        +truth_and_weight_CATD[j,2]+'\n');

with open('test/bus_station_with_subway_data/370_TMVD.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_EXP)):
            if(truth_and_weight_EXP[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_EXP[j,1]+','
                        +truth_and_weight_EXP[j,2]+'\n');

with open('test/bus_station_with_subway_data/370_GTM.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_GTM)):
            if(truth_and_weight_GTM[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_GTM[j,1]+','
                        +truth_and_weight_GTM[j,2]+'\n');

with open('test/bus_station_with_subway_data/370_KDEm.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_KDEm)):
            if(truth_and_weight_KDEm[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_KDEm[j,1]+','
                        +truth_and_weight_KDEm[j,2]+'\n');

with open('test/bus_station_with_subway_data/370_Mean.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_MEAN)):
            if(truth_and_weight_MEAN[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_MEAN[j,1]+','
                        +truth_and_weight_MEAN[j,2]+'\n');

with open('test/bus_station_with_subway_data/370_Median.csv', 'w+') as f:
    for i in range(bus_station_with_subway.__len__()):
        for j in range(len(truth_and_weight_MEDIAN)):
            if(truth_and_weight_MEDIAN[j,0]==bus_station_with_subway[i]):
                f.write(bus_station_with_subway[i]+','+truth_and_weight_MEDIAN[j,1]+','
                        +truth_and_weight_MEDIAN[j,2]+'\n');








#plt.scatter(v2[:,1],v2[:,2], label='frist label',color='r', s=10);
# l=truth_and_weight_CRH[:,1];
# l1=truth_and_weight_CRH[:,2];
# l=l.astype(np.float);
# l1=l1.astype(np.float);
# l2=truth_and_weight_CATD[:,1];
# l3=truth_and_weight_CATD[:,2];
# l2=l2.astype(np.float);
# l3=l3.astype(np.float);
#
# l4=truth_and_weight_EXP[:,1];
# l5=truth_and_weight_EXP[:,2];
# l4=l4.astype(np.float);
# l5=l5.astype(np.float);
#
# l6=truth_and_weight_GTM[:,1];
# l7=truth_and_weight_GTM[:,2];
# l6=l6.astype(np.float);
# l7=l7.astype(np.float);
#
# l8=truth_and_weight_KDEm[:,1];
# l9=truth_and_weight_KDEm[:,2];
# l8=l8.astype(np.float);
# l9=l9.astype(np.float);
#
# # plt.scatter(l, l1, label='f1 label', color='g', s=10);
# # plt.scatter(l2, l3, label='f2 label', color='r', s=10);
# # plt.scatter(l4, l5, label='f3 label', color='c', s=10);
# plt.scatter(l6, l7, label='f4 label', color='b', s=10);
# plt.scatter(l8, l9, label='f5 label', color='m', s=10);
# help(plt.scatter);
# plt.xlabel('x');
# plt.ylabel('y');
# plt.title('Interesting Graph\nCheck it out');
# plt.legend();
# plt.show();

#计算误差
CRH_mae=caculat.caculat(truth_and_weight_CRH,v2);
CATD_mae=caculat.caculat(truth_and_weight_CATD,v2);
GTM_mae=caculat.caculat(truth_and_weight_GTM,v2);
KDEm_mae=caculat.caculat(truth_and_weight_KDEm,v2);
EXP_mae=caculat.caculat(truth_and_weight_EXP,v2);
MEAN_mae=caculat.caculat(truth_and_weight_MEAN,v2);
MEDIAN_mae=caculat.caculat(truth_and_weight_MEDIAN,v2);

print("CRH_mae={}".format(CRH_mae));
print("CATD_mae={}".format(CATD_mae));
print("GTM_mae={}".format(GTM_mae));
print("KDEm_mae={}".format(KDEm_mae));
print("EXP_mae={}".format(EXP_mae));
print("MEAN_mae={}".format(MEAN_mae));
print("MEDIAN_mae={}".format(MEDIAN_mae));


# v2 = v2[v2[:,0].argsort()];
# plt.scatter(truth_and_weight_CRH[:,1].astype(np.float),truth_and_weight_CRH[:,2].astype(np.float), label='frist label',color='r', s=5);
# plt.scatter(list(v2[:,1]*1000000), list(v2[:,2]*1000000), label='frist label', color='g', s=10);
# plt.scatter(truth_and_weight_EXP[:,1].astype(np.float),truth_and_weight_EXP[:,2].astype(np.float), label='frist label',color='b', s=5);
# plt.scatter(truth_and_weight_CATD[:,1].astype(np.float),truth_and_weight_CATD[:,2].astype(np.float), label='frist label',color='k', s=5);
# help(plt.scatter);
# plt.xlabel('x');
# plt.ylabel('y');
# plt.title('Interesting Graph\nCheck it out');
# plt.legend();
# plt.show();
# l=[];


