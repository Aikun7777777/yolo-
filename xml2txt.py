# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET

dirpath = r'E:\CV04\yolov5-6.0housesmart\runs\detect\exp41\ng_label'  # 原来存放xml文件的目录
newdir = r'E:\CV04\yolov5-6.0housesmart\runs\detect\exp41\label_txt'                # 修改label后形成的txt目录

if not os.path.exists(newdir):
    os.makedirs(newdir)

dict_info = {'NG': 0}              # 有几个 属性 填写几个label names
# dict_info = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4,'6': 5, '7': 6, '8': 7,'9': 8, '2': 9}
# dict_info = {'zhadian':0,'hanzha': 1, 'hankong': 2,'buhanhouhankong':3, 'duanhan':4,
#         'pianhan':5, 'wuding':6, 'loudianhan':7, 'qiaoding':8,  'ok':9}
for fp in os.listdir(dirpath):
    if fp.endswith('.xml'):
        root = ET.parse(os.path.join(dirpath, fp)).getroot()

        xmin, ymin, xmax, ymax = 0, 0, 0, 0
        sz = root.find('size')
        width = float(sz[0].text)
        height = float(sz[1].text)
        filename = root.find('filename').text
        for child in root.findall('object'):  # 找到图片中的所有框

            sub = child.find('bndbox')  # 找到框的标注值并进行读取
            label = child.find('name').text
            label_ = dict_info.get(label)
            if label_:
                label_ = label_
            else:
                label_ = 0
            xmin = float(sub[0].text)
            ymin = float(sub[1].text)
            xmax = float(sub[2].text)
            ymax = float(sub[3].text)
            try:  # 转换成yolov3的标签格式，需要归一化到（0-1）的范围内
                x_center = (xmin + xmax) / (2 * width)
                x_center = '%.6f' % x_center
                y_center = (ymin + ymax) / (2 * height)
                y_center = '%.6f' % y_center
                w = (xmax - xmin) / width
                w = '%.6f' % w
                h = (ymax - ymin) / height
                h = '%.6f' % h
            except ZeroDivisionError:
                print(filename, '的 width有问题')
            with open(os.path.join(newdir, fp.split('.xml')[0] + '.txt'), 'a+') as f:
                f.write(' '.join([str(label_), str(x_center), str(y_center), str(w), str(h) + '\n']))
print('ok')



