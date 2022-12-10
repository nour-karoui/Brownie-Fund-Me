from brownie import FundMe, config, accounts, network, MockV3Aggregator
from .helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    # pass the price feed address to the fund me contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        feed_price_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"The network is {network.show_active()}")
        feed_price_address = deploy_mocks()
    fund_me = FundMe.deploy(
        feed_price_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print(f"Contract Deployed to: {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()