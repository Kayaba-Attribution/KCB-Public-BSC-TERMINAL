from web3 import Web3, contract
import json
import asyncio
from threading import Thread
import webbrowser 

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

# the data for the logs contains the lp address of the token 
# to snipe the token simply add a function that parses the data, returns the lp address for all new txns
# when calling  the sniper pass the contract and the lp contract 
# to trigger the buy use a if statement that compares the token lp address to the lp address found in the mempool
# if they match buy the token

def handle_event(event):
    txn = json.loads(Web3.toJSON(event))
    hash = txn["transactionHash"]
    print(txn["transactionHash"])
    data = txn["data"]
    temp_ = data[26:]
    lp = "0x" + temp_[:40]
    print("LP ADDRESS: 0x" + temp_[:40])
    url = 'https://bscscan.com/tx/' + hash 
    webbrowser.open_new(url)
    url_lp = 'https://bscscan.com/address/' + lp 
    webbrowser.open_new(url_lp)
    # print(txn)
    # and whatever

async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
    event_filter = web3.eth.filter({"address": web3.toChecksumAddress(('0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73').upper()), "block_identifier": 'pending', })
    #event_filter = contract.events.Here.createFilter(fromBlock='latest')
    # block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()