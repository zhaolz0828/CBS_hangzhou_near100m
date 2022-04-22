import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def take2(elem):
    return elem[1];

df1 = pd.DataFrame(pd.read_excel('translation_data/Bus_data_06/293.xlsx'));

Uni_Bus_ID = list(df1['BUS_ID'].unique());
Uni_Bus_ID.sort();

for i in range(len(Uni_Bus_ID)):
    df3=df1.loc[df1['BUS_ID'] == Uni_Bus_ID[i]];
    v3 = df3.values;
    n = 0;

    while (n < v3.__len__()):
        if (v3[n][5] == 0 or v3[n][6] == 0 or v3[n][5]<=100000000 or v3[n][6]<=20000000):
            v3 = np.delete(v3, n, axis=0);
            continue;
        n=n+1;

    # l=list(v3[:,5]);
    # l1=list(v3[:,6]);
    # plt.scatter(l, l1, label='frist label', color='g', s=10);
    plt.scatter(v3[:,5],v3[:,6], label='frist label',color='r', s=5);
    help(plt.scatter);
    plt.xlabel('x');
    plt.ylabel('y');
    plt.title(Uni_Bus_ID[i]);
    plt.legend();
    plt.show();