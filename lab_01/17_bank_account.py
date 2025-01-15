class BankAccount:
    def __init__(self, balance, account_number, deposit=0, withdraw=0):
        self.__balance = balance
        self.__account_number = account_number
        self.__withdraw = withdraw
        self.__deposit = deposit

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def deposit_withdraw(self):
        if (self.__deposit != 0):
            balance = (self.__balance)+(self.__deposit)
            return balance
        else:
            balance = (self.__balance) - (self.__withdraw)
            return balance

    def __str__(self):
        return (f"The account number is {self.__account_number}.\nBalance={self.__balance}\nDeposit={self.__deposit}\nWithdraw={
            self.__withdraw}\nAmount_after_transaction ={self.deposit_withdraw()}")


first_account = BankAccount(2000, 201570, 300, 0)
print(first_account)
# second_account = BankAccount(4000, 20178, 0, 600)
# print(second_account.__str__())

# Getting the balance throung mangling
print(f"The balance= {first_account._BankAccount__balance}")
