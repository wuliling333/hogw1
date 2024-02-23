# 编写一个Python程序，实现一个计数器函数，该函数能够记录特定函数的调用次数。你需要使用闭包和装饰器来实现这个功能。

# 1，写一个闭包和计数器
def c_func(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"方法{func.__name__},返回了{count}次")
        return func(*args, **kwargs)

    return wrapper

# 2，调用次数
@c_func
def my_Count(name):
    return f"hello，{name}"

print(my_Count("TOM"))
print(my_Count("Lily"))
# 定义装饰器函数
# def count_calls(func):
#     count = 0  # 初始化计数器变量
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"函数 '{func.__name__}' 已被调用 {count} 次。")
#         return func(*args, **kwargs)  # 调用原始函数
#
#     return wrapper
#
#
# # 使用装饰器来计数函数调用
# @count_calls
# def greet(name):
#     return f"Hello, {name}!"
#
#
# # 调用被装饰的函数
# print(greet("Alice"))
# print(greet("Bob"))
# print(greet("Charlie"))