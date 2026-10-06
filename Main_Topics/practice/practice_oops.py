"""
method over loading: means when we have multiple methods with same name but different parameters in the same class, it is called method overloading.
method overriding: means when we have a method in the child class with same name and same parameters as in the parent class, it is called method overriding.


"""
#access modifier / specifiers: public, __private, _protected
class X:
    def timepass(self,name,_age,__salary):
        self.nsme=name
        self._age=_age
        self.__salary=__salary
    
    def display(self):
        print("Name:",self.nsme)
        print("Age:",self._age)
        print("Salary:",self.__salary)
x=X()
x.timepass("Alice", 25, 50000)
x.display()
