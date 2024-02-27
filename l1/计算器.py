# coding=utf-8
# coding=gbk
# @author: rourou
# @file: 计算器.py.py
# @time: 2024/2/26 11:36
# @desc:
# 编写一个Python程序，可以执行加法、减法、乘法和除法操作。用户可以输入两个数字和运算符，然后计算并输出结果。
# 实现计算器的功能（+、-、*、/），并处理异常情况，比如：输入的不是数字、除数为0等
# def calculating_machine():
#
#     while True:
#         try:
#             num1 = int(input("请输入第一个数字："))
#             formula = input("请输入【+、—、*、/】任意一个：")
#             num2 = int(input("请输入第二个数字："))
#             if formula == "+":
#                 result = num1 + num2
#             elif formula == "-":
#                 result = num1 - num2
#             elif formula == "*":
#                 result = num1 * num2
#             elif formula == "/":
#                 result = num1 / num2
#             else:
#                 print("请输入正确的运算符!")
#
#             print(f"结果为{num1}{formula}{num2}={result}")
#
#         except UnboundLocalError as error:
#           print("输入的运算符不对，请重新输入!", error)
#         except ValueError as error:
#           print("输入的不是数字", error)
#         except ZeroDivisionError as error:
#           print("被除数不能为0", error)
#
# if __name__ == '__main__':
#     calculating_machine()
def outer(fn):
    print('outer')
    def inner():
        print('inner')
        return fn

    return inner

@outer
def fun():
    print(fun)





