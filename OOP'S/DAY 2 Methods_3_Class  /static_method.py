'''
class School:
    @staticmethod
    def demo():
        print("Static Method")
'''
'''
s=School()
s.demo()
'''
'''
School.demo()
'''

'''
class Operations:
    @staticmethod
    def ADD(a,b):
        return a+b

    @staticmethod
    def SUB(x,y):
        return x-y

    @staticmethod
    def MUL(P,Q):
        return P*Q

h=Operations()
print(h.ADD(1,4))
print(h.SUB(5,10))
print(h.MUL(10,20))
'''

'''
class Total:
    sal=1000
    @staticmethod
    def Information():
        print(Total.sal)
        print("First method")

    @staticmethod
    def show():
        Total.sal=5000
        print(Total.sal)
        print("show method")

t=Total()
t.Information()
http://t.show()
'''
'''
class Total:
    sal=1000
    @staticmethod
    def Information(a):
        print(a.sal)
        print("First method")

    @staticmethod
    def show():
        print("show method")

t=Total()
t.Information(t)
'''
'''
class Check:
    data="Information"
    def Method1(self):
        print(http://self.data)

    @classmethod
    def method2(cls):
        print(http://cls.data)

    @staticmethod
    def method3():
        print(http://Check.data)

s=Check()
s.Method1()
s.method2()
s.method3()

print("Calling By useing Class Name")
Check.Method1(s)
Check.method2()
Check.method3()
'''

'''class Data:
    def spam(a,b):
        print(a+b)
        print("Data")
# Data.spam(10,20)
d=Data()
d.spam(1,2)'''

"""
spam()------>method

Data.spam()



"""
