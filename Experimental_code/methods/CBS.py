import numpy as np
import pandas as pd
import math
import random
from matplotlib import pyplot as plt
import scipy.stats as st

def CBS(Dataset, iti):
    column_v_enty=1;
    column_v_source=0;
    nof=Dataset.__len__();
    list_entry, entry_ia, entry_ic = np.unique(Dataset[:, column_v_enty], return_index=True, return_inverse=True);
    entry_ia.sort();
    list_entry.sort();
    list_source, source_ia, source_ic = np.unique(Dataset[:, column_v_source], return_index=True, return_inverse=True);
    nos=list_source.__len__();
    noe=entry_ia.__len__();
    entry_ia = list(entry_ia);
    entry_ia.append(nof);
    num=np.zeros((nos,1));

    #统计每个源声明的实体数
    for i in range(nof):
        num[source_ic[i]]=num[source_ic[i]]+1;

    ini_truth=[np.array([0.0,0.0]) for i in range(entry_ia.__len__()-1)];
    ini_truth=np.array(ini_truth);
    ini_truth1 = [np.array([0.0, 0.0]) for i in range(entry_ia.__len__() - 1)];
    ini_truth1 = np.array(ini_truth1);
    truth_2_column = np.zeros((noe, 2));
    Truth = np.c_[list_entry, truth_2_column];

    for i in range(noe):
        tempvalue=Dataset[entry_ia[i]:entry_ia[i+1],2];
        tempvalue = tempvalue.astype(np.float);
        tempvalue1 = Dataset[entry_ia[i]:entry_ia[i + 1], 3];
        tempvalue1 = tempvalue1.astype(np.float);
        ini_truth[i][0]=np.median(tempvalue);
        ini_truth1[i][0] = np.median(tempvalue1);

    index_truth = ini_truth[entry_ic];
    index_truth1 = ini_truth1[entry_ic];
    interval = np.zeros((nos, 2));
    interval1 = np.zeros((nos, 2));
    interval_mean = np.zeros((nos, 1));
    interval_mean1 = np.zeros((nos, 1));
    weight = np.zeros((nos, 1));
    weight1 = np.zeros((nos, 1));
    t = 1;

    while(t<=iti):
        t=t+1;
        score=np.zeros((nos,1));
        score1 = np.zeros((nos, 1));
        S_value_mean=np.zeros((nos,1));
        S_value_mean1 = np.zeros((nos, 1));
        S_value_error = np.zeros((nos, 1));
        S_value_error1 = np.zeros((nos, 1));
        l=[];
        l1=[];

        for i in range(nof):
            #score[source_ic[i]] = score[source_ic[i]]+(float(Dataset[i][2])-index_truth[i][0])**2;
            S_value_mean[source_ic[i]]=S_value_mean[source_ic[i]]+(float(Dataset[i][2])-index_truth[i][0]);
            S_value_mean1[source_ic[i]] = S_value_mean1[source_ic[i]] + (float(Dataset[i][3]) - index_truth1[i][0]);
        #     if(source_ic[i]==4):
        #         l.append(float(Dataset[i][2])-index_truth[i][0]);
        # #
        # # l_min = np.min(l);
        # # l_max = np.max(l);
        # # for i in range(l.__len__()):
        # #     l[i] = (l[i] - l_min) / (l_max - l_min);
        # # # #score = score + 0.1;
        # n, bins, patches = plt.hist(l, bins=20, normed=0, facecolor='green', alpha=0.75);
        # plt.show();

        for i in range(nos):
            S_value_mean[i]=S_value_mean[i]/num[i];
            S_value_mean1[i] = S_value_mean1[i] / num[i];

        for i in range(nof):
            S_value_error[source_ic[i]] = S_value_error[source_ic[i]] + ((float(Dataset[i][2]) - index_truth[i][0])-S_value_mean[source_ic[i]])**2;
            S_value_error1[source_ic[i]] = S_value_error1[source_ic[i]] + ((float(Dataset[i][3]) - index_truth1[i][0]) - S_value_mean1[source_ic[i]]) ** 2;

        for i in range(nos):
            if((num[i]-1)==0):
                S_value_error[i] = S_value_error[i] / (num[i]);
                S_value_error1[i] = S_value_error1[i] / (num[i]);
            else:
                S_value_error[i]=S_value_error[i]/(num[i]-1);
                S_value_error1[i] = S_value_error1[i] / (num[i] - 1);

        for i in range(nos):
            if ((num[i] - 1) == 0):
                a = S_value_mean[i] - (st.t.ppf(0.975, num[i] ) * np.sqrt(S_value_error[i])) / np.sqrt(num[i]);
                b = S_value_mean[i] + (st.t.ppf(0.975, num[i]) * np.sqrt(S_value_error[i])) / np.sqrt(num[i]);
                a1=S_value_mean1[i] - (st.t.ppf(0.975, num[i] ) * np.sqrt(S_value_error1[i])) / np.sqrt(num[i]);
                b1 = S_value_mean1[i] + (st.t.ppf(0.975, num[i]) * np.sqrt(S_value_error1[i])) / np.sqrt(num[i]);
            else:
                a=S_value_mean[i]-(st.t.ppf(0.975,num[i]-1)*np.sqrt(S_value_error[i]))/np.sqrt(num[i]);
                a1 = S_value_mean1[i] - (st.t.ppf(0.975, num[i] - 1) * np.sqrt(S_value_error1[i])) / np.sqrt(num[i]);
                b = S_value_mean[i] + (st.t.ppf(0.975, num[i] - 1) * np.sqrt(S_value_error[i])) / np.sqrt(num[i]);
                b1 = S_value_mean1[i] + (st.t.ppf(0.975, num[i] - 1) * np.sqrt(S_value_error1[i])) / np.sqrt(num[i]);
            interval[i][0]=a;
            interval1[i][0] = a1;
            interval[i][1]=b;
            interval1[i][1] = b1;

        for i in range(nos):
            #interval_mean[i]=1/(np.abs(interval[i][0]+interval[i][1])/2);
            # interval_mean[i] = 1 / 2*np.abs((st.t.ppf(0.975,num[i]-1)*np.sqrt(S_value_error[i]))/np.sqrt(num[i]));
            # interval_mean1[i] = 1 / 2*np.abs((st.t.ppf(0.975, num[i] - 1) * np.sqrt(S_value_error1[i])) / np.sqrt(num[i]));

            interval_mean[i] = 1 / np.abs(interval[i][1]);
            interval_mean1[i] = 1 / np.abs(interval1[i][1]);
            #interval_mean[i] = 1 / np.abs(S_value_mean[i]);

        weight=np.divide(interval_mean,np.sum(interval_mean));
        weight1 = np.divide(interval_mean1, np.sum(interval_mean1));
        Z=[];
        Z1 = [];

        for i in range(weight.__len__()):
            if(weight[i]!=0):
                Z.append(weight[i]);
            if (weight1[i] != 0):
                Z1.append(weight1[i]);

        for i in range(weight.__len__()):
            if(weight[i]==0):
                weight[i]=np.min(Z);
            if (weight1[i] == 0):
                weight1[i] = np.min(Z1);

        weight_M_matrix = weight[source_ic];
        weight_M_matrix1 = weight1[source_ic];
        truth = np.zeros((noe, 1));
        truth1 = np.zeros((noe, 1));

        for i in range(noe):
            tempvalue=Dataset[entry_ia[i]:entry_ia[i+1],2];
            tempvalue=tempvalue.astype(np.float);
            tempvalue1 = Dataset[entry_ia[i]:entry_ia[i + 1], 3];
            tempvalue1 = tempvalue1.astype(np.float);
            truth[i][0] = np.sum(np.multiply(weight_M_matrix[entry_ia[i]:entry_ia[i + 1], 0],tempvalue)) / np.sum(weight_M_matrix[entry_ia[i]:entry_ia[i + 1], 0]);
            truth1[i][0] = np.sum(np.multiply(weight_M_matrix1[entry_ia[i]:entry_ia[i + 1], 0], tempvalue1)) / np.sum(weight_M_matrix1[entry_ia[i]:entry_ia[i + 1], 0]);
            Truth[i][1] =truth[i][0];
            Truth[i][2] =truth1[i][0];

        index_truth = truth[entry_ic];
        index_truth1 = truth1[entry_ic];



    return Truth;
        # W = np.divide(st.chi2.cdf(num, noe), score); # 返回\chi^2(n)的概率密度函数在 0 到 num 上的积分，也就是概率分布函数的值
        # W = np.divide(st.chi2.cdf(num, noe), score);