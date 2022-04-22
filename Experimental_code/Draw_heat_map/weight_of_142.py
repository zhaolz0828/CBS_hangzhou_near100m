import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
import Latitude as Lat
import Longitude as Lon



# from numpy import random
#
# N = 20
# R = random.randn(N, N)
# fig = plt.figure()
# sns_plot = sns.heatmap(R)
# # fig.savefig("heatmap.pdf", bbox_inches='tight') # 减少边缘空白
# plt.show()



def take2(elem):
    return elem[1];

def LatAndLonToDis(lat1,lon1,lat2,lon2):
    Lat_dis = Lat.dis(lat1, lon1, lat2, lon2);
    Lon_dis = Lon.dis(lat1, lon1, lat2, lon2);
    dis=math.sqrt(Lat_dis**2+Lon_dis**2);
    return dis;


df1 = pd.DataFrame(pd.read_csv('bus_station_with_subway_data/near_point/142_Trans.csv', header=None, encoding='gbk'));

Uni_Bus_ID = list(df1[0].unique());
Uni_Bus_ID.sort();
Data=df1.values;

bus_142_truth=pd.read_excel('translation_data/truth_line/142_truth.xlsx').values;

bus_142_CATD=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_CATD.csv',
                         header=None, encoding='gbk').values;
bus_142_CRH=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_CRH.csv',
                        header=None, encoding='gbk').values;
bus_142_GTM=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_GTM.csv',
                        header=None, encoding='gbk').values;
bus_142_KDEm=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_KDEm.csv',
                         header=None, encoding='gbk').values;
bus_142_Mean=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_Mean.csv',
                         header=None, encoding='gbk').values;
bus_142_Median=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_Median.csv',
                           header=None, encoding='gbk').values;
bus_142_TMVD=pd.read_csv('bus_station_with_subway_data/all_bus_stop/142_TMVD.csv',
                         header=None, encoding='gbk').values;

dis_GT=[];
dis_CATD=[];
dis_CRH=[];
dis_GTM=[];
dis_KDEm=[];
dis_Mean=[];
dis_Median=[];
dis_TMVD=[];
#计算误差
for i in range(len(Uni_Bus_ID)):
    Temp=Data[Data[:,0]==Uni_Bus_ID[i]];
    #GT
    temp_gt=[];
    for j in range(len(Temp)):
        for k in range(len(bus_142_truth)):
            if(Temp[j][1]==bus_142_truth[k][0]):
                temp_gt.append(LatAndLonToDis(bus_142_truth[k, 2], bus_142_truth[k, 1]
                , float(Temp[j, 3]) * pow(10, -6),float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_GT.append(np.mean(temp_gt));
    #PTBS
    temp_catd = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_CATD)):
            if (Temp[j][1] == bus_142_CATD[k][0]):
                temp_catd.append(LatAndLonToDis(bus_142_CATD[k, 2]* pow(10, -6), bus_142_CATD[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_CATD.append(np.mean(temp_catd));
    #CRH
    temp_crh = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_CRH)):
            if (Temp[j][1] == bus_142_CRH[k][0]):
                temp_crh.append(LatAndLonToDis(bus_142_CRH[k, 2]* pow(10, -6), bus_142_CRH[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_CRH.append(np.mean(temp_crh));
    #GTM
    temp_gtm = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_GTM)):
            if (Temp[j][1] == bus_142_GTM[k][0]):
                temp_gtm.append(LatAndLonToDis(bus_142_GTM[k, 2]* pow(10, -6), bus_142_GTM[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_GTM.append(np.mean(temp_gtm));
    #KDEm
    temp_kdem = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_KDEm)):
            if (Temp[j][1] == bus_142_KDEm[k][0]):
                temp_kdem.append(LatAndLonToDis(bus_142_KDEm[k, 2]* pow(10, -6), bus_142_KDEm[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_KDEm.append(np.mean(temp_kdem));
    #Mean
    temp_mean = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_Mean)):
            if (Temp[j][1] == bus_142_Mean[k][0]):
                temp_mean.append(LatAndLonToDis(bus_142_Mean[k, 2]* pow(10, -6), bus_142_Mean[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_Mean.append(np.mean(temp_mean));
    #Median
    temp_median = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_Median)):
            if (Temp[j][1] == bus_142_Median[k][0]):
                temp_median.append(LatAndLonToDis(bus_142_Median[k, 2]* pow(10, -6), bus_142_Median[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_Median.append(np.mean(temp_median));
    #TMVD
    temp_tmvd = [];
    for j in range(len(Temp)):
        for k in range(len(bus_142_TMVD)):
            if (Temp[j][1] == bus_142_TMVD[k][0]):
                temp_tmvd.append(LatAndLonToDis(bus_142_TMVD[k, 2]* pow(10, -6), bus_142_TMVD[k, 1]* pow(10, -6)
                                              , float(Temp[j, 3]) * pow(10, -6), float(Temp[j, 2]) * pow(10, -6)));
                break;
    dis_TMVD.append(np.mean(temp_tmvd));

dis_GT_max=max(dis_GT);
dis_GT_min=min(dis_GT);
for i in range(len(dis_GT)):
    dis_GT[i]=(dis_GT[i]-dis_GT_min)/(dis_GT_max-dis_GT_min);

dis_CATD_max=max(dis_CATD);
dis_CATD_min=min(dis_CATD);
for i in range(len(dis_CATD)):
    dis_CATD[i]=(dis_CATD[i]-dis_CATD_min)/(dis_CATD_max-dis_CATD_min);

dis_CRH_max=max(dis_CRH);
dis_CRH_min=min(dis_CRH);

for i in range(len(dis_CRH)):
    dis_CRH[i]=(dis_CRH[i]-dis_CRH_min)/(dis_CRH_max-dis_CRH_min);

dis_GTM_max=max(dis_GTM);
dis_GTM_min=min(dis_GTM);

for i in range(len(dis_GTM)):
    dis_GTM[i]=(dis_GTM[i]-dis_GTM_min)/(dis_GTM_max-dis_GTM_min);

dis_KDEm_max=max(dis_KDEm);
dis_KDEm_min=min(dis_KDEm);

for i in range(len(dis_KDEm)):
    dis_KDEm[i]=(dis_KDEm[i]-dis_KDEm_min)/(dis_KDEm_max-dis_KDEm_min);

dis_Mean_max=max(dis_Mean);
dis_Mean_min=min(dis_Mean);

for i in range(len(dis_Mean)):
    dis_Mean[i]=(dis_Mean[i]-dis_Mean_min)/(dis_Mean_max-dis_Mean_min);

dis_Median_max=max(dis_Median);
dis_Median_min=min(dis_Median);

for i in range(len(dis_Median)):
    dis_Median[i]=(dis_Median[i]-dis_Median_min)/(dis_Median_max-dis_Median_min);

dis_TMVD_max=max(dis_TMVD);
dis_TMVD_min=min(dis_TMVD);

for i in range(len(dis_TMVD)):
    dis_TMVD[i]=(dis_TMVD[i]-dis_TMVD_min)/(dis_TMVD_max-dis_TMVD_min);

GT=[3,1,0,1,4,1,5,5,0,3,2,3,0,0,2,0,2,0,0,1,0,2,0,1,0,0,0,0,0,0,0,0,0,0,1];
CRH=[4,2,5,3,0,2,1,3,1,2,0,0,1,0,1,0,1,0,0,1,2,0,1,1,0,0,0,1,1,2,0,0,0,0,1];
CATD=[2,3,4,3,4,0,0,4,0,3,0,1,1,0,0,0,1,1,2,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,1];
GTM=[1,0,2,3,2,2,2,2,2,1,2,0,2,2,1,0,1,0,1,2,0,1,0,0,1,0,0,1,0,3,1,1,0,0,1];
KDEm=[2,2,1,4,5,1,2,0,3,1,1,2,0,1,0,0,0,0,1,1,0,1,2,0,1,0,1,0,1,0,2,0,0,0,2];
Mean=[3,4,1,3,1,4,1,0,2,2,0,1,3,0,0,1,0,0,0,0,1,1,1,3,0,1,0,1,1,0,0,0,1,0,1];
Median=[2,4,1,7,0,2,0,2,3,1,1,0,0,1,1,0,0,1,0,1,2,0,1,0,0,1,0,1,0,1,2,0,0,0,2];
TMVD=[4,3,0,4,2,2,2,2,1,1,2,1,1,0,1,0,0,0,0,1,1,2,1,1,0,0,2,0,1,0,0,0,1,0,1];

#probability
for i in range(len(GT)):
    GT[i] /= 37;
    CRH[i] /= 37;
    CATD[i] /= 37;
    GTM[i] /= 37;
    KDEm[i] /= 37;
    TMVD[i] /= 37;

with open('Data_of_Trans_Map/GT.csv','w+') as f:
    for i in range(len(GT)):
        f.write(str(GT[i])+'\n');

with open('Data_of_Trans_Map/CRH.csv','w+') as f:
    for i in range(len(CRH)):
        f.write(str(CRH[i])+'\n');

with open('Data_of_Trans_Map/CATD.csv','w+') as f:
    for i in range(len(CATD)):
        f.write(str(CATD[i])+'\n');

with open('Data_of_Trans_Map/GTM.csv','w+') as f:
    for i in range(len(GTM)):
        f.write(str(GTM[i])+'\n');

with open('Data_of_Trans_Map/KDEm.csv','w+') as f:
    for i in range(len(KDEm)):
        f.write(str(KDEm[i])+'\n');

with open('Data_of_Trans_Map/TMVD.csv','w+') as f:
    for i in range(len(TMVD)):
        f.write(str(TMVD[i])+'\n');



#heatmap
def relation(list1,list2):
    temp=0;
    for i in range(len(GT)):
        temp = temp + (np.sqrt(list2[i]) - np.sqrt(list1[i])) ** 2;
    temp/=np.sqrt(2);
    return temp;

for i in range(len(GT)):
    GT[i]=GT[i]/35;
    CRH[i]=CRH[i]/35;
    CATD[i]=CATD[i]/35;
    GTM[i]=GTM[i]/35;
    KDEm[i]=KDEm[i]/35;
    TMVD[i]=TMVD[i]/35;

Methods=[GT,CRH,CATD,GTM,KDEm,TMVD];

rela_matrix=[];
for list1 in Methods:
    temp=[];
    for list2 in Methods:
        temp.append(relation(list1,list2))
    rela_matrix.append(temp);

rela_matrix=pd.DataFrame(rela_matrix);
rela_matrix.columns=['GT','CRH','PTBS','GTM','KDEm','TMVD'];
rela_matrix.index=['GT','CRH','PTBS','GTM','KDEm','TMVD'];
f,ax=plt.subplots(figsize=(9,8));
ax=sns.heatmap(rela_matrix,vmin=0,vmax=0.02,annot=True,
               xticklabels=['GT','CRH','PTBS','GTM','KDEm','PTBS'],
               yticklabels=['GT','CRH','PTBS','GTM','KDEm','PTBS']);



cax = plt.gcf().axes[-1];
cax.tick_params(labelsize=20);
plt.xticks(fontsize=18);
plt.yticks(fontsize=18);
plt.show();




# CRH_Dh=0;
# CATD_Dh=0;
# GTM_Dh=0;
# KDEm_Dh=0;
# TMVD_Dh=0;
#
# for i in range(len(GT)):
#     CRH_Dh=CRH_Dh+(np.sqrt(GT[i])-np.sqrt(CRH[i]))**2;
#     CATD_Dh = CATD_Dh + (np.sqrt(GT[i]) - np.sqrt(PTBS[i])) ** 2;
#     GTM_Dh = GTM_Dh + (np.sqrt(GT[i]) - np.sqrt(GTM[i])) ** 2;
#     KDEm_Dh = KDEm_Dh + (np.sqrt(GT[i]) - np.sqrt(KDEm[i])) ** 2;
#     TMVD_Dh = TMVD_Dh + (np.sqrt(GT[i]) - np.sqrt(TMVD[i])) ** 2;
#
# CRH_Dh=CRH_Dh/np.sqrt(2);
# CATD_Dh=CATD_Dh/np.sqrt(2);
# GTM_Dh=GTM_Dh/np.sqrt(2);
# KDEm_Dh=KDEm_Dh/np.sqrt(2);
# TMVD_Dh=TMVD_Dh/np.sqrt(2);





CRH_RMSE=0;
CATD_RMSE=0;
GTM_RMSE=0;
KDEm_RMSE=0;
Mean_RMSE=0;
Median_RMSE=0;
TMVD_RMSE=0;
for i in range(len(GT)):
    CRH_RMSE=CRH_RMSE+(GT[i]-CRH[i])**2;
    CATD_RMSE = CATD_RMSE + (GT[i] - CATD[i]) ** 2;
    GTM_RMSE = GTM_RMSE + (GT[i] - GTM[i]) ** 2;
    KDEm_RMSE = KDEm_RMSE + (GT[i] - KDEm[i]) ** 2;
    Mean_RMSE = Mean_RMSE + (GT[i] - Mean[i]) ** 2;
    Median_RMSE = Median_RMSE + (GT[i] - Median[i]) ** 2;
    TMVD_RMSE = TMVD_RMSE + (GT[i] - TMVD[i]) ** 2;