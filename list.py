import os

path = "E:\\Pandownload\\04 数据结构与算法之美\\mp3"
listll = []
for files in os.listdir(path):
    name = files.split(".")[0]
    listll.append(name)
print(listll)