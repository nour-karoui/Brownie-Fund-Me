from brownie import FundMe
from .helpful_scripts import get_account

class bcolors:
    WARNING = '\033[93m'
def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print("Entrance Fee: " + str(entrance_fee))
    print(f"{bcolors.WARNING} here is the contract balance before the funding:  {fund_me.balance()}")
    fund_transaction = fund_me.fund({"from": account, "value": 1})
    fund_transaction.wait(1)
    print(f"{bcolors.WARNING} here is the balance after the funding:  {account.balance()}")

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"{bcolors.WARNING} here is the contract balance after the funding:  {fund_me.balance()}")
    withdraw_transaction = fund_me.withdraw({"from": account})
    withdraw_transaction.wait(1)
    print(f"{bcolors.WARNING} here is the balance after the withdrawal:  {account.balance()}")
    print(f"{bcolors.WARNING} here is the contract balance after the withdrawal:  {fund_me.balance()}")

def main():
    fund()
    withdraw()