"""



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

from dataclasses import dataclass

from time import sleep

# https://www.iban.com/currency-codes
RUSSIAN_RUBLE = 643


@dataclass
class Banknote:

    bin: int

    amount: int

    currency_code: int

    # BankNote id
    bnid: str

    # hash
    hash: str

    # signature
    signature: str

    @classmethod
    def make_bnid(cls, bin):

        _now = datetime.datetime.now()
        no = _now.strftime('%Y%m%d%H%M%S%f')
        sleep(0.001)  # необходимо поспать, чтобы гарантировать уникальный номер
        bnid = f'{bin}-{no}'
        return bnid

    @classmethod
    def make_hash(cls, *, bnid):
        return cryptography.hash(bnid)

    def verify(self, bok):
        _hash = Banknote.make_hash(bnid=self.bnid)
        if _hash != self.hash:
            return False
        if not cryptography.verify_signature(self.hash, self.signature, bok):
            return False
        return True

    @classmethod
    def init(cls, *, bpk, bin: int, amount: int, currency_code: int = RUSSIAN_RUBLE):
        bnid = Banknote.make_bnid(bin)
        _hash = Banknote.make_hash(bnid=bnid)
        banknote = Banknote(
            bin=bin,
            bnid=bnid,
            amount=amount,
            currency_code=currency_code,
            hash=_hash,
            signature=cryptography.signature(_hash, bpk),
        )
        # assert banknote.verify(bok=bok)
        return banknote



if __name__ == "__main__":

    bin = 1234


