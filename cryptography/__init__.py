"""
cryptography

Модуль по криптографии

created by pavel in pavel as 1/2/21
Проект odc-poc
"""

import datetime
import rsa

__author__ = 'pavel'
__maintainer__ = 'pavel'
__credits__ = ['pavel', ]
__copyright__ = "LGPL"
__status__ = 'Development'
__version__ = '20210102'

import random
from hashlib import sha256

random.seed(datetime.datetime.now())


def init_pear():
    """
    Инициализирует пары ключей:
    * закрытый ключ шифрования
    * открытый ключ расшифрования
    :return:
    """

    pubkey, privkey = rsa.newkeys(512)

    pubkey = pubkey._save_pkcs1_pem().decode()
    privkey = privkey._save_pkcs1_pem().decode()

    return pubkey, privkey


def hash(*values):

    salt = 'eRgjPi235ps1'
    v = salt
    for value in values:
        value = str(value)
        v += '|' + value

    hex_hash = sha256(v.encode('utf-8')).hexdigest()
    return hex_hash


def signature(hex_hash: str, privkey: str) -> str:
    # rsa.PublicKey.load_pkcs1(pubkey)
    assert len(hex_hash) == 64

    _privkey = rsa.PrivateKey.load_pkcs1(privkey.encode())

    message = bytearray.fromhex(hex_hash)

    hex_signature = rsa.encrypt(message, _privkey).hex()
    return hex_signature


def check_signature(hex_hash: str, hex_signature: str, publickey: str) -> bool:
    assert len(hex_hash) == 64
    _publickey = rsa.PublicKey.load_pkcs1(publickey.encode())

    _signature = bytearray.fromhex(hex_signature)

    _check_hex_hash = rsa.decrypt(_signature, _publickey).hex()

    if _check_hex_hash == hex_hash:
        return True
    return False

    return message


if __name__ == "__main__":
    pubkey, privkey = init_pear()

    hex_hash = hash('Привет', 'Мир')
    print(f'message:{hex_hash}')

    _signature = signature(hex_hash, privkey)
    print(f'signature:{_signature}')
    if check_signature(hex_hash, _signature, pubkey):
        print("Correct")
    else:
        print("ERROR!")

