import numpy as np
import pandas as pd
import math
import WeightedMedian as weightedMedian
def CRH(Dataset,iti):
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
    # df1 = pd.DataFrame(Dataset);
    # truth = df1[1].unique();
    ini_truth=[np.array([0.0,0.0]) for i in range(entry_ia.__len__()-1)];
    ini_truth1 = [np.array([0.0, 0.0]) for i in range(entry_ia.__len__() - 1)];
    ini_truth=np.array(ini_truth);
    ini_truth1 = np.array(ini_truth1);
    truth_2_column = np.zeros((noe, 2));
    truth = np.c_[list_entry, truth_2_column];
    #truth=[np.array(['aaaaaaaaaaaaaaaa',0.0]) for i in range(entry_ia.__len__()-1)];
    #truth=np.array(truth);
    weight=1/nos*np.ones((nos,1));
    weight_matrix=weight[source_ic];
    standerror=[];
    standerror1 = [];

    for i in range(noe):#calculate initial truth entry by entry
        #temp=[];
        temp1=[];
        temp2=[];
        truth[i][0]=Dataset[entry_ia[i]][1];
        tempvalue=Dataset[entry_ia[i]:entry_ia[i + 1], 2];#修改列值
        tempvalue=tempvalue.astype(np.float);
        tempvalue1=Dataset[entry_ia[i]:entry_ia[i+1],3];
        tempvalue1 = tempvalue1.astype(np.float);
        #temp.append(np.median(tempvalue));
        ini_truth[i][0]=np.median(tempvalue);
        ini_truth1[i][0] = np.median(tempvalue1);
        if (tempvalue.__len__() == 1 or tempvalue1.__len__()==1):
            temp1.append(np.std(tempvalue) + 0.1);
            temp2.append(np.std(tempvalue1)+0.1);
        else:
            temp1.append(np.std(tempvalue, ddof=1) + 0.1);
            temp2.append(np.std(tempvalue1, ddof=1) + 0.1);
        standerror.append(np.array(temp1));
        standerror1.append(np.array(temp2));

    #ini_truth=np.array(ini_truth);
    standerror=np.array(standerror);
    standerror1 = np.array(standerror1);
    index_truth=ini_truth;
    index_truth1 = ini_truth1;
    truth_matrix = ini_truth[entry_ic,0];
    truth_matrix1 = ini_truth1[entry_ic, 0];
    std_matrix = standerror[entry_ic];
    std_matrix1 = standerror1[entry_ic];
    con_count = np.zeros((nos, 1));
    t=1;
    temp_index = index_truth;

    while(t<=iti):
        t=t+1;
        score1 = np.zeros((nos, 1));
        score2 = np.zeros((nos, 1));

        for j in range(nof):
            score1[source_ic[j]]=score1[source_ic[j]]+np.abs((float(Dataset[j,2])-truth_matrix[j])/std_matrix[j]);#修改列值
            score2[source_ic[j]] = score2[source_ic[j]] + np.abs((float(Dataset[j, 2]) - truth_matrix1[j]) / std_matrix1[j]);

            if(t==2):
                con_count[source_ic[j]] = con_count[source_ic[j]] + 1;

        score1=np.divide(score1,con_count);
        score2 = np.divide(score2, con_count);
        score1=score1/np.sum(score1);
        score2 = score2 / np.sum(score2);
        score3=np.array(score1);
        score4 = np.array(score1);
        norm_score=np.max(score3);
        norm_score1 = np.max(score4);
        w=score3/norm_score+0.00001;
        w1 = score4 / norm_score1 + 0.00001;

        weight=-np.log(w);
        weight1 = -np.log(w1);
        weight_matrix=weight[source_ic];
        weight_matrix1 = weight1[source_ic];
        #weightedMedian=[];
        b=[];

        for j in range(noe):
            tempvalue = Dataset[entry_ia[j]:entry_ia[j + 1],2];#修改列值
            tempvalue = tempvalue.astype(np.float);
            tempvalue1 = Dataset[entry_ia[j]:entry_ia[j + 1], 3];
            tempvalue1 = tempvalue1.astype(np.float);
            tempweight = weight_matrix[entry_ia[j]:entry_ia[j + 1]];
            tempweight = tempweight.astype(np.float);
            tempweight1 = weight_matrix1[entry_ia[j]:entry_ia[j + 1]];
            tempweight1 = tempweight1.astype(np.float);
            index_truth[j, 1] = weightedMedian.WeightedMedian(tempvalue, tempweight);
            index_truth1[j, 1] = weightedMedian.WeightedMedian(tempvalue1, tempweight1);
            truth[j, 1] = index_truth[j, 1];
            truth[j,2]= index_truth1[j,1];
            # c=[];
            # c.append(np.median(tempvalue));
            # c.append(np.median(tempweight));
            # b.append(np.array(c));
            # index_truth[j]=np.array(index_truth[j]);
            # list(truth[j]).append(index_truth[j, 1]);
        # b=np.array(b);
        #index_truth=np.insert(index_truth, 0, values=b, axis=1);
        # index_truth=np.c_[temp_index,b];#合并两个数组

        truth_matrix = index_truth[entry_ic, 1];
        truth_matrix1 = index_truth1[entry_ic, 1];


    #truth = np.c_[truth, index_truth[:,1:3]];

    return truth;