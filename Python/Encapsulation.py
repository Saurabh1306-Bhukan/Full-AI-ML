# Encapsulation: 
# Wrapping data & functions into single unit

# private: 
#     - can only be accessed within the class
#     - cannot be accessed outside the class
#     - write __ before the variable name to make it private

# public:
#     - can be accessed within the class
#     - can be accessed outside the class

# protected:
#     - can be accessed within the class
#     - can be accessed outside the class but should not be accessed outside the class (convention)
#     - write  _ before the variable name to make it protected


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance    # private

    def get_balance(self):    # getter
        return self.__balance

    def set_balance(self, newBalance):  # setter
        self.__balance = newBalance


acc1 =  BankAccount("rahul", 100_000)

acc1.set_balance(200_000)

print(acc1.name, acc1._BankAccount__balance)  # acc.__balance
    



