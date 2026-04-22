print("=== ENCAPSULATION ===")

'''                                                  N O T E S

IN languages like c++, java, PhP, Typescript Encapsulation works in following way => public, private, protected.
IN Python => for public = just the "name", 
             for private = __ (private)
             for protected = _ (protected)
'''


class Account():
    description = "The class makes bank accounts"

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    def getBalance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property  # GETTER
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_holder):
        print("holder_setter:", new_holder)
        self.__owner = new_holder

    def changeOwnership(self, new_owner):
        print("change ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Zikirullo", 1000)
my_account.getBalance()

my_account.deposit(4000)
my_account.withdraw(400)
my_account.getBalance()

#   Questions
# my_account.__amount = 1000000
# my_account.__owner = "Le vi"
# print(my_account.__owner)

try:
    result = my_account.__owner
    print("result:", result)
except Exception as err:
    print("The targe state is not found:", err)

print("=== Getter/Setter ===")

print("owner before:", my_account.holder)
# my_account.changeOwnership("Alex")

my_account.holder = "Alex"
print("owner now:", my_account.holder)
