import xml.etree.ElementTree as ET
import numpy as np

class mytree:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.apple = []

    def val_leaves(self, node):
        # 判断是否为叶子节点
        children = []
        for child in node:
            children.append(child)
        if len(children) == 0:
            return True
        else:
            return False

    def get_children(self, node):
        # 产生儿子节点
        children = []
        for child in node:
            children.append(child)
        return children

    def grow_apple(self, node):
        # 长出水果
        if self.val_leaves(node):
            pass
        else:
            children = self.get_children(node)
            basket = []
            for child in children:
                if self.val_leaves(child):
                    # 控制得到是果实，或者枝头的其他属性
                    if child.text == None:
                        basket.append(child.attrib)
                    else:
                        basket.append(child.text)
                else:
                    self.grow_apple(child)
            self.apple.append(basket)

    def get_apple(self):
        # 得到所有水果
        self.grow_apple(self.root)
        return self.apple


if __name__ == "__main__":
    file = "stopinfos.xml"
    mytree = mytree(file)
    data = mytree.get_apple()
    data=np.array(data)
# for i in range(0,data.shape[0])
    for item in data:
        print(item[0])
        print('\n')