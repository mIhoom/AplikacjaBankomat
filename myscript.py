from bankaccount import BankAccount, Result, MinimumBalanceAccount


# konto = BankAccount(500)

# amountToWithdraw = 700

# result = konto.try_withdraw(amountToWithdraw)

# if (result.isSuccess):
#     print(result.message)
#     print("Propozycja zakupu nowej karty, ubezpieczenia, itd.")
# else:
#     print(result.message)


accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(600)

accountMin.deposit(500)

print(result.message)

