"""
examples.first


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


from dataclasses import asdict

from party import BOK, BPK, BIN

from core import Banknote

import json


def main():
    print(datetime.datetime.now())

    banknote = Banknote.init(bpk=BPK, bin=BIN, amount=500)
    assert banknote.verify(bok=BOK)

    with open('./examples/data/500.json', 'w') as fw:
        info = asdict(banknote)
        json.dump(info, fw, indent=4)

    banknote = Banknote.init(bpk=BPK, bin=BIN, amount=100)
    assert banknote.verify(bok=BOK)

    with open('./examples/data/100.json', 'w') as fw:
        info = asdict(banknote)
        json.dump(info, fw, indent=4)


if __name__ == "__main__":
    main()
