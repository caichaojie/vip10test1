# #定义一个类
# class Washer():
#     #初始化属性
#     def __init__(self,width,height,brand):
#         self.width=width
#         self.height=height
#         self.brand=brand
#     #定义打印对象的returu数据
#     def __str__(self):
#         return "这是%s的说明书"%self.brand
#     #删除方法
#     def __del__(self):
#         print("对象被删除了")
#     #创建一个方法
#     def wash(self):
#         #获取类里面的实例属性
#         print("%s洗衣机的宽度是%s,高度是%s"%(self.brand,self.width,self.height))
#         # print("洗衣机的高度是%s"%self.height)
#         # print("洗衣机的品牌是%s"%self.brand)
#
# #创建一个对象
# haier=Washer(10,20,'海尔')
# haier1=Washer(30,40,'西门子')
# #给对像定义属性
# # haier.width=500
# # haier.height=800
# # print("haier的宽度是%s"%haier.width)
# # print("haier的高度是%s"%haier.height)
#
# # print(haier)
# # #调用这个方法
# haier.wash()
# haier1.wash()
# print(haier)
# print(haier1)
# del haier

# #定义一个老师的类
# class Teacher():
#     #定义老师的属性
#     def __init__(self,name,sax,book):
#         self.name=name
#         self.sax=sax
#         self.book=book
#     #定义一个教学的方法
#     def booking(self):
#         print("%s老师的性别是%s,教的课程是%s"%(self.name,self.sax,self.book))
# #创建对象
# teacher1=Teacher('王大大',18,'语文')
# teacher2=Teacher('张大大',20,'数学')
# #调用方法
# teacher1.booking()
# teacher2.booking()

#定义一个家具类
class Furniture():
    #定义家具的属性
    def __init__(self,name,size):
        self.name=name
        self.size=size
#定义一个房子类
class House():
    #定义房子的属性
    def __init__(self,residual_area,floor_area):
        self.residual_area=residual_area
        self.floor_area=floor_area
        self.lst1=[]
    #房子的说明
    def __str__(self):
        return "房子的总面积%s,剩余面积%s"%(self.floor_area,self.residual_area)
    #创建一个放家具的方法
    def addfurniture(self,item):
        if self.residual_area >= item.size:
            self.lst1.append(item.name)

        else:
            print("剩余面积不足")

#创建一个房子的对象
house1=House(80,100)
#创建家具的对象
bad=Furniture('床',4)
#调用方法
house1.addfurniture(bad)