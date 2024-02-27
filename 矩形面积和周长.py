# coding=utf-8
# coding=gbk
# @author: rourou
# @file: 矩形面积和周长.py
# @time: 2024/2/27 17:44
# @desc:
# 编写一个Python程序，创建一个几何图形计算程序，使用静态方法来计算矩形的面积和周长。
# 定一个一个计算程序的类
class Calc:
    # 计算面积的公式
    @staticmethod
    def area(n1,n2):
        return n1*n2

    # 计算面积的周长
    @staticmethod
    def round(n1, n2):
        return 2*n1+2*n2
print(f"矩形的面积{Calc.area(17,30)},周长为{Calc.round(17,30)}")


