# #1、打印小猫爱吃鱼，小猫要喝水
# # 定义一个猫的类
class Cat():
    #定义猫的方法
    def eat(self,food):
        print("小猫爱吃%s"%food)
    def drink(self,juice):
        print("小猫要喝%s"%juice)
#定义一个对象
Tom=Cat()
#调用猫的动作方法
Tom.eat("fash")
Tom.drink("werter")
# # 2、小明爱跑步，爱吃东西。
# # 1）小明体重75.0公斤
# # 2）每次跑步会减肥0.5公斤
# # 3）每次吃东西体重会增加1公斤
# # 4）小美的体重是45.0公斤
# #定义一个人的类
# class Person():
#     #初始化人的属性
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#     #打印人的初始体重
#     def __str__(self):
#         return "%s当前的体重是%s"%(self.name,self.weight)
#     #定义方法-吃饭
#     def eat(self):
#         self.weight=self.weight+1
#         print("%s吃饭后的体重是%s"%(self.name,self.weight))
#     #定义方法-跑步
#     def run(self):
#         self.weight=self.weight-0.5
#         print("%s跑步后的体重是%s"%(self.name,self.weight))
# #定义对象
# xiaoming= Person('小明',75.0)
# xiaomei=Person('小美',45.0)
# #打印这个对象
# print(xiaoming)
# #调用方法
# xiaoming.eat()
# xiaomei.run()
# # 3、摆放家具
# # 需求：
# # 1）.房子有户型，总面积和家具名称列表
# #    新房子没有任何的家具
# # 2）.家具有名字和占地面积，其中
# #    床：占4平米
# #    衣柜：占2平面
# #    餐桌：占1.5平米
# # 3）.将以上三件家具添加到房子中
# # 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
# # 定义一个家具的类
# class Furniture():
#     #定义家具的属性
#     def __init__(self,name,size):
#         self.name=name
#         self.size=size
# #定义一个房子的类
# class House():
#     #定义房子的属性:户型、总面积、剩余面积（总面积就是初始剩余面积）、家具列表
#     def __init__(self,house_type,total_area):
#         self.house_type=house_type
#         self.total_area=total_area
#         self.residual_area=total_area
#         self.lst1=[]
#     #答应房子的初始属性
#     def __str__(self):
#         return "房子的户型是%s，房子的总面积是%s，房子的剩余面积是%s，房子的中的家具有%s"%(self.house_type,self.total_area,self.residual_area,self.lst1)
#     #定义一个放家具的方法，此处需要传参
#     def add(self,item):
#         if self.residual_area >= item.size:
#             self.lst1.append(item.name)
#             self.residual_area=self.residual_area-item.size
#             print("房子的户型是%s，房子的总面积是%s，房子的剩余面积是%s，房子的中的家具有%s"%(self.house_type,self.total_area,self.residual_area,self.lst1))
#         else:
#             print("剩余面积不足")
# #创建一个对象-房子
# house1=House("三室一厅",100)
# #创建一个对象-家具
# bad=Furniture("床",4)
# closet=Furniture("衣柜",2)
# dining_table=Furniture("餐桌",1.5)
# #打印这个对象
# print(house1)
# #调用放家具的方法
# house1.add(bad)
# house1.add(closet)
# house1.add(dining_table)
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
# #定义一个类-士兵
# class Soldier():
#     #定义士兵的属性:姓名
#     def __init__(self,name):
#         self.name=name
#     #定义一个士兵的方法-开枪,并判断枪里面的剩余子弹
#     def short(self,item):
#         if item.zidan>0:
#             item.launch()
#         else:
#             item.shot()zz
# #定义一个类-枪
# class Gun():
#     #枪的属性
#     def __init__(self,gun_name,zidan):
#         self.gun_name=gun_name
#         self.zidan=zidan
#     #枪的方法-开火
#     def launch(self):
#         self.zidan-=1
#         print("剩余子弹%s"%self.zidan)
#     #枪的方法-装子弹
#     def shot(self):
#         self.zidan+=20
#         print("剩余子弹%s"%self.zidan)
# #定义一个士兵的对象
# Soldier1=Soldier("瑞恩")
# #定义一个枪的对象
# gun1=Gun("AK47",1)
# #调用枪的方法
# # gun1.launch(Soldier1)
# # gun1.shot(Soldier1)
# Soldier1.short(gun1)
