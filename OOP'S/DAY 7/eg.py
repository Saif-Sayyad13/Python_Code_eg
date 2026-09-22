
'''using encoplusation concep acc no pin and user detiles pass karna hai user detiles private
withdrewa dep methods inheridance use  in current and saving acc and poly use we have to use display 
main class bank   
class saving class current 
it should use all the oops conceppt except abstraction'''
     
'''       
class Bank:
    def __init__(self, bank_name, user, _accountno, __pin):
        self.bank_name = bank_name
        self.__user = user
        self._accountno = _accountno
        self.__pin = __pin
        
        print(f'Bank Name is {self.bank_name}\nUser name is {self.__user}\nUser Account number is {self._accountno}\n')
        
    def info(self, name, bal):
        self.name = name
        self.bal = bal
        
    def check_pin(self, entered_pin):
        return self.__pin == entered_pin


class Saving(Bank):
    def data(self, sbal, totalbal):
        self.sbal = sbal
        self.totalbal = totalbal
        print(f'Total balance is  {self.totalbal}')
        
    def deposit(self, amount):
        self.amount = amount
        self.totalbal = self.totalbal + self.amount
        print(f'Deposit amount is {self.amount}\nTotal amount is {self.totalbal}\n')
        
    def withdraw(self, amount2, entered_pin):
        self.amount2 = amount2

        if self.check_pin(entered_pin):
            if self.amount2 <= self.totalbal:
                self.totalbal = self.totalbal - self.amount2
                print(f'Amount withdrawn is {self.amount2}\nRemaining Balance is {self.totalbal}\n')
            else:
                print("Insufficient balance\n")
        else:
            print(" Incorrect Pin \n")

    def display(self):
        print("Saving account data is ")
        print(f"Bank: {self.bank_name} | Account: {self._accountno} | Balance: {self.totalbal}\n")

class Current(Bank):
    def data(self, cbal, totalbal):
        self.cbal = cbal
        self.totalbal = totalbal
        print(f'Total balance in current account is {self.totalbal}')
        
    def deposit(self, amount):
        self.amount = amount
        self.totalbal = self.totalbal + self.amount
        print(f'Deposit Amount is {self.amount}\nTotal amount is {self.totalbal}\n')
        
    def withdraw(self, amount2, entered_pin):
        self.amount2 = amount2
        if self.check_pin(entered_pin):
            if self.amount2 <= self.totalbal:
                self.totalbal = self.totalbal - self.amount2
                print(f'Amount withdrawn from Current is {self.amount2}\nRemaining Balance is {self.totalbal}\n')
            else:
                print("Insufficient balance in Current Account!\n")
        else:
            print(" Incorrect PIN! Transaction Denied.\n")

    def display(self):
        print("--- CURRENT ACCOUNT DISPLAY ---")
        print(f"Bank: {self.bank_name} | Account: {self._accountno} | Current Balance: {self.totalbal}\n")


print("=== Creating Savings Account ===")
sav = Saving("SBI Bank", "Rahul", "SBI992211", 1234)
sav.data(5000, 5000)

print("-> Attempting withdrawal with wrong PIN:")
sav.withdraw(1000, 9999)

print("-> Attempting withdrawal with correct PIN:")
sav.withdraw(1500, 1234)

sav.display()


print("=== Creating Current Account ===")
curr = Current("HDFC Bank", "Amit", "HDFC554433", 4321)
curr.data(10000, 10000)

print("-> Attempting current withdrawal with correct PIN:")
curr.withdraw(3000, 4321)

curr.display()
'''