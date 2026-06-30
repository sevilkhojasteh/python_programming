class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Amount must be greater than balance")
        self._balance -= amount
        return self._balance
    


def main():
    account = Account()
    print(account.balance)
    account.deposit(100)
    print(account.balance)
    account.withdraw(50)
    print(account.balance)


if __name__ == "__main__":
    main()