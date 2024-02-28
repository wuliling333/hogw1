# coding=utf-8
# coding=gbk
# @author: rourou
# @file: 动物园作业.py
# @time: 2024/2/28 17:29
# @desc:
# 设计一个简单的动物园系统，其中包含不同类型的动物（如狗、猫和鸟）。每个动物都有自己的属性（如名字、年龄）和行为（如发出声音）。
# 使用封装、继承和多态来完成。
# 动物
class Animal:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def barking(self):
        return
class Dog(Animal):
    def barking(self):
        print(f"{self._name}{self._age}岁，汪汪汪")
# 属性
class Cat(Animal):
    def barking(self):
        print(f"{self._name}{self._age}岁，喵喵喵")
class Bird(Animal):
    def barking(self):
        print(f"{self._name}{self._age}岁，渣渣渣")

# class Zoo(Animal):
#     anlmal_list=[]
#
if __name__ == '__main__':
    dog=Dog("小狗",3)
    cat=Cat("小猫",2)
    bird =Bird("小鸟", 8)

    dog.barking()
    cat.barking()
    bird.barking()
    # print(dog1)



# 行为
# 动物园系统


