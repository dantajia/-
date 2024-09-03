import os

from web3 import Web3

from trace.trace_balance_analyzer import parse_trace
from utils.processor import Processor
from utils.get_fields import get_chain_by_tx

trace_data_dir = r'../trace_data'
processor = Processor(transaction=None, chain=None)

for root, dirs, files in os.walk(trace_data_dir):
    for file in files:
        file_path = os.path.join(root, file)
        tx_hash = file[12:-4]
        balance_changes = parse_trace(file_path)
        # print(balance_changes)
        address_increase = []
        for addr, change in balance_changes.items():
            # print(f"Address: {addr}, Balance Change: {change}")
            if change > 0:
                address_increase.append({'addr': addr, 'change': change})
        chain = get_chain_by_tx(tx_hash)
        # print(f"链：{chain}")
        processor.chain = chain
        processor.transaction = tx_hash
        processor.rpc_node = processor.config['rpc_nodes'].get(chain, None)
        if processor.rpc_node:
            processor.w3 = Web3(Web3.HTTPProvider(processor.rpc_node))
        else:
            print(f'No RPC node for chain {chain}')
        res = processor.get_ex_balance(address_increase)
        print(res)
        output_file = r'sus_wallet.txt'
        with open(output_file, 'a') as f:
            if res is not None:
                for item in res:
                    f.write(item['addr'] + '\n')
        print('------------------------------------------------------------------------------------------------------')
