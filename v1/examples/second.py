"""
second.py

Пример создания блокчейнов вокруг каждой купюры

См ~/examples/data/blockchain_500.json

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
from core.wallet import transaction_hash

from core import OneBlock

import cryptography


def sok_signature(sok):
    """
    В нормальном решении SOK должен изначально быть подписанным внутри SIM карты
    :param sok: 
    :return: 
    """
    h = cryptography.hash(sok)
    sok_signature_ = cryptography.signature(h, BPK)
    return sok_signature_


wallet_A = Wallet(spk=A_SPK, sok=A_SOK, sok_signature=sok_signature(A_SOK))
wallet_B = Wallet(spk=B_SPK, sok=B_SOK, sok_signature=sok_signature(B_SOK))


def main():

    blockchain = list()

    with open('./examples/data/500.json', 'r') as fr:
        data = fr.read()
        banknote = json.loads(data)


    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    # Первый блок
    # Передача купюры: банк -> Алиса
    # -----------------------------------------------------------------------------------------------------------------
    
    # ------- Сторона:: Банк ------------------ 
    bnid = banknote['bnid']

    # ------- Канал связи --------------------
    # Банк передаёт bnid Алисе по каналу связи
    bnid = bnid
    pass

    # -------- Сторона: Алиса ----------------
    # Алиса создаёт новый блок
    uuid, _, otok, _, init_wallet_signature = wallet_A.new_block_params(bnid=bnid, parent_uuid=None)
    

    # ------- Канал связи --------------------
    # Передача данных от Алисы Банку:
    uuid = uuid
    otok = otok
    init_wallet_signature = init_wallet_signature
    sok = wallet_A.sok
    sok_signature_ = wallet_A.sok_signature

    # ------- Сторона: Банк ------------------
    # Верификация
    h = cryptography.hash(sok)
    assert cryptography.verify_signature(h, sok_signature_, BOK)

    h = transaction_hash(uuid, None, otok, bnid)
    assert cryptography.verify_signature(h, init_wallet_signature, sok)

    # Банк подписывает
    magic, subscribe_transaction_hash, subscribe_transaction_signature = bank_subscribe(bnid=bnid, uuid=uuid, bpk=BPK)

    # ------- Канал связи -----------------
    # Передача данных от банка Алисе
    magic = magic
    subscribe_transaction_hash = subscribe_transaction_hash
    subscribe_transaction_signature = subscribe_transaction_signature
    pass

    # -------- Сторона: Алиса -------------

    block = OneBlock(
        uuid=str(uuid),
        parent_uuid='',
        bnid=bnid,
        otok=otok,
        magic=magic,
        subscribe_transaction_hash=subscribe_transaction_hash,
        subscribe_transaction_signature=subscribe_transaction_signature,
    )

    blockchain.append(
        block
    )


    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    # Второй блок
    # Передача купюры: Алиса -> Боб
    # -----------------------------------------------------------------------------------------------------------------

    # ------------ Канал связи -------------------
    # Алиса передаёт Бобу
    parent_uuid = block.uuid
    bnid = block.bnid
    sok = wallet_A.sok
    sok_signature_ = wallet_A.sok_signature
    init_wallet_signature = init_wallet_signature

    # ----------- Сторона: Боб -------------------
    # Верификация Боб-а
    h = cryptography.hash(sok)
    assert cryptography.verify_signature(h, sok_signature_, BOK)

    h = transaction_hash(uuid, None, otok, bnid)
    assert cryptography.verify_signature(h, init_wallet_signature, sok)

    # Боб создаёт новый блок
    uuid, parent_uuid, otok, _, init_wallet_signature = wallet_B.new_block_params(bnid=bnid, parent_uuid=parent_uuid)

    # ----------- Канал связи --------------------
    # Передача этих данных от Боба Алисе через канал связи
    uuid = uuid
    parent_uuid = parent_uuid
    otok = otok
    sok = wallet_B.sok
    sok_signature_ = wallet_B.sok_signature
    init_wallet_signature = init_wallet_signature
    pass

    # ---------- Сторона: Алиса -------------------
    # Верификация
    h = cryptography.hash(sok)
    assert cryptography.verify_signature(h, sok_signature_, BOK)

    h = transaction_hash(uuid, parent_uuid, otok, bnid)
    assert cryptography.verify_signature(h, init_wallet_signature, sok)

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

    # ----------- Канал связи --------------------
    # Алиса передаёт Бобу
    magic = magic
    subscribe_transaction_hash = subscribe_transaction_hash
    subscribe_transaction_signature = subscribe_transaction_signature
    pass

    # ---------- Сторона: Боб -------------------
    # Боб записывает блок

    block = OneBlock(
        uuid=str(uuid),
        parent_uuid=str(parent_uuid),
        bnid=bnid,
        otok=otok,
        magic=magic,
        subscribe_transaction_hash=subscribe_transaction_hash,
        subscribe_transaction_signature=subscribe_transaction_signature,
    )

    blockchain.append(block)

    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
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
    main()
