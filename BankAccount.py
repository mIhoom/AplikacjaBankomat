class Result:
    def __init__(self, isSuccess, message, value=None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """tu jest coś co sprawdza, czy pieniądze są ok"""
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return Result(True, "Wypłacono gotówkę", amount)

        return Result(False, "Nie wypłacono gotówki. Brak wystarczających środków na koncie ", amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumbalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumbalance

    def try_withdraw(self, amount):
        if(self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)

        else:
            return Result(False, "Nie wypłacono gotówki. Przekroczono limit dostępnych środków na koncie", amount)

