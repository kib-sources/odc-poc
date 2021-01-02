"""
second.py

Пример создания блокчейнов вокруг каждой купюры

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

from dataclasses import asdict

from party import A_SOK, A_SPK, A_WID
from party import B_SOK, B_SPK, B_WID
from party import BOK, BPK

from core.wallet import Wallet
from core.wallet import bank_subscribe

from core import OneBlock

wallet_A = Wallet(spk=A_SPK, sok=A_SOK)
wallet_B = Wallet(spk=B_SPK, sok=B_SOK)


def example1():

    blockchain = list()

    with open('./examples/data/500.json', 'r') as fr:
        data = fr.read()
        banknote = json.loads(data)


    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    # Первый блок
    # Передача купюры: банк -> Алиса
    # -----------------------------------------------------------------------------------------------------------------

    bnid = banknote['bnid']

    # Банк передаёт bnid Алисе по каналу связи
    pass

    # Алиса создаёт новый блок
    uuid, _, otok, transaction_hash, init_wallet_signature = wallet_A.new_block_params(bnid=bnid, parent_uuid=None)

    # Передача данных от Алисы Банку
    pass

    # Банк подписывает
    magic, subscribe_transaction_hash, subscribe_transaction_signature = bank_subscribe(bnid=bnid, uuid=uuid, bpk=BPK)

    # Передача данных от банка Алисе
    pass

    block = OneBlock(
        uuid=str(uuid),
        parent_uuid='',
        bnid=bnid,
        otok=otok,
        transaction_hash=transaction_hash,
        init_wallet_signature=init_wallet_signature,
        magic=magic,
        subscribe_transaction_hash=subscribe_transaction_hash,
        subscribe_transaction_signature=subscribe_transaction_signature,
    )

    blockchain.append(block)

    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    # Второй блок
    # Передача купюры: Алиса -> Боб
    # -----------------------------------------------------------------------------------------------------------------

    parent_uuid = block.uuid
    bnid = block.bnid

    # Алиса передаёт parent_uuid и bnid Бобу
    pass

    # Боб создаёт новый блок
    uuid, parent_uuid, otok, transaction_hash, init_wallet_signature = wallet_B.new_block_params(bnid=bnid, parent_uuid=parent_uuid)

    # Передача этих данных от Боба Алисе через канал связи
    pass

    # Алиса подписывает
    magic, subscribe_transaction_hash, subscribe_transaction_signature = wallet_A.subscribe(uuid, parent_uuid, bnid)

    # Проверим, что мы не можем один и тот же parent_uuid подписать дважды
    try:
        wallet_A.subscribe(None, parent_uuid, None)
    except Exception as e:
        # уф... всё хорошо
        pass
    else:
        raise Exception("Мы можем сделать 'штаны' в блокчейне!")

    block = OneBlock(
        uuid=str(uuid),
        parent_uuid=str(parent_uuid),
        bnid=bnid,
        otok=otok,
        transaction_hash=transaction_hash,
        init_wallet_signature=init_wallet_signature,
        magic=magic,
        subscribe_transaction_hash=subscribe_transaction_hash,
        subscribe_transaction_signature=subscribe_transaction_signature,
    )

    blockchain.append(block)

    # -----------------------------------------------------------------------------------------------------------------

    info = {
        'banknote': banknote,
        'blockchain': list()
    }
    for block in blockchain:
        block = asdict(block)
        info['blockchain'].append(block)

    with open('./examples/data/blockchain_500.json', 'w') as fw:
        json.dump(info, fw, indent=4)


if __name__ == "__main__":
    example1()
