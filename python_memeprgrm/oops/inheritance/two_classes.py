class One:
    def method1(self):
        print('this is method1 from class One')
        
class Two:
    def method2(self):
        # obj_one=One()
        # obj_one.method1()
        print('this is method2 from class Two')

def test():
    obj1=One()
    obj1.method1()
    
    obj2=Two()
    obj2.method2()
    

test()