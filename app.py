import json
from web3 import Web3

# A way to connect to the BlockChain
url = "https://mainnet.infura.io/v3/f9b7422fa52e43bfa3ea3f3e836b1df2"
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

f = open('abi.json')
abi = json.load(f)
address = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"

contract = web3.eth.contract(address=address, abi=abi)

totalSupply = contract.functions.totalSupply().call()
print(totalSupply)
print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())

balance = contract.functions.balanceOf(web3.toChecksumAddress('0xbdbd1d2602d77b98368d3f9c8c7a689dd939d5b2')).call()
print(web3.fromWei(balance, 'ether'))