"""
core.wallet


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

import cryptography

import datetime

from typing import Optional

from uuid import UUID, uuid4

import random

from core import datetime2epoch


def transaction_hash(uuid: UUID, parent_uuid: Optional[UUID], otok):
    if parent_uuid:
        _hash = cryptography.hash(str(uuid), str(parent_uuid), otok)
    else:
        _hash = cryptography.hash(str(uuid), otok)
    return _hash


def subscribe_transaction_hash(uuid: UUID, magic: str):
    return cryptography.hash(str(uuid), magic)


def random_magic():

    magic = list()
    for i in range(16):
        magic += str(random.randint(0, 9))
    magic = ''.join(magic)
    return magic

class Wallet:
    # В рамках POC мы:
    #    1. Не разделяем на SDK, SIM
    #    2. Не используем фильтр блума, а храним все использованные блоки в приватном self._bag

    def __init__(self, spk: str, sok: str):
        self._spk = spk
        self._sok = sok
        self._bag = dict()
        # self._otpk_set = dict()

    @property
    def sok(self):
        return self._sok

    def new_block_params(self, parent_uuid: Optional[UUID] = None):

        otok, otpk = cryptography.init_pear()

        uuid = uuid4()

        _transaction_hash = transaction_hash(uuid, parent_uuid, otok)
        _init_wallet_signature = cryptography.signature(_transaction_hash, self._spk)

        self._bag[uuid] = otpk

        return uuid, parent_uuid, otok, _transaction_hash, _init_wallet_signature

    def subscribe(self, uuid, parent_uuid):
        if parent_uuid not in self._bag:
            raise Exception(f"Уже передан блок с uuid={parent_uuid} или данного блока никогда не было в кошельке")

        otpk = self._bag[parent_uuid]

        magic = random_magic()

        _subscribe_transaction_hash = subscribe_transaction_hash(uuid, magic)
        _subscribe_transaction_signature = cryptography.signature(_subscribe_transaction_hash, otpk)

        # Удаляем ключ, чтобы более ни разу нельзя было подписывать
        #   в нормальном решении необходимо хранение на доверенном носителе, например на SIM
        del self._bag[parent_uuid]

        return magic, _subscribe_transaction_hash, _subscribe_transaction_signature


