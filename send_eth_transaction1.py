import csv
import requests
import web3

#Create a web3 object with NOWNodes as HTTTPProvider
w3 = web3.Web3(web3.HTTPProvider("https://eth.nownodes.io/"))

#Specify your private key from my_address wallet
private_key = ""


#my_address is the address from which you will send ETH to test_address
my_address = ""
test_address = ""

#This is how to get the balance of test_address
print(w3.eth.getBalance(test_address))


#Change the value if you want to send more or less
value = w3.toHex(w3.toWei("0.001", "ether"))


#This is how to create a raw transaction object
#gas is the maximum gas that is allowed to be spent to process the transaction;
#chainId is the id of the Ethereum chain;
#nonce is  the transaction sequence number for the sending account;
#gasPrice is the price you are offering to pay.

rawTransaction = {
	"from": my_address,

	"to": test_address,

	"value": value,

	"gas": 200000,

	"chainId": 1,

	"nonce": w3.eth.getTransactionCount(my_address),

	"gasPrice": w3.eth.gasPrice
}

#This is how to send a raw transaction with your private key
signed_txn = w3.eth.account.sign_transaction(rawTransaction, private_key)

#This is how to send a transaction and print its hash
#You can take a look at your transaction at https://etherscan.io/ by copying and pasting this hash
print(w3.toHex(w3.eth.sendRawTransaction(signed_txn.rawTransaction)))


