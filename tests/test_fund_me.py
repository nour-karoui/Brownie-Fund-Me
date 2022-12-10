from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions, reverts
import pytest
import brownie

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    contract_balance = fund_me.balance()
    assert fund_me.addressToAmountFunded(account) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account) == 0

def test_can_only_withdraw_if_admin():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local blockchain")
    account = get_account()
    fund_me = deploy_fund_me()
    maleficent_account = accounts[1]
    print('here is the maleficent account:', maleficent_account.balance())
    with pytest.raises(Exception):
        tx2 = fund_me.withdraw({"from": maleficent_account})