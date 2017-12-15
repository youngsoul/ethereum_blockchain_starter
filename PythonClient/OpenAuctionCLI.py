from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from web3 import Web3, HTTPProvider, IPCProvider
import json
import time

web3 = None
contract = None
bidder = None
account = None

account_names = ['Bob', 'Joe', 'Sue']
bidders = WordCompleter(account_names, ignore_case=True)

ipc_path="/Users/youngsoul/blockchain/data/geth.ipc"

main_account = "0xB3f8ff0890424179d1AF24c0740AA77B94d28DaB"
account_2 = "0x44190410c788831799d49Ed5a313007D05b7F209"
account_3 = "0x217A6bE8840139a8C50eb00639aa8086B77e1442"

accounts = {
    'Bob': { 'address': main_account, 'pwd': 'test123456' },
    'Joe': { 'address': account_2, 'pwd': 'test123456' },
    'Sue': { 'address': account_3, 'pwd': 'test123456' }
}

contract_version = 'version3'
contract_versions = {
    'version1': {
        'abi': """[ { "constant": false, "inputs": [], "name": "bid", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "auctionEnd", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "beneficiary", "outputs": [ { "name": "", "type": "address", "value": "0x68681ff8dd3489e6282147eb08f431b278f239c0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "withdraw", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "itemName", "outputs": [ { "name": "", "type": "string", "value": "raspberry pi 3" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "highestBidder", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "highestBid", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_biddingTime", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "bidding Time", "template": "elements_input_uint", "value": "" }, { "name": "_beneficiary", "type": "address", "index": 1, "typeShort": "address", "bits": "", "displayName": "beneficiary", "template": "elements_input_address", "value": "" }, { "name": "_itemname", "type": "string", "index": 2, "typeShort": "string", "bits": "", "displayName": "itemname", "template": "elements_input_string", "value": "" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "bidder", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "HighestBidIncreased", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "winner", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "AuctionEnded", "type": "event" } ]""",
        'address': "0xE0b300aDAB83489f024FE6999B143286B070fBB8"
    },
    'version2': {
        'abi': """[ { "constant": false, "inputs": [], "name": "bid", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "auctionEnd", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "beneficiary", "outputs": [ { "name": "", "type": "address", "value": "0x904015f90e2f7c7e1cb2f9e92b9e0c30d5e7139e" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "withdraw", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "itemName", "outputs": [ { "name": "", "type": "string", "value": "Car" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "highestBidder", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "highestBid", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_biddingTime", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;bidding Time", "template": "elements_input_uint", "value": "360000" }, { "name": "_beneficiary", "type": "address", "index": 1, "typeShort": "address", "bits": "", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;beneficiary", "template": "elements_input_address", "value": "0x904015F90E2f7C7e1CB2f9E92b9E0C30D5E7139e" }, { "name": "_itemname", "type": "string", "index": 2, "typeShort": "string", "bits": "", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;itemname", "template": "elements_input_string", "value": "Car" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "bidder", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "HighestBidIncreased", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "winner", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "AuctionEnded", "type": "event" } ]""",
        'address': '0x6D145715D5534484d53FcB6898FaD5f2268cC39d'
    },
    'version3': {
        'abi': """[ { "constant": false, "inputs": [], "name": "bid", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "auctionEnd", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "beneficiary", "outputs": [ { "name": "", "type": "address", "value": "0xb3f8ff0890424179d1af24c0740aa77b94d28dab" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "withdraw", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "itemName", "outputs": [ { "name": "", "type": "string", "value": "Car" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "highestBidder", "outputs": [ { "name": "", "type": "address", "value": "0x44190410c788831799d49ed5a313007d05b7f209" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "highestBid", "outputs": [ { "name": "", "type": "uint256", "value": "5000000000000000000" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_biddingTime", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;bidding Time", "template": "elements_input_uint", "value": "" }, { "name": "_beneficiary", "type": "address", "index": 1, "typeShort": "address", "bits": "", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;beneficiary", "template": "elements_input_address", "value": "" }, { "name": "_itemname", "type": "string", "index": 2, "typeShort": "string", "bits": "", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;itemname", "template": "elements_input_string", "value": "" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "bidder", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "HighestBidIncreased", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "winner", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "AuctionEnded", "type": "event" } ]""",
        'address': '0x8B7F1e006D774EA2a515b55A097D82Cb6E5f3BA2'
    }
}

def get_user_from_address(user_address):
    for k,v in accounts.items():
        if v['address'] == user_address:
            return k

    return 'Unknown'

def get_bidder():
    _bidder = None
    while _bidder is None:
        _bidder = prompt("Select a bidder>", completer=bidders)
        if _bidder not in account_names:
            _bidder = None


    print("You will be bidding as: {}".format(_bidder))
    return _bidder

def get_account_for_bidder(bidder):
    _account = accounts[bidder]
    if _account is None:
        raise ValueError("Could not find account for bidder: {}".format(bidder))
    return _account

def initialize_web3(account):
#    _web3 = Web3(HTTPProvider('http://192.168.1.159:8545'))

    _web3 = Web3(IPCProvider(ipc_path))
    return _web3

def unlock_account(account):
    web3.personal.unlockAccount(account['address'], account['pwd'])

def setup_contract(version_key):
    abi = contract_versions[version_key]['abi'].replace("&thinsp;<span class=\"punctuation\">_</span>&thinsp;", '')

    contract_abi = json.loads(abi)
    contract_address = contract_versions[version_key]['address']  #"0xE0b300aDAB83489f024FE6999B143286B070fBB8"
    _contract = web3.eth.contract(abi=contract_abi, address=contract_address)
    #print(contract)
    return _contract

def print_current_auction_details():
    print("Public Property itemName:  {}".format(contract.call().itemName()))
    print("Beneficiary: {}".format(get_user_from_address(contract.call().beneficiary())))
    print("Highest Bid: {}".format(contract.call().highestBid()))
    print("Highest Bidder: {}".format(get_user_from_address(contract.call().highestBidder())))
    print("Auction End: {}".format(contract.call().auctionEnd()))

def wait_for_transaction_to_complete(trans_hash):
    trans_receipt = web3.eth.getTransactionReceipt(trans_hash)

    while trans_receipt is None:
        print("Mining transaction....")
        time.sleep(2)
        trans_receipt = web3.eth.getTransactionReceipt(trans_hash)

def place_bid(account, bid_amount):
    bid_amount = web3.toWei(bid_amount, 'ether')
#    trans_hash = contract.transact({'from': account['address'], 'value': bid_amount, 'gas': 100000}).bid()
    trans_hash = contract.transact({'from': account['address'], 'value': bid_amount, 'gas': 100000}).bid()
    wait_for_transaction_to_complete(trans_hash)

def get_bid():
    bid = None
    while bid is None:
        bid = prompt("bid amount>")
        if not bid.isdigit():
            bid = None

    return int(bid)

def are_you_done():
    done = False
    d = prompt("Are you done? [y | n]>")
    if d == 'y':
        done = True
    return done


def on_high_bid_increase(eventLog):
    """

    :param eventLog:
                args, event, logIndex, transactionIndex, transactionHash, address, blockHash, blockNumber
    :return: None
    """
    print("High Bid Increase: {}".format(eventLog))

def on_auction_ended(eventLog):
    print("Auction Ended: {}".format(eventLog))


if __name__ == '__main__':

    bidder = get_bidder()
    account = get_account_for_bidder(bidder)
    web3 = initialize_web3(account)
    contract = setup_contract(contract_version)
    f1 = contract.on('HighestBidIncreased')
    f1.watch(on_high_bid_increase)
    #contract.on('AuctionEnded', on_auction_ended)

    print_current_auction_details()

    done = False
    while not done:
        unlock_account(account)
        bid_amount = get_bid()
        place_bid(account, bid_amount)
        print_current_auction_details()
        done = are_you_done()




