class BankAccount:
    def __init__(self,balance=0, int_rate=1, holder= 'Default'):
        self.balance = balance
        self.int_rate = int_rate
        self.accountHolder = holder

    
    def print_balance(self):
        print('Your balance, MISTER, ', self.accountHolder, 'is: ', self.balance)
        return self
    
    def deposit_money(self, ammount):
        self.balance += ammount
        return self
    
    def withdraw_money(self, ammount):
        if self.balance > ammount:
            self.balance -= ammount
        else:
            print('You dont have enough money. Get it together')
        return self
    
    def transfer_money(self, receiver, ammount):
        if self.balance > ammount:
            receiver.account.deposit_money(20)
            self.withdraw_money(ammount)
        else:
            print('You dont have enough money. Get it together')
        return self


class User:	
    numberOfUsersRegistered = 0
    def __init__(self,firstName='Default', lastName='default', age=100):
        self.first_name = firstName
        self.last_name = lastName
        self.age = age
        self.account = BankAccount(balance=100, int_rate=0.0, holder = self.first_name)	




    @classmethod
    def increaseNrOfUsers(cls):
        cls.numberOfUsersRegistered = cls.numberOfUsersRegistered+1
        return cls
    
    def say_name(self):
        print('My name is ' ,self.first_name, 'and my last name is ', self.last_name)
        return self

    @classmethod
    def printNrOfUsers(cls):
        print(cls.numberOfUsersRegistered)
        return cls
    
    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name'])<2:
            print("Emri duhet me i madh se dy karaktere", 'emri')
            is_valid = False
        if len(user['last_name'])<2:
            print("Mbiemri duhet me i madh se dy karaktere", 'emri')
            is_valid = False
        return is_valid






endi = User('Endi', 'Mimini', 25)
flogert = User('Flogert', 'Ciku', 25)

endi.account.print_balance().deposit_money(25).print_balance().withdraw_money(100).print_balance()
endi.account.transfer_money(flogert, 20).print_balance()
flogert.account.print_balance()