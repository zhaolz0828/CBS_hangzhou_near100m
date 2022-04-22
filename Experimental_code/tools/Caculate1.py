import math

import numpy as np

import Latitude
import Longitude


def caculat(Dataset,Data):
    count=0;
    count1=0;
    l=[];
    dis1=[];
    dis2=[];
    for i in range(Dataset.__len__()):
        for j in range(Data.__len__()):
            if(Dataset[i][0]==Data[j][1]):
                # a=float(Dataset[i][2])*pow(10,-6)-float(Data[j][2])
                # b=float(Dataset[i][1])*pow(10,-6)-float(Data[j][1])
                # r = math.sqrt(a ** 2 + b ** 2);
                # l.append(r);
                # print(r)(lat1,lng1,lat2,lng2)维度维度经度经度
                a = Latitude.dis(float(Dataset[i][2])*pow(10,-6), float(Dataset[i][1])*pow(10,-6), float(Data[j][3]), float(Data[j][2]));
                b = Longitude.dis(float(Dataset[i][2])*pow(10,-6), float(Dataset[i][1])*pow(10,-6), float(Data[j][3]), float(Data[j][2]));
                r=math.sqrt(a**2+b**2);
                #r= np.sqrt(((float(Dataset[i][1]) - float(Data[j][1])*1000000)**2+(float(Dataset[i][2]) - float(Data[j][2])*1000000)**2));
                l.append(r);
                if(i==8 or i==17 or i==18 or i==20 or i==21 or i==23 or i==29 or i==31 or i==32 or i==33 or i==36 or i==40 or i==42 or i==45):
                    dis1.append(a);
                    dis2.append(b);
                #count1 += abs(float(Dataset[i][1]) - float(Data[j][1]));
                break;

    # rmse = math.sqrt(count / Data.__len__());
    # mae = count1 / Data.__len__();

    # return np.sum(l);
    return np.mean(l)