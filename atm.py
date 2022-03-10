import random

class Automatic_Teller_Machine(object):
    def __init__(self, card_num, pin):
        self.card_num = card_num
        self.pin = pin
    
    def check_balance(self):
        print("Checking your balance..")
        print("Your balance is - " + str(balance) + "$")
    
    def cash_withdraw(self):
        withdrawn_amount = int(input("enter the amount to be withdrawn - "))
        remaining_amount = int(balance - withdrawn_amount)

        if(withdrawn_amount > balance):
            print("flyng high.. you don't have enough balance.")
            print("withdraw something below " + str(balance) + "$")
            withdrawn_amount = int(input("enter the amount to be withdrawn - "))
        elif(withdrawn_amount < balance & withdrawn_amount > 0):
            print("processing the withdraw..")
            print("Successfully withdrew " + str(balance) + "$")
            print("you are left with " + str(remaining_amount) + "$")


balance = random.randrange(300,500)

card_num = input("enter your card number - ")
pin_num = input("Enter the pin - ")

auto_tlr_mach = Automatic_Teller_Machine(card_num, pin_num)
enter_act = int(input("enter (1) to check balance, (2) to withdraw Cash.. - "))

if enter_act==1:
    auto_tlr_mach.check_balance()
elif enter_act==2:
    auto_tlr_mach.cash_withdraw()