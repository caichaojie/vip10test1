class Master(object):
    def __init__(self):
        self.gongfu="五香煎饼果子配方"
    def cake(self):
        print("会使用%s制作煎饼果子"%self.gongfu)
class School(Master):
    def __init__(self):
        self.gongfu="蒜香配方"
    def cake(self):
        print("会使用%s制作煎饼果子"%self.gongfu)
        super().__init__()
        super().cake()

#继承
class Tudi(School):
    def __init__(self):
        self.gongfu="独创配方"
        self.__money=1000000
    #获取私有属性
    def get_money(self):
        return self.__money
    #修改私有属性
    def set_money(self,much):
        self.__money=much
    def make_old_cake(self):
        # Tudi.__init__(self)
        # print("使用%s制作煎饼果子"%self.gongfu)
        #super方法继承
        # super().__init__()
        # super().cake()
        def __info_make(self):
            print(self.gongfu)
            print(self.__money)
    # def master_cake(self):
    #     Master.__init__(self)
    #     Master.cake(self)
    # def school_cake(self):
    #     School.__init__(self)
    #     School.cake(self)
#多层继承
class Tusun(Tudi):
    pass

tom=Tudi()
xiaogang=Tusun()
# print(tom.gongfu)
print(tom.get_money())
tom.set_money(500)
xiaogang.set_money(800)
print(tom.get_money())
print(xiaogang.get_money())
# print(xiaogang.gongfu)
# tom.cake()
# tom.__info_make()
# xiaogang.cake()
# tom.school_cake()
# tom.master_cake()
# xiaogang.cake()
# xiaogang.school_cake()
# xiaogang.master_cake()