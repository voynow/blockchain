from web3 import Web3
import pandas as pd

# dictionary for data collection
data = {
    "number": [],
    "miner": [],
    "size": [],
    "timestamp": [],
    "totalDifficulty": [],
    "baseFeePerGas": [],
    "difficulty": [],
    "gasLimit": [],
    "gasUsed": []}

# connection to infura eth api endpoint
endpoint = 'https://mainnet.infura.io/v3/fcc08fdf54844e46aa4b60989bdc0f14'
w3 = Web3(Web3.HTTPProvider(endpoint))

# get most recent block number
block_number = w3.eth.getBlock(w3.eth.defaultBlock, True).number

# iter over 'n_iter' most recent blocks and collect associated data
n_iter = 1000
for i in range(n_iter):
    block = w3.eth.getBlock(block_number, True)
    print(f'block_id={block_number}')
    block_number = block.number - 1

    for key in data.keys():
        data[key].append(getattr(block, key))

# format data as .csv file
pd.DataFrame(data).to_csv(f'block_data.csv', index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# block attribute output
# for item in dir(block):
#     if item[:1] != "_":
#         try:
#             attr = getattr(block, item)
#             if type(attr) == int or type(attr) == str:
#                 print(f'{item:27s}{attr}')
#             else:
#                 print(f'{item:27s}{type(attr)}')
#         except:
#             print(f'{item:27s} ERROR')