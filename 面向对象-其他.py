# class Dog(object):
#     def work(self):
#         print("指哪打哪儿")
# class Jingdog(Dog):
#     def work(self):
#         print("追击犯人")
# class Dudog(Dog):
#     def work(self):
#         print("追查毒品")
# class Person(object):
#     def work_with_dog(self,dog):
#         dog.work()
# tom=Jingdog()
# dg=Dudog()
# Dbing=Person()
# Dbing.work_with_dog(tom)
# Dbing.work_with_dog(dg)
# #类属性
# class Dog(object):
#     #定义类属性
#     tooch=10
# xiaohei=Dog()
# xiaobai=Dog()
# print(Dog.tooch)
# print(xiaohei.tooch)
# print(xiaobai.tooch)
# #修改类属性
# Dog.tooch=13
# #修改实例属性
# xiaobai.tooch=15
# print(Dog.tooch)
# print(xiaohei.tooch)
# print(xiaobai.tooch)
#类方法
# class Dog():
#     __tooch=10
#     @classmethod
#     def get_tooch(cls):
#         return cls.__tooch
# wangcai=Dog()
# result=wangcai.get_tooch()
# print(result)
#静态方法
class Dog():
    @staticmethod
    def work_dog():
        print("狗子能跑能跳")
xiaohei=Dog()
xiaohei.work_dog()
Dog.work_dog()