import numpy as np
import pandas as pd
import math
import scipy.stats as st
from scipy.stats import chi2
def CATD(Dataset,iti):
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

    for i in range(nof):
        num[source_ic[i]]=num[source_ic[i]]+1;

    ini_truth=[np.array([0.0,0.0]) for i in range(entry_ia.__len__()-1)];
    ini_truth1 = [np.array([0.0, 0.0]) for i in range(entry_ia.__len__() - 1)];
    ini_truth=np.array(ini_truth);
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

    index_truth = ini_truth[entry_ic];
    index_truth1 = ini_truth1[entry_ic];
    t=1;
    W = np.zeros((nos, 1));
    W1 = np.zeros((nos, 1));

    while(t<=iti):
        t=t+1;
        score=np.zeros((nos,1));
        score1 = np.zeros((nos, 1));

        for i in range(nof):
            score[source_ic[i]] = score[source_ic[i]]+(float(Dataset[i][2])-index_truth[i][0])**2;
            score1[source_ic[i]] = score1[source_ic[i]] + (float(Dataset[i][3]) - index_truth1[i][0]) ** 2;

        score = score + 0.1;
        score1 = score1 + 0.1;

        W = np.divide(chi2.cdf(num,noe),score);
        W1 = np.divide(chi2.cdf(num, noe), score1);

        Z=[];
        Z1=[];

        for i in range(W.__len__()):
            if(W[i]!=0):
                Z.append(W[i]);
            if(W1[i]!=0):
                Z1.append(W1[i]);

        for i in range(W.__len__()):
            if(W[i]==0):
                W[i]=np.min(Z);
            if(W1[i]!=0):
                W1[i]=np.min(Z1);

        w_M_matrix=W[source_ic];
        w_M_matrix1 = W1[source_ic];
        truth=np.zeros((noe,1));
        truth1 = np.zeros((noe, 1));

        for i in range(noe):
            tempvalue=Dataset[entry_ia[i]:entry_ia[i+1],2];
            tempvalue = tempvalue.astype(np.float);
            tempvalue1 = Dataset[entry_ia[i]:entry_ia[i + 1], 3];
            tempvalue1 = tempvalue1.astype(np.float);
            truth[i][0]=np.sum(np.multiply(w_M_matrix[entry_ia[i]:entry_ia[i+1],0],tempvalue))/np.sum(w_M_matrix[entry_ia[i]:entry_ia[i+1],0]);
            truth1[i][0] = np.sum(np.multiply(w_M_matrix1[entry_ia[i]:entry_ia[i + 1], 0], tempvalue1)) / np.sum(w_M_matrix1[entry_ia[i]:entry_ia[i + 1], 0]);
            Truth[i][1]= truth[i][0];
            Truth[i][2] = truth1[i][0];

        index_truth=truth[entry_ic];
        index_truth1 = truth1[entry_ic];

    return Truth;