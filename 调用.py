# import test2
# test2.add(3,5)

# from test2 import *
# TestA()
# TestB()
import Page1.test11,Page1.test22
Page1.test11.info_print1()
from Page1 import test11
Page1.test11.info_print1()
# from Page1 import test22
Page1.test22.info_print2()