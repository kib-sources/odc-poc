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


if __name__ == "__main__":
    a, b = init_pear()
    print(a)
    print(b)