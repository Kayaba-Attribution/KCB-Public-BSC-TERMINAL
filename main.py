
from eth_utils import address
from toolz.functoolz import return_none
from web3 import Web3
import json
import wallets
import emoji
import timeit
from datetime import datetime
import time
from urllib.request import Request, urlopen
import random

import webbrowser 

#import config

bsc = "https://bsc-dataseed.binance.org/"
#bsc = "https://bsc-mainnet.web3api.com/v1/E9C73WWUBACG3BTVDR5KVRSXHM3YGFDCGS"
#bsc = "https://data-seed-prebsc-1-s1.binance.org:8545"
web3 = Web3(Web3.HTTPProvider(bsc))

main_address = "0xfef916b01ff9a0f2b8a2b2fe3144221d9b265c8e"
contract = ""
pancake = ""
gas = "5"
verified = ""

erudite = {}
quick_erudite = {}

# BASIC KCB CONNECTIONS

def connection():
    global contract
    global pancake
    print(emoji.emojize("""
    -------------------------------------------
    :rocket::rocket::rocket:  KAYABA CRYPTO TRADING BOT :rocket::rocket::rocket:
    -------------------------------------------""", variant="emoji_type"))
    print("Connecting to Web3 Provider.....\n")
    if(web3.isConnected()):
        print(emoji.emojize(":check_mark_button: Connection Success!",variant="emoji_type"))
        contract = contract_connection(main_address)
        print(emoji.emojize(":check_mark_button: Contract object Created!",variant="emoji_type"))
        pancake = pancake_router()
        print(emoji.emojize(":check_mark_button: Pancake Router V2 connected!\n",variant="emoji_type"))
        print("Ready to play!")
        update("")
        choose_function()
    else:
        print("Connection Failed!\n")
        choose_function()

def contract_connection(contract_input):
    contract_address =  web3.toChecksumAddress((contract_input).upper()) #be sure to use a BSC Address in uppercase format like this 0x9F0818B... 

    abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"minTokensBeforeSwap","type":"uint256"}],"name":"MinTokensBeforeSwapUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SwapAndLiquifyEnabledUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"_liquidityFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"enableTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"geUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"lock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidityFee","type":"uint256"}],"name":"setLiquidityFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxPercent","type":"uint256"}],"name":"setMaxTxPercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setSwapAndLiquifyEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"taxFee","type":"uint256"}],"name":"setTaxFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapAndLiquifyEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tradingEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')

    contract = web3.eth.contract(address=contract_address, abi=abi)

    return contract

def pancake_router():
    contract_address =  web3.toChecksumAddress(('0x10ED43C718714eb63d5aA57B78B54704E256024E').upper()) #be sure to use a BSC Address in uppercase format like this 0x9F0818B... 

    abi = json.loads('[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')

    contract = web3.eth.contract(address=contract_address, abi=abi)

    return contract

def update(packet):
    global erudite
    global contract
    erudite["name"] = contract.functions.name().call()
    erudite["symbol"] = contract.functions.symbol().call()
    erudite["decimals_raw"] = contract.functions.decimals().call() 
    erudite["DECIMALS"] =  10 ** erudite["decimals_raw"]
    erudite["supply_raw"] = contract.functions.totalSupply().call()
    erudite["supply"] = int(erudite["supply_raw"] // erudite["DECIMALS"])
    erudite["supply_human"] = "{:,}".format(erudite["supply"])
    try:
        erudite["owner"] = contract.functions.owner().call()
    except Exception as err:
        erudite["owner"] = "---"

    try:
        erudite["max_raw"] = contract.functions._maxTxAmount().call()
        erudite["max_%"] = (erudite["max_raw"] / erudite["supply_raw"]) * 100 
    except Exception as err:
        erudite["max_raw"] = "---"
        erudite["max_%"] = "--- "

    print("\nErudite finished learning")

    #print(erudite)
    
def quick_update(wallet):
    global contract
    global quick_erudite

    raw_info = wallets.wallet_info_all(wallet)
    DECIMALS = erudite["DECIMALS"]
    raw_balanceOf = contract.functions.balanceOf(raw_info[0]).call()
    balanceOf = raw_balanceOf // DECIMALS

    result = web3.eth.get_balance(raw_info[0])
    wallet_balance = (float(web3.fromWei(result, "ether")))

    quick_erudite["tokens"] =  balanceOf
    quick_erudite["bnb"] = wallet_balance

    print("\nQuick Erudite up to date")
    
#### WORKINNG FUNCTIONS ####

## TRADING FUNCRIONS ###

def launch(packet, type):

    logs = open("logs.txt","a")

    if type == "manual":
        launch = input("LAUNCH? ")
        if launch == "":
            web3.eth.sendRawTransaction(packet[0].rawTransaction)
            print(packet[1])
            print("Waiting for confirmation...\n")
            web3.eth.wait_for_transaction_receipt(packet[3])
            _now = now()

            receipt = web3.eth.getTransactionReceipt(packet[3])
            if receipt['status'] == 1:
                log = f"{_now}  [SUCCESS] [auto] {packet[4]}"
                logs.write(f"{log} \n")
                logs.close()
                print("Transaction Succesfull! and log recorded!\n")
            else:
                log = f"{_now}  [FAILED] [auto] {packet[4]}"
                logs.write(f"{log} \n")
                logs.close()
                print("txn failed :( and log recorded!\n")

         
            url = 'https://bscscan.com/tx/' + packet[3]
            print(url)
            return
        else:
            print("\nTRANSACTION ABORT")
            return

    if type == "auto":
        web3.eth.sendRawTransaction(packet[0].rawTransaction)
        print(packet[1])
        print("Waiting for confirmation...\n")
        web3.eth.wait_for_transaction_receipt(packet[3])
        _now = now()

        receipt = web3.eth.getTransactionReceipt(packet[3])
        if receipt['status'] == 1:
            log = f"{_now}  [SUCCESS] [auto] {packet[4]}"
            logs.write(f"{log} \n")
            logs.close()
            print("Transaction Succesfull! and log recorded!\n")
        else:
            log = f"{_now}  [FAILED] [auto] {packet[4]}"
            logs.write(f"{log} \n")
            logs.close()
            print("txn failed :( and log recorded!\n")
            print(emoji.emojize("\n:police_car_light::warning:  COULDNT SELL :warning: :police_car_light:",variant="emoji_type"))
            

        
        url = 'https://bscscan.com/tx/' + packet[3]
        print(url)
        return

    if type == "check":
        web3.eth.sendRawTransaction(packet[0].rawTransaction)
        #print(packet[1])
        print("NO WAIT!\n")
        #web3.eth.wait_for_transaction_receipt(packet[3])
        logs.close()
        
        url = 'https://bscscan.com/tx/' + packet[3]
        print(url)
        return


def transfer_tokens(packet):

    sender = wallets.wallet_info_all(packet[1])
    reciever = wallets.wallet_info_all(packet[2])

    global contract
    global erudite
    global quick_erudite
    global gas

    quick_update(packet[1])

    # query sender token amount
    name = erudite["name"]
    decimals = erudite["decimals_raw"]

    balanceOf = quick_erudite["tokens"]

    if packet[3] == "max":
        aumount = balanceOf - 1
    else:
        aumount = int(packet[3])


    #print(decimals)
    amount = aumount * (10 ** decimals)
  
    #print(amount)

    nonce = web3.eth.getTransactionCount(sender[0])
    #print(nonce)

    token_tx = contract.functions.transfer(reciever[0], amount).buildTransaction(
        {
            'chainId':56,
            'gas': 300000,
            'gasPrice': web3.toWei(gas,'gwei'),
            'nonce':nonce
        }
    )
    print(f"\nTransfer Transaction Build Succesfully\n")

    sign_txn = web3.eth.account.signTransaction(token_tx, private_key=sender[1])

    hash = sign_txn.hash.hex()

    print(f"Transaction sends {aumount} to {packet[2]}\n")

    launch_message = f"Transaction has been sent from {packet[1]} to {packet[2]} \n--> Tx Hash: {hash}\n"
    logs_message = f"Tranfer from {packet[1]} to {packet[2]} for {aumount} {name} --> Tx Hash: {hash}"

    ammo =  [sign_txn, launch_message, token_tx, hash, logs_message]

    #print(packet[4])
    if packet[4] == "manual":
        launch(ammo, "manual")
        choose_function()
    elif packet[4] == "auto":
        launch(ammo, "auto")
        choose_function()

def buy_tokens(packet):

    global contract
    global main_address
    global pancake
    global erudite
    global quick_erudite
    global gas

    reciever = wallets.wallet_info_all(packet[1])
    bnb = float(packet[2])

    nonce = web3.eth.getTransactionCount(reciever[0])

    token = web3.toChecksumAddress((main_address))
    wBnb = web3.toChecksumAddress(('BB4CDB9CBD36B01BD1CBAEBF2DE08D9173BC095C'))
   
    path = [wBnb, token]

    t_name = erudite["name"]

    now = int(time.time())
    #print(now)

    expire = now + 900

    #print(expire)

    bnb_amount = Web3.toWei(bnb, 'ether')
    
    #aprox_gas = pancake.functions.swapExactETHForTokens(0, path, reciever[0],expire ).estimateGas()
    #print(aprox_gas)
    token_tx = pancake.functions.swapExactETHForTokens(0, path, reciever[0],expire ).buildTransaction(
        {
            'chainId':56,
            'value': bnb_amount,
            'gas': 600000,
            'gasPrice': web3.toWei(gas,'gwei'),
            'nonce':nonce,
        }
    )
    print(f"\n ++++ BUY Transaction Build Successfully ++++ \n")

    sign_txn = web3.eth.account.signTransaction(token_tx, private_key=reciever[1])

    hash = sign_txn.hash.hex()

    print(f"Transaction buys {bnb} worth of {t_name} tokens...\n")

  
    #web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    launch_message = f"Transaction has been launched to pancake router \n--> Tx Hash: {hash}\n"

    logs_message = f"Buy with {packet[1]} {bnb} BNB worth of {t_name} tokens --> Tx Hash: {hash}"
   

    ammo = [sign_txn, launch_message, token_tx, hash, logs_message]

    if packet[3] == "manual":
        launch(ammo, "manual")
        choose_function()
    elif packet[3] == "auto":
        launch(ammo, "auto")
        choose_function()
    elif packet[3] == "check":
        launch(ammo, "auto")
        return

def sell_tokens(packet):
    start = timeit.default_timer()
    
    global main_address
    global pancake
    global erudite
    global quick_erudite
    global gas

    reciever = wallets.wallet_info_all(packet[1])
    quick_update(packet[1])
    tokens = packet[2]
    nonce = web3.eth.getTransactionCount(reciever[0])

    decimals = erudite["decimals_raw"]

    balanceOf = quick_erudite["tokens"]
    t_name = contract.functions.name().call()

    if tokens == "max":
        tokens = int(balanceOf - 1)

    if tokens == "half":
        tokens = int(balanceOf/2)
    else:
        tokens = int(packet[2])
        #print(f"Selling max value: {tokens}")
    
    #print(decimals)
    tokens_amount = tokens * (10 ** decimals)

    token = web3.toChecksumAddress((main_address))
    wBnb = web3.toChecksumAddress(('BB4CDB9CBD36B01BD1CBAEBF2DE08D9173BC095C'))
   
 

    path = [token, wBnb]

    now = int(time.time())
    #print(now)

    expire = now + 900

    #print(expire)

    #tokens_amount = Web3.toWei(tokens, 'ether')
    
    #aprox_gas = pancake.functions.swapExactETHForTokens(0, path, reciever[0],expire ).estimateGas()
    '''
    print(f"""
    {tokens_amount}
    0
    {path}
    {reciever[0]}
    {expire}""")
    #print(aprox_gas)
    '''
    #print(gas)
    token_tx = pancake.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(tokens_amount,0 , path, reciever[0],expire ).buildTransaction(
        {
            'chainId':56,
            'gas': 300000,
            'gasPrice': web3.toWei(gas,'gwei'),
            'nonce':nonce,
        }
    )
    print(f"\n ++++ SELL Transaction Build Successfully ++++ \n")
    

    sign_txn = web3.eth.account.signTransaction(token_tx, private_key=reciever[1])

    hash = sign_txn.hash.hex()

    print(f"Transaction sells {tokens} tokens of {t_name}...\n")

  
    #web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    launch_message = f"Transaction has been launched to pancake router \n--> Tx Hash: {hash}\n"

    logs_message = f"Sell with {packet[1]} for {tokens} {t_name} --> Tx Hash: {hash}"

    ammo = [sign_txn, launch_message, token_tx, hash, logs_message]

    if packet[3] == "manual":
        stop = timeit.default_timer()
        print('\nRunTime: ', stop - start)  
        launch(ammo, "manual")
        choose_function()
    elif packet[3] == "auto":
        launch(ammo, "auto")
        choose_function()
    elif packet[3] == "check":
        launch(ammo, "check")
        choose_function()

def snipe(packet):
    global contract
    global main_address
    global pancake


    change_packet = ["", packet[3]]
    changeContract(change_packet)

    buy_packet = ["", packet[1], packet[2], "check"]
    approve_packet = ["", packet[1]]
    sell_packet = ["", packet[1], 1, "auto"]
    
    
    #url = 'https://bscscan.com/token/' + main_address + '#readContract'
    #webbrowser.open_new(url)
    '''
    if input("LAUNCH?") == "":
        buy_tokens(buy_packet)
        sell_tokens(sell_packet)
    else:
        print("ABORT")
    '''
    buy_tokens(buy_packet)
    approve_trading(approve_packet)
    sell_tokens(sell_packet)
    

## non-trading functions ##

def approve_trading(packet):
    global contract
    global erudite

    raw_info = wallets.wallet_info_all(packet[1])
    #address = raw_info[0]

    address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
    amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

    nonce = web3.eth.getTransactionCount(raw_info[0])

    token_tx = contract.functions.approve(address, amount).buildTransaction(
        {
            'chainId':56,
            'gas': 300000,
            'gasPrice': web3.toWei(gas,'gwei'),
            'nonce':nonce,
        }
    )
    print(f"\n ++++ APPROVE Transaction Build Successfully ++++ \n")
    

    sign_txn = web3.eth.account.signTransaction(token_tx, private_key=raw_info[1])

    hash = sign_txn.hash.hex()

    name = erudite["name"]

    print(f"Transaction approves {name} to trade\n")

  
    #web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    launch_message = f"Transaction has been launched to pancake router \n--> Tx Hash: {hash}\n"

    logs_message = f"Approve with {packet[1]} {name} to trade --> Tx Hash: {hash}"

    ammo = [sign_txn, launch_message, token_tx, hash, logs_message]

    launch(ammo, "auto")
    




    

# c
def currentContract(packet):
    global contract
    global erudite
    name = erudite["name"]
    print(f"\nCurrent Contract: {name}\nAddress: {main_address}")
    choose_function()

# ntoken
def changeContract(packet):
    
    global main_address
    global contract
    global erudite
    global verified
    
    print("\nCurrent Contract: ", main_address)
    print("Changing to: ", packet[1])
   
    new = packet[1]
    if new == main_address:
        print("Already using this contract")
    else:

        main_address = new
        contract = contract_connection(main_address)
        name = contract.functions.name().call()
        
        update("")
        print(f"\nSuccesful contract object creation with {name}")
        
    if packet[0] == "":
        return
    choose_function()

# winfo  
def wallet_info(packet):
    start = timeit.default_timer()

    global contract
    global erudite
    global quick_erudite

    quick_update(packet[1])

    symbol = erudite["symbol"]
    supply = erudite["supply"]


    balanceOf = quick_erudite["tokens"]
    bnb = quick_erudite["bnb"]

    percentage_owned = (balanceOf / supply) * 100
    

    print(f"\nBNB: {bnb} \n{symbol}: {balanceOf} \nPercentage: {percentage_owned}%")
    stop = timeit.default_timer()
    print('\nRunTime: ', stop - start)  
    choose_function()
 
# cinfo
def contract_info_erudite(packet):
    start = timeit.default_timer()
    
    global erudite
    global gas

    
    info = f"""
    Name: {erudite["name"]}
    Symbol: {erudite["symbol"]}
    Supply: {erudite["supply_human"]}
    Owner: {erudite["owner"]}
    Max txn amount: {erudite["max_%"]}%
    Gas selected: {gas}"""
    print(info)
    stop = timeit.default_timer()
    print('\nRunTime: ', stop - start)  
    
    choose_function()

### helpers ###

# methods
def methods(packet):
    global contract
    global erudite
    all_methods = contract.all_functions()
    name = erudite["name"]

    print(f"\nAll functions for {name} \n\n{all_methods}")
    choose_function()
#now
def now():
    return datetime.today().strftime('%Y-%m-%d-%H:%M:%S')




def gas_change(packet):
    global gas
    if packet[1] != "?":
        print(f"\nPrevious gas: {gas}")
        gas = str(packet[1])
        print(f"\nNew gas: {gas}")
    else:
        print(f"\nCurrent gas: {gas}")

def help(packet):
    if packet[1] == "all":
        print(f"""
        Functions:                Describtions:

        c:                   returns current connected contract
        ntoken:              (address) function to change the current contract aka add a new token and replace old one
        cinfo:               information on token
        methods:             returns all methods of token
        winfo:               (wallet_address) information of the wallet
        t:                   (from, to, amount(int or "max"), type("manual" or "auto")) transfer tokens between wallets
        buy:                 (buyer, amount, type) buys amount of tokens at the price of the block it enters
        sell:                (sell, amount or "max", type) sells amount of tokens -currently undere development-
        snipe:                   (buyer, amount, contract_address) snipe fair launches by connecting to to contract and sending a buy at market price 
        """)
        choose_function()

def choose_function():

    raw_input = list(map(str, input("\n--> ").strip().split()))[:5]

    if raw_input == "help":
        print("""
    --- KCB INSTRUCTIONS ---

    + Enter 0 to view current wallet
    + Enter 1 to change current wallet
    + Enter 2 to see contract info
    + Enter 3 to transfer tokens\n""")
        choose_function()
    else:
        packet = raw_input
        run_function(raw_input[0], packet)

def run_function(name, packet):
    
    try:
        KCB_functions[name](packet)
    finally:
        print(f"Error found while runnig \"{name}\" check spelling and parameters")
        choose_function()
        
        
     
    
    #KCB_functions[name](packet)
    #choose_function()

KCB_functions = {
    "help": help,
    "c": currentContract,
    "cinfo": contract_info_erudite,
    "winfo": wallet_info,
    "ntoken": changeContract,
    "update": update,
    "methods": methods,
    "t": transfer_tokens,
    "buy": buy_tokens,
    "sell": sell_tokens,
    "snipe": snipe,
    "gas": gas_change,
    "a": approve_trading

}

connection()
