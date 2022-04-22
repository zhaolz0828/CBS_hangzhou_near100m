import numpy as np
import pandas as pd
import math
import random
from matplotlib import pyplot as plt
import scipy.stats as st

def Mean(Dataset,iti):
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
        ini_truth[i][0]=np.mean(tempvalue);
        ini_truth1[i][0] = np.mean(tempvalue1);

    for i in range(noe):
        Truth[i][1] = ini_truth[i][0];
        Truth[i][2] = ini_truth1[i][0];

    return Truth;
        # W = np.divide(st.chi2.cdf(num, noe), score); # 返回\chi^2(n)的概率密度函数在 0 到 num 上的积分，也就是概率分布函数的值
        # W = np.divide(st.chi2.cdf(num, noe), score);