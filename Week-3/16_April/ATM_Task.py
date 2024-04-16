account_data = {}

class ATM:
    def __init__(self):
        self.name = input('Enter Your Name: ')
        if self.name in account_data:
            print("Name already registered! Plz Choose Another Options [2/3/4]")
        else:
            account_data[self.name] = 0
            print("Account created successfully!")
    
    def Credit(self):
        print(f'Balance: {account_data[self.name]} Rs')
        amount = int(input('Add Money to Your Account: '))
        account_data[self.name] += amount
        print(f'{self.name}, {amount} Rs Credited. Balance: {account_data[self.name]} Rs')

    def Debit(self):
        print(f'Balance: {account_data[self.name]} Rs')
        amount = int(input('Enter amount to debit: '))
        if account_data[self.name] >= amount:
            account_data[self.name] -= amount
            print(f'{self.name}, {amount} Rs Debited. Balance: {account_data[self.name]} Rs')
        else:
            print("Empty Account!")

    def Display_Details(self):
        print(f'{self.name} has {account_data[self.name]} Rs Balance')

obj1 = None

while True:
    ch = int(input('''
*********** Welcome To Bank *********** 
    Choose 1 To Open Account With Your Name
    Choose 2 To Add Money to Your Account
    Choose 3 To Debit Money From Your Account
    Choose 4 To Show Details
    Choose 5 To Exit
       Enter : '''))
    if ch == 5:
        exit()
    elif ch == 1:
        if not obj1:
            obj1 = ATM()
        else:
            print("Account already opened!")
    elif ch == 2:
        if obj1:
            obj1.Credit()
        else:
            print("Please open an account first!")
    elif ch == 3:
        if obj1:
            obj1.Debit()
        else:
            print("Please open an account first!")
    elif ch == 4:
        if obj1:
            obj1.Display_Details()
        else:
            print("Please open an account first!")
    else:
        print('Please Enter a Valid Input [1/2/3/4/5]')
