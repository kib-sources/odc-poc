"""
second_verify.py

Проверим ~/examples/data/blockchain_500.json

created by pavel in pavel as 1/2/21
Проект odc-poc
"""

import datetime

__author__ = 'pavel'
__maintainer__ = 'pavel'
__credits__ = ['pavel', ]
__copyright__ = "LGPL"
__status__ = 'Development'
__version__ = '20210102'

import json

from core.wallet import transaction_hash, subscribe_transaction_hash

import cryptography

from party import BOK


def main():

    with open('./examples/data/blockchain_500.json', 'r') as fr:
        info = json.load(fr)

    blockchain = info['blockchain']
    banknote = info['banknote']
    bnid = info['banknote']['bnid']

    last_block = None
    for i, block in enumerate(blockchain):
        assert block['bnid'] == bnid

        if last_block is None:
            assert block['parent_uuid'] == "", "В первом блоке parent_uuid должен быть пустым"
            publickey = BOK
        else:
            publickey = last_block['otok']

        _subscribe_transaction_hash = subscribe_transaction_hash(uuid=block['uuid'], magic=block['magic'], bnid=bnid)

        assert _subscribe_transaction_hash == block['subscribe_transaction_hash']

        assert cryptography.verify_signature(_subscribe_transaction_hash, block['subscribe_transaction_signature'], publickey=publickey)

        last_block = block
        print(f"Блок №{1+i} корректен!")
        continue
    print("Корректны все блоки!")


if __name__ == "__main__":
    main()
