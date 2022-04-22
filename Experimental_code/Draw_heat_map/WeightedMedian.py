import numpy as np
def WeightedMedian(tempvalue,tempweight):

    if(tempvalue.__len__()!=tempweight.__len__()):
        print("error");
        return;

    WSum=np.sum(tempweight[:]);
    tempweight = tempweight / WSum;
    A=np.c_[tempvalue,tempweight];
    ASort = A[A[:, 0].argsort()];
    dSort=ASort[:,0];
    wSort=ASort[:,1];
    sumVec=[];
    i=1;

    while(i<=wSort.__len__()):
        sumVec.append(np.sum(wSort[0:i]));
        i+=1;

    for j in range(sumVec.__len__()):
        if(sumVec[j]>=0.5):
            wMed=dSort[j];
            return wMed;
            break;

    if((np.sum(wSort[0:j-1])>0.5) and (np.sum(wSort[j:wSort.__len__()]))):
        print("error");
        return;