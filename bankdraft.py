# parent
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name, self.age, self.gender}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return cls(name, age, gender)

# child
class Bank(User):
    lst = []
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        Bank.lst.append(self)
    def deposite(self):
        amount = float(input("Amount: "))
        self.balance += amount
        print(f"+{amount} -> Balance: {self.balance}")

    def withdraw(self):
        amount = float(input("Amount: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"-{amount} -> Balance: {self.balance}")
        else:
            print("Invalid balance! plz-Deposite")

    def view_balance(self):
        print(f"Name: {self.name} - Age: {self.age} - Gender: {self.gender} - Balance: {self.balance}")

    def __repr__(self):
        return f"Name: {self.name} - Age: {self.age} - Gender: {self.gender} - Balance: {self.balance}"
def menu():
    print("|----------Tri'sBank----------|")
    print("|       1. New User           |")
    print("|       2. Deposite           |")
    print("|       3. Withdraw           |")
    print("|       4. View balance       |")
    print("|       5. Exit               |")
    print("|-----------------------------|")
    n = 1
    while n != 5:
        n = int(input("Select 1/2/3/4/5: "))
        if n == 1:
            x = Bank.get()

        if n == 2:
            x.deposite()
        if n == 3:
            x.withdraw()
        if n == 4:
            x.view_balance()
        if n == 5:
            print("Thank for using our services")


def main():
    menu()
    print(Bank.lst)

if __name__ == "__main__":
    main()
