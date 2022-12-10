from brownie import config, network, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
DECIMALS = 18
STARTING_PRICE = 20000000000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
        #     account = accounts.load("storage_account")

def deploy_mocks():
    account = get_account()
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
    return MockV3Aggregator[-1].address
    print("Mocks Deployed...")