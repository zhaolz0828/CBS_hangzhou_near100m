#!/usr/bin/env python
"""
@Time ： 2022/4/9 15:46
@Auth ： 赵凌子
@File ： read_trace_xml.py
@IDE ：  PyCharm
@Motto： After all,tomorrow is another day.
"""
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from typing import re
from xml.dom import minidom
import pandas as pd
import numpy as np


# 提取的代码如下：

class get_xml():
    # 加载获取xml的文档对象
    def __init__(self, address):
        # 解析address文件，返回DOM对象，address为文件地址
        self.doc = minidom.parse(address)
        # DOM是树形结构，_get_documentElement()获得了树形结构的根节点
        self.root = self.doc._get_documentElement()
        # .getElementsByTagName()，根据name查找根目录下的子节点
        self.stops = self.root.getElementsByTagName("vehicle")


    def getxmldata(self):

        data_list = []
        j = -1
        responseData_node = self.root.getElementsByTagName("vehicle")

        for i in self.stops:
            j = j + 1
            # getAttribute()，获取DOM节点的属性的值

            if (i.getAttribute('type') == "pt_bus"):
                a = 'chatId":"(.*?)"'
                data_list.append(
                    (i.getAttribute("type"), i.getAttribute("id"), i.getAttribute("x"), i.getAttribute("y")))
        return data_list


data = get_xml('sumoTrace.xml')
data.getxmldata()
a = data.getxmldata()
a = pd.DataFrame(a)

a.to_csv('sumoTrace.csv')
print(a)
