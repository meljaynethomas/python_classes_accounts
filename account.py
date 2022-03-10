class Account:
    # public class variable
    numCreated = 0

    def __init__(self, initial):
        # private class variable
        self.__balance = initial
        Account.numCreated += 1


    # Methods below:
    def deposit(self, amt):
        self.__balance += amt
        return

    def withdraw(self, amt):
        self.__balance -= amt
        return

    # getter
    def getbalance(self):
        return self.__balance

    def get_holder_name(self):
        return self.__holder_name

    # setter
    def set_holder_name(self, name):
        self.__holder_name = name

    def __str__(self):
        return "Account has balance " + str(self.getbalance())

    # need this code to run total_balance2 code in practice_instantiation file:
    def __add__(self, other):
        return self.getbalance() + other.getbalance()



