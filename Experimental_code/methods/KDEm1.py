import numpy as np
import pandas as pd
import math

def KDEm(Dataset,iti):
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
#Initialize truth
    ini_truth = [np.array([0.0, 0.0]) for i in range(entry_ia.__len__() - 1)];
    ini_truth = np.array(ini_truth);
    ini_truth1 = [np.array([0.0, 0.0]) for i in range(entry_ia.__len__() - 1)];
    ini_truth1 = np.array(ini_truth1);
    truth_2_column = np.zeros((noe, 2));
    Truth = np.c_[list_entry, truth_2_column];
#Initialize weight
    kernel_M=np.zeros(nof);
    kernel_M1 = np.zeros(nof);

    for i in range(noe):
        x=Dataset[entry_ia[i]:entry_ia[i+1],2];
        x = x.astype(np.float);
        y=Dataset[entry_ia[i]:entry_ia[i+1],3];
        y = y.astype(np.float);
        N=x.__len__();
        N1 = y.__len__();
        K=[];
        K1=[];
        x_mean=np.mean(x);
        y_mean=np.mean(y);
        z=0;
        z1=0;
        for j in range(N):
            z=z+np.abs(x[j]-x_mean);
            z1 = z1 + np.abs(y[j] - y_mean);
        h=z/N+0.1;
        h1=z1/N1+0.1;

        for j in range(N):
            k=0;
            k1=0;
            for m in range(N):
                tmp=np.abs(x[j]-x[m])/h;
                tmp1 = np.abs(y[j] - y[m]) / h1;
                k=k+np.exp(-(tmp)**2)/(np.sqrt(2*math.pi)*h);
                k1 = k1 + np.exp(-(tmp1) ** 2) / (np.sqrt(2 * math.pi) * h);

            K.append(k/N);
            K1.append(k1 / N1);
        kernel_M[entry_ia[i]:entry_ia[i+1]]=np.array(K);
        kernel_M1[entry_ia[i]:entry_ia[i + 1]] = np.array(K1);

    weight=1/nos*np.ones(nos);
    weight1 = 1 / nos * np.ones(nos);
    index_weight=weight[source_ic];
    index_weight1 = weight1[source_ic];
    #get normal
    temp_weight = [index_weight[j] ** 2 for j in range(index_weight.__len__())];
    temp_weight = np.array(temp_weight);
    temp_weight1 = [index_weight1[j] ** 2 for j in range(index_weight1.__len__())];
    temp_weight1 = np.array(temp_weight1);
    norm_M=kernel_M-np.multiply(2*kernel_M,index_weight)+np.multiply(kernel_M,temp_weight);
    norm_M1 = kernel_M1 - np.multiply(2 * kernel_M1, index_weight1) + np.multiply(kernel_M1, temp_weight1);
    #get c
    score=np.zeros(nos);
    score1 = np.zeros(nos);
    for i in range(nof):
        score[source_ic[i]]=score[source_ic[i]]+norm_M[i];
        score1[source_ic[i]] = score1[source_ic[i]] + norm_M1[i];

    c=-np.log(np.divide(np.divide(score,nos),np.sum(score)));
    c1 = -np.log(np.divide(np.divide(score1, nos), np.sum(score1)));
    #KDEm iteration Algorithm
    b=1;
    while(b<=iti):
        b=b+1;
        #undate weight
        weight=c/np.sum(c);
        weight1 = c1 / np.sum(c1);
        index_weight=weight[source_ic];
        index_weight1 = weight1[source_ic];
        #update truth
        t1=np.zeros(noe);
        t1_1 = np.zeros(noe);
        for i in range(noe):
            x1=index_weight[entry_ia[i]:entry_ia[i+1]];
            x1_1 = index_weight1[entry_ia[i]:entry_ia[i + 1]];
            x2=kernel_M[entry_ia[i]:entry_ia[i+1]];
            x2_1 = kernel_M1[entry_ia[i]:entry_ia[i + 1]];
            x3=Dataset[entry_ia[i]:entry_ia[i+1],2];
            x3 = x3.astype(np.float);
            x3_1 = Dataset[entry_ia[i]:entry_ia[i + 1], 3];
            x3_1 = x3_1.astype(np.float);
            t1[i]=np.sum(np.multiply(np.multiply(x1,x2),x3));
            t1_1[i] = np.sum(np.multiply(np.multiply(x1_1, x2_1), x3_1));

        t2=np.zeros(noe);
        t2_1 = np.zeros(noe);

        for i in range(noe):
            x1=index_weight[entry_ia[i]:entry_ia[i+1]];
            x1_1 = index_weight1[entry_ia[i]:entry_ia[i + 1]];
            x2=kernel_M[entry_ia[i]:entry_ia[i+1]];
            x2_1 = kernel_M1[entry_ia[i]:entry_ia[i + 1]];
            t2[i]=np.sum(np.multiply(x1,x2));
            t2_1[i] = np.sum(np.multiply(x1_1, x2_1));
            Truth[i][1]=np.divide(t1[i],t2[i]);
            Truth[i][2] = np.divide(t1_1[i], t2_1[i]);

        #get normal
        temp_weight = [index_weight[j] ** 2 for j in range(index_weight.__len__())];
        temp_weight = np.array(temp_weight);
        temp_weight1 = [index_weight1[j] ** 2 for j in range(index_weight1.__len__())];
        temp_weight1 = np.array(temp_weight1);
        norm_M = kernel_M - np.multiply(2 * kernel_M, index_weight) + np.multiply(kernel_M, temp_weight);
        norm_M1 = kernel_M1 - np.multiply(2 * kernel_M1, index_weight1) + np.multiply(kernel_M1, temp_weight1);
        #update c
        score=np.zeros(nos);
        score1 = np.zeros(nos);
        for i in range(nof):
            score[source_ic[i]]=score[source_ic[i]]+norm_M[i];
            score1[source_ic[i]] = score1[source_ic[i]] + norm_M1[i];

        c=-np.log(np.divide(np.divide(score,nos),np.sum(score)));
        c1 = -np.log(np.divide(np.divide(score1, nos), np.sum(score1)));

    return Truth;