import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

def check_multiplicity(amount):
    if amount%MULTIPLICITY != 0:
        print("Сумма должна быть кратной 50 у.е.")
        return False
    return True
def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")

def withdraw(amount):
    global bank_account
    check_multiplicity(amount)

    comission = decimal.Decimal(amount * PERCENT_REMOVAL)
    if comission <= MIN_REMOVAL:
        comission = MIN_REMOVAL
    elif comission >= MAX_REMOVAL:
        comission = MAX_REMOVAL
    else:
        comission = amount * PERCENT_REMOVAL

    if bank_account>= (amount+comission):
            bank_account-= (amount+comission)
            operations.append(f"Снятие с карты {amount} у.е. Процент за снятие {comission} у.е.. Итого {bank_account} у.е.")
    else:
            operations.append(f"Недостаточно средств. Сумма с комиссией {amount + comission} у.е. На карте {bank_account} у.е.")



def exit():
    global bank_account
    if bank_account >= RICHNESS_SUM:
        operations.append(f"Вычтен налог на богатство 0.1% в сумме {RICHNESS_PERCENT*bank_account}000 у.е. Итого {bank_account-(RICHNESS_PERCENT*bank_account)}000 у.е.")
        bank_account -= RICHNESS_PERCENT * bank_account
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")

deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)