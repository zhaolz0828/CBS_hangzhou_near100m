#!/usr/bin/env python
"""
@Time ： 2022/4/10 9:42
@Auth ： 赵凌子
@File ： get_sumo_bus_loc.py
@IDE ：  PyCharm
@Motto： After all,tomorrow is another day.
"""
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
bus=pd.read_csv('sumo_hangzhou_bus.csv')
loc=pd.read_csv('line3.csv',encoding = "gbk")
Bus=[]
bus=np.array(bus)
loc=np.array(loc)





# Bus=pd.DataFrame(Bus)
# list_entry1, entry_ia1, entry_ic1 = np.unique(bus[:,1], return_index=True, return_inverse=True);
# entry_ia1.sort();
# list_entry1.sort();
# bus=bus[entry_ia1]



# print(bus[0][1],loc[0][1])
for j in range(0,bus.shape[0]-1):
    for i in range(0,loc.shape[0]-1):
        if  bus[j][1]==loc[i][1]:
            # print('1111111111')
            Bus.append([loc[i][1],loc[i][2],loc[i][3]])
            # Bus.append(loc[i][2])
            # Bus.append(loc[i][3])
            # Bus[i][0] = loc[i][1]
            # Bus[j][1] = loc[i][2]
            # Bus[j][2] = loc[i][3]
Bus=np.array(Bus)
# Bus=pd.DataFrame(Bus)
list_entry, entry_ia, entry_ic = np.unique(Bus[:,0], return_index=True, return_inverse=True);
entry_ia.sort();
list_entry.sort();
# Uni_Bus_ID = list(Bus[0].unique());
# Bus=Bus[Bus[:,1].argsort()]
# Bus.to_csv('sumo_bus_loc.csv')

# print(Bus[entry_ia])
stop_loc=pd.DataFrame(Bus[entry_ia])
# stop_loc=pd.DataFrame(Bus[entry_ia])
stop_loc.to_csv('sumo_bus_loc.csv')
print('3333333')