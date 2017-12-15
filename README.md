
# Ethereum Blockchain Starter

This repo contains some utilities and notes on how to get a
private ethereum blockchain running on a Mac.

Some of these instructions might work for Windows but I have not
tested it out on windows.

## Resources

[Souptacular](https://souptacular.gitbooks.io/ethereum-tutorials-and-tips-by-hudson/content/private-chain.html)

[Medium Blog](https://medium.com/@WWWillems/how-to-set-up-a-private-ethereum-testnet-blockchain-using-geth-and-homebrew-1106a27e8e1e)


## Install Geth:

### MacOS:

- Homebrew

brew update

brew upgrade

brew tap ethereum/ethereum

brew install ethereum

- Download package

[go-ethereum downloads](https://ethereum.github.io/go-ethereum/downloads/)

If you use the download package, unzip to the users Application directory

~/Applications

and I recommend changing the folder name to something like:

```geth-1.7.3```

and then setup a symlink like:

```ln -s geth geth-1.7.3```

In your .profile add:
GETH_HOME=~/Applications/geth
PATH=$GETH_HOME:$PATH; export PATH


--------

## Download Mist

[Mist Down Releases](https://github.com/ethereum/mist/releases)


## Clone this repo

Clone this repo:  [Ethereum Blockchain Starter](https://github.com)

## Create a data directory for the ethereum data

When starting Ethereum as a private network, we need to specify
a data directory.  This should be outside the git repo

## Generate the scripts to run Ethereum on local private network

Update the python script:

```generate_geth_scripts.py```

and set the following:

```
mistpath = ""
datadir = ""
networkid = ""
genesisfile = ""
```


and then execute:
```python generate_geth_scripts.py```

This will generate a number of scripts to the 'generated' directory.

## Copy CustomGenesis.json file to the generated directory

The init genesis script assumes the genesis file is local.  If you
use the one from the repo, copy that one to this generated directory
or provide another genesis file in the generated directory.


## Running Ethereum

1) Open 3 terminal windows
2) change directory to the 'generated' diretory
3) terminal 1 - run: init-genesis-block.sh
4) terminal 1 - run: start-geth-for-web.sh
5) terminal 2 - run: get-attache.sh
6) terminal 3 - run: run-mist.sh

When Mist starts up is should say it is connecting to the PrivateNet.
If it does not, stop it, and check your scripts.

## Working with Mist

- You should create some accounts.  I create 3 to match what the
python client application is expecting

- Use the ```OpenAuction.sol``` to create a Smart Contract in Mist

- Update PythonClient->OpenAuctionCLI.py to update the account hashs,
the contract hashes and the contract ABI.

## Run OpenAuctionCLI.py

```
cd to/project/root
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd PythonClient
python OpenAuctionCLI.py
```
