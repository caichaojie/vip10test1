class Dog(object):
    def work(self):
        print("指哪打哪儿")
class Jingdog(Dog):
    def work(self):
        print("追击犯人")
class Dudog(Dog):
    def work(self):
        print("追查毒品")
class Person(object):
    def work_with_dog(self,dog):
        dog.work()
tom=Jingdog()
dg=Dudog()
Dbing=Person()
Dbing.work_with_dog(tom)
Dbing.work_with_dog(dg)