class A:
    def student_data(self,name,age):
        self.name=name
        self.age=age
        print(f'student Name is {self.name}\n'
              f'student age is {self.age}')

class B(A):
    def student_data(self,name,age,sub,roll_no):
        self.sub=sub
        self.roll_no=roll_no
        A.student_data(self,name,age)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student Roll Number is {self.roll_no}')
class C(A):
    def student_data(self,name,age,sub,roll_no):
        self.sub=sub
        self.roll_no=roll_no
        A.student_data(self,name,age)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student Roll Number is {self.roll_no}')
class D(B,C):
    def student_data(self,name,age,sub,roll_no):
        self.sub=sub
        self.roll_no=roll_no
        B.student_data(self,name,age,sub,roll_no)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student Roll Number is {self.roll_no}')
    
d=D()
d.student_data("Aman",23,"Python","P1234")
