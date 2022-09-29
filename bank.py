#input User, id, deposite, withdraw, transfer money from one account to another.(from their id), delete user[i] (18/09/2022)
import datetime
from datetime import date, datetime
from encodings import search_function
from getpass4 import getpass
import stdiomask
d = date.today()
n = datetime.now()
# parent
class User:
    def __init__(self, name, age, gender, id, pin):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id
        self.pin = pin

    def __str__(self):
        return f"{self.name, self.age, self.gender}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        id = int(input("ID: "))
        pin = int(stdiomask.getpass(prompt="Pin: ", mask = "*"))
        return cls(name, age, gender, id, pin)

# child
class Bank(User):
    lst = []#name, age, gender, balance
    id_lst = []#id
    balance_lst = []# Balance of users
    pin_lst = []# Pin

    def __init__(self, name, age, gender, id, pin):
        super().__init__(name, age, gender, id, pin)
        self.balance = 0
        Bank.lst.append(self)
        Bank.id_lst.append(self.id)
        Bank.balance_lst.append(self.balance)
        Bank.pin_lst.append(self.pin)
    '''
    def deposite(self):
        amount = float(input("Amount($): "))
        self.balance += amount
        print(f"+{amount} -> Balance: {self.balance}$")

    def withdraw(self):
        amount = float(input("Amount: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"-{amount} -> Balance: {self.balance}$")
        else:
            print("Invalid balance! plz-Deposite")
        return self.balance
    '''
    '''def view_balance(self):
        print(f"Name: {self.name} - Age: {self.age} - Gender: {self.gender} - Balance: {self.balance} $")'''

    def view_balance(self):
        print(f"Balance: {self.balance} $")

    '''def send(self):
        i = 0
        amount = float(input("Amount: "))
        if amount >= self.balance:
            self.balance -= amount
            print(f"Balance: {self.balance}") 
    
        return amount'''

    def __repr__(self):
        return f"Name: {self.name} - Age: {self.age} - Gender: {self.gender} - Balance: {self.balance}"


def id_search():
    i = 0
    flag = 0
    idd = int(input("ID: "))
    for i in range(len(Bank.id_lst)):
        if idd == Bank.id_lst[i]:
            flag = 1
            #print("flag: " + str(flag)) command for checking
            #print(Bank.lst[i])
            #print(f"{i} + 68")
            return i
    if flag == 0:
        print("this id doesnt exist")
        return -1


def pin_search():
    i = 0
    flag = 0
    pin = int(stdiomask.getpass(prompt="Pin: ", mask = "*"))
    for i in range(len(Bank.pin_lst)):
        if pin == Bank.pin_lst[i]:
            flag = 1
            #print("flag: " + str(flag))
            #print(Bank.pin_lst[i])
            #print(f"{i} + 68")
            return 1
    if flag == 0:
        print("Wrong")
        return 0

def withdraw(amount):
    k = 0
    Bank.balance_lst[k] -= amount 
    print(f"-{amount} >>> Your balance: {Bank.balance_lst[k]}")
    print(d.strftime("%a, %d, %b, %Y"))
    print(n)


def send(amount):
    z = 0
    Bank.balance_lst[z] += amount 
    print(f"ID: {Bank.id_lst[z]} >>>  +{amount}($) >>> Balance: {Bank.balance_lst[z]}($)")
    print(d.strftime("%a, %d, %b, %Y"))
    print(n)

def menu():
    if not Bank.lst:
        menu_admin()
    n = 0
    while n != 3:
        print("1. admin")
        print("2. user")
        print("3. exit")
        n = int(input("Select 1/2/3: "))
        #print("\n")
        #print("\n")
        if n == 1:
            menu_admin()
        elif n == 2:
            menu_user()
    #print("Thank for using our services")
def menu_admin():
    x = 0
    n = 1
    print("|---------------------|")
    print("|     Add new user    |")
    print("|---------------------|")
    x = Bank.get()
    while n != 3:
        print("1. Add new user")
        print("2. Delete user")
        print("3. exit")
        n = int(input("Select 1/2/3: "))
        if n == 1:
            print("Add new user")
            x = Bank.get()
        if n == 2:
            x = -1
            print("Delete user")
            x = id_search()
            Bank.lst[x] = 0 
            if x != -1:
                print("Complete")
            else:
                print("Fail")


def menu_user():
    print("|----------Tri'sBank----------|")
    print("|       1. Deposite           |")
    print("|       2. Withdraw           |")
    print("|       3. View balance       |")
    print("|       4. Send               |")
    print("|       5. Exit               |")
    print("|-----------------------------|")
    i = 0
    j = 0
    n = 1
    m = 0
    t = False
    x = 0
    y = 0
    while n != 5:
        z = -1
        n = int(input("Select 1/2/3/4/5: "))
        while z == -1:
            z = id_search()
            if z != -1:
                while True:
                        t = pin_search()
                        #sprint(t)
                        j += 1
                        if j == 4:
                            print("1 time remaining")
                            print("to continue press any Num")
                            print('''press 0 to exit''')# get input from user
                            m = int(input("->"))
                            if m == 0:
                                break
                        if j == 5:
                            print("Contact your teller")
                            break
                        if t == 1:
                            break
            if z != -1 and t == 1:
                if n == 1:
                    amount = float(input("Amount($): "))
                    send(amount)
                if n == 2:
                    amount = float(input("Amount($): "))
                    if Bank.balance_lst[z] >= amount:
                        Bank.balance_lst[z] -= amount
                        print(f"-{amount}$ Your balance: {Bank.balance_lst[z]}$ ")
                        print(d.strftime("%a, %d, %b, %Y"))
                        print(n)
                if n == 3:
                        #print("110 - r = ", r)
                        print(Bank.lst[z])
                        print(Bank.balance_lst[z] + "$")
                if n == 4:
                    print("Send money to")
                    q = id_search()
                    if q != -1:
                        amount = float(input("Amount: "))
                        if amount <= Bank.balance_lst[z]:
                            Bank.balance_lst[q] += amount
                            #print(f"q id {Bank.balance_lst[q]}")
                            print(f"ID: {Bank.id_lst[q]}$  +{amount}$")
                        #if amount <= Bank.balance_lst[z]:
                            Bank.balance_lst[z] = Bank.balance_lst[z] - amount
                            #print(f"z id {Bank.balance_lst[z]}")
                            print(f"-{amount} >>> Your balance: {Bank.balance_lst[z]}$")
                            print(d.strftime("%a, %d, %b, %Y"))
                            print(n)
                            print("Money transfer successful")
                        else:
                            print("Unavailable balance")                    
                if n == 5:
                    print("-----------------------------")
                    break

def main():
    menu()
    #print(Bank.lst)
    #print(Bank.id_lst)
    #print(Bank.pin_lst)
    print("Thank for using our services")
if __name__ == "__main__":
    main()