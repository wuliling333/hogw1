# 编写一个Python程序，实现一个计数器函数，该函数能够记录特定函数的调用次数。你需要使用闭包和装饰器来实现这个功能。

# 1，写一个闭包和计数器
def c_func(func):

    def wrapper(*args,**kwsrgs):
        wrapper.count+=1
        func(*args, **kwsrgs)
        print(f"方法{func.__name__},返回了{wrapper.count}次")

    wrapper.count = 0
    return wrapper

# 2，调用次数
@c_func
def my_Count():
    print("Hello,world")

my_Count()
my_Count()