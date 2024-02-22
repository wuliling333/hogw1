# 使用 for-in 内嵌 while 访问示例中的二维列表
# 使用 while 内嵌 for-in 访问示例中的二维列表
# 实现九九乘法表标准格式输出
def loop_info():
    # data = [
    #     [1,2,3,4,5,6,7,8,9],
    #     ["A","B","C","D","E"],
    #     ["Hello","World","Python","Hogwarts"]
    # ]
# 使用 for-in 内嵌 while 访问示例中的二维列表
#     for i in data:
#         for j in i:
#             print(j,end=" ")
#         print(j)
# 使用 while
#     x = 0
#     len1 = len(data)
#     while x < len1:
#         i = data[x]
#         j=0
#         len2=len(i)
#         while j <len2:
#             item=i[j]
#             print(item, end=" ")
#             j+=1
#         print()
#         x += 1
#  使用 for-in 内嵌 while 访问示例中的二维列表
#     for i in data:
#         r=0
#         len1=len(i)
#         while r< len1:
#             x=i[r]
#             print(x, end=" ")
#             r+=1
#         print()
# 使用 while 内嵌 for-in 访问示例中的二维列表
#     i=0
#     len1=len(data)
#     while i<len1:
#         item=data[i]
#         for x in item:
#             print(x, end=" ")
#         i+=1
#         print()
#  实现九九乘法表标准格式输出
   for i in range(1,10):
       for j in range(1,1+i):
           print(f"{j}*{i}={i*j:<3}" , end="  ")
       print()

if __name__ == '__main__':
    loop_info()
