'''class shopping:
    item='phone'
    cost=700
    def collection(self):
        print(shopping.item)
        print(shopping.cost)
s=shopping()
s.collection()'''
'''
class bank:
    def total_amount(self,amount):
        self.amount=amount
        print(f'Total Balance is:{self.amount}')
        
    def deposite(self,bal):
        self.amount=self.amount+bal
        print(f'after dep total amount is:{self.amount}')
        
    def withdraw(self,bal):
        self.amount=self.amount-bal
        print(f'after withdraw from the balance is:{self.amount}')       
    
b=bank()
b.total_amount(2000)
b.deposite(500)
b.withdraw(1000) 



#  4 def product name cost total product addresss
class flipkart:
    product_name="laptop"
    cost=450000
    total_product=5
    add="pune"
    
    def product_data(self):
        print(f'product name is {self.product_name}\n'
              f'toal cost is {self.cost}\n'
              f'total product is {self.total_product}\n')
        
    def address(self):
        print(f'current address is {self.add}')
        
        
    def modification_data(self,new_cost,TP):
        self.cost=new_cost
        self.total_product=TP
        print(f'after modification cost is {self.cost}\n'
              f'total product is {self.total_product}')
        
        
        
        
        
        
f=flipkart()
f.product_data()
f.address()
f.modification_data(500000,20)
print()
print(f.add)
print(f.cost)
        '''
        
'''

class test:
    sub="python"
    fee=20000
    
    def data(self):
        print(self.sub)
        print(self.fee)
        
        print('modification')
    
        self.sub="aman"
        self.fee=1000
        print(self.sub)
        print(self.fee)
        
t=test()
t.data()
'''
'''
class Bank:
    def Total_Balance(self,amount):
        self.amount=amount
        print(f'Total Balance is {self.amount}')

    def Deposit(self,bal):  #+
        self.bal=bal
        self.amount+=self.bal
        # 20000=20000+5000 self.amount+=bal
        print(f'After deposit Total amount is {self.amount}')

    def withdrawal(self,bal): #-
        self.bal=bal
        self.amount-=self.bal
        print(f'After withdrawal total amount is {self.amount}')

b=Bank()
b.Total_Balance(20000)
b.Deposit(5000)
b.withdrawal(9500)
'''
print()
'''
class Bank:
    def Total_Balance(self):
        self.amount=5000
        print(f'Total Balance is {self.amount}')

    def Deposit(self,bal):  #+
        self.bal=bal
        self.amount+=self.bal
        # 20000=20000+5000 self.amount+=bal
        print(f'After deposit Total amount is {self.amount}')

    def withdrawal(self,bal): #-
        self.bal=bal
        self.amount-=self.bal
        print(f'After withdrawal total amount is {self.amount}')

b=Bank()
b.Total_Balance()
b.Deposit(5000)
b.withdrawal(9500)
'''








'''
class Flipkart:
    Product_name="Laptop"
    cost=45000
    total_product=5
    add="Pune"

    def Product_Data(self):
        print(f'Product name is {self.Product_name}\n'
              f'Total Cost is {self.cost}\n'
              f'Total product is {self.total_product}')
        print()
        self.cost = 1000
        self.total_product = 500
        self.add = "Pune5"
        print(f'Updated Cost price is {self.cost}\n'
              f'Updated Total product is {self.total_product}\n'
              f'Updated Address is {self.add}')

    def Address(self):
        print(f'Current Address is {self.add}')

    
    def Modification_data(self,new_cost,TP,add):
        self.cost=new_cost
        self.total_product=TP
        self.add=add
        print(f'Updated Cost price is {self.cost}\n'
              f'Updated Total product is {self.total_product}\n'
              f'Updated Address is {self.add}')

    
    
    def Modification_data(self):
        self.cost=1000
        self.total_product=500
        self.add="Pune5"
        print(f'Updated Cost price is {self.cost}\n'
              f'Updated Total product is {self.total_product}\n'
              f'Updated Address is {self.add}')
    
    
f=Flipkart()
f.Product_Data()
f.Address()
print()
print()
print(f.add)
print(f.cost)
print(f.total_product)
print(f.Product_name)
'''
