import numpy as np
import pandas as pd
import math

def CTM(Dataset,iti):
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
    alpha=10;beta=10;sigma=1;mu0=0;
#Initialize truth  Mean
    ini_truth = [np.array([0.0, 0.0]) for i in range(entry_ia.__len__() - 1)];
    ini_truth = np.array(ini_truth);
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

    index_truth=ini_truth[entry_ic];
    index_truth1 = ini_truth1[entry_ic];
#Initialize weight
    weight=np.zeros(nos);
    weight1 = np.zeros(nos);
    count=np.zeros(nos);
    count1 = np.zeros(nos);

    for i in range(nof):
        weight[source_ic[i]]=weight[source_ic[i]]+2*beta+(float(Dataset[i][2])-index_truth[i][0])**2;
        weight1[source_ic[i]] = weight1[source_ic[i]] + 2 * beta + (float(Dataset[i][3]) - index_truth1[i][0]) ** 2;
        count[source_ic[i]]=count[source_ic[i]]+1;
        count1[source_ic[i]] = count1[source_ic[i]] + 1;

    weight=np.divide(weight,count+2*(alpha+1));
    weight1 = np.divide(weight1, count1 + 2 * (alpha + 1));
    weight=np.divide(weight,np.sum(weight));
    weight1 = np.divide(weight1, np.sum(weight1));
    weight_matrix=weight[source_ic];
    weight_matrix1 = weight1[source_ic];
    truth = np.zeros(noe);
    truth1 = np.zeros(noe);
# GTM iteration Algorithm
    t=1;
    while(t<=iti):
        #calculate truth
        t=t+1;
        for i in range(noe):
            tempvalue=Dataset[entry_ia[i]:entry_ia[i+1],2];
            tempvalue = tempvalue.astype(np.float);
            tempvalue1 = Dataset[entry_ia[i]:entry_ia[i + 1], 3];
            tempvalue1 = tempvalue1.astype(np.float);
            tempweight=weight_matrix[entry_ia[i]:entry_ia[i+1]];
            tempweight1 = weight_matrix1[entry_ia[i]:entry_ia[i + 1]];
            temp_weight=[tempweight[j]**2 for j in range(tempweight.__len__())];
            temp_weight1 = [tempweight1[j] ** 2 for j in range(tempweight1.__len__())];
            temp_weight=np.array(temp_weight);
            temp_weight1 = np.array(temp_weight1);
            tmp=mu0/(sigma)**2+np.sum(np.divide(tempvalue,temp_weight));
            tmp_1 = mu0 / (sigma) ** 2 + np.sum(np.divide(tempvalue1, temp_weight1));
            tmp1=1/(sigma)**2+np.sum(np.divide(1,temp_weight));
            tmp1_1 = 1 / (sigma) ** 2 + np.sum(np.divide(1, temp_weight1));
            truth[i]=tmp/tmp1;
            truth1[i] = tmp_1 / tmp1_1;
            Truth[i][1]=truth[i];
            Truth[i][2] = truth1[i];

        index_truth=truth[entry_ic];
        index_truth1 = truth1[entry_ic];
        #calculate weight
        for i in range(nof):
            weight[source_ic[i]]=weight[source_ic[i]]+2*beta+(float(Dataset[i][2])-index_truth[i])**2;
            weight1[source_ic[i]] = weight1[source_ic[i]] + 2 * beta + (float(Dataset[i][3]) - index_truth1[i]) ** 2;
            count[source_ic[i]]=count[source_ic[i]]+1;
            count1[source_ic[i]] = count1[source_ic[i]] + 1;

        weight=np.divide(weight,np.sum(weight));
        weight1 = np.divide(weight1, np.sum(weight1));
        weight_matrix=weight[source_ic];
        weight_matrix1 = weight1[source_ic];

    return Truth;