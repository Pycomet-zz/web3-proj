import json
from web3 import Web3, contract

infura_url = "https://mainnet.infura.io/v3/104abeafa90045c490605995b21684c1"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.eth.blockNumber)

# print(web3.isConnected())

# address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"
# abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')

# contract = web3.eth.contract(address=address, abi=abi)

# print(contract)

# totalSupply = contract.functions.totalSupply().call()
# print(totalSupply)

# print(web3.fromWei(totalSupply, 'ether'))

# # Get nme
# print(contract.functions.name().call())



# Sending Transactions
# genache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(genache_url))

# account1 = "0xC6d7EfC87FF29e49B0d8F61a89ACf6cE866a6e0F"
# account2 = "0xC4D5100918CfEaDd17F4D68ad7B454Ed58EEbAdc"
 
# private_key = "3ed821099221a54302f1d1b6b30a7e3dd8b4ff50003c775e49e6717f2b02130b"

# # get the nonce
# nonce = web3.eth.getTransactionCount(account1)

# # build a transaction
# tx = {
#     'nonce': nonce,
#     'to': account2,
#     'value': web3.toWei(1, 'ether'),
#     'gas': 2000000,
#     'gasPrice': web3.toWei('50', 'gwei')
# }

# # sign transaction
# signed_tx = web3.eth.account.signTransaction(tx, private_key)

# # send transaction
# tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# # get transaction hash
# print(web3.toHex(tx_hash))






# genache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(genache_url))

# # Gretter Smart Contract Deployed on Remix.Ether
# abi = json.loads('[{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"newGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# address = web3.toChecksumAddress("0xE555A865f0767f420E774E293f6e0c0548D8d624")

# #easier way to register signed account
# web3.eth.defaultAccount = web3.eth.accounts[0]

# contract = web3.eth.contract(address=address, abi=abi)


# tx_hash = contract.functions.newGreeting("NEW GREND").transact()
# print(web3.toHex(tx_hash))

# web3.eth.waitForTransactionReceipt(tx_hash)


# print(contract.functions.greet().call())



### GETTING BLOCK DATA
