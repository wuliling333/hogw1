# coding=utf-8
# coding=gbk
# @author: rourou
# @file: 文件写入作业.py
# @time: 2024/2/23 17:17
# @desc:
# 打开文件 open（file，mode="r",buffering=-1,encoding=None)
# file.close()
# with open（"data","r") as file:

# 编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来
# 方法一
# file = open("data.txt", "w")
# file.write("你是属狗的吧")
# file.close()
# file = open("data.txt", "r")
# con = file.read()
# file.close()
# print(con)
# 方法二
data="[{'name':'王毛','age':8,'habby':'eat'},{'name':'李四','age':9,'habby':'play'}]"
# file_name="data.txt"
with open("data.txt", "w") as f:
    f.write(data)
with open("data.txt", "r") as f:
    c=f.read()
    print(c)
