"""
party.py

Стороны взаимодействия

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


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Bank


# Bank Open Key
BOK = """-----BEGIN RSA PUBLIC KEY-----
MEgCQQCZScdB8AFwcrZDOLVsBT7m+KyuARWixZCstV99oOMYD318o0rhAqSYk/3Q
nxV31GMYcJv7qABEqnowEkTGDh1TAgMBAAE=
-----END RSA PUBLIC KEY-----"""

# Bank Private Key
BPK = """-----BEGIN RSA PRIVATE KEY-----
MIIBPQIBAAJBAJlJx0HwAXBytkM4tWwFPub4rK4BFaLFkKy1X32g4xgPfXyjSuEC
pJiT/dCfFXfUYxhwm/uoAESqejASRMYOHVMCAwEAAQJBAJTydLSkgrGCNYpSEy9Y
VYvXfOtDUIOul2rKfnQzHWRQWX8MntoQTdw30v2gQuDI8gEpBqP4llYOM8ws4BTb
sykCIwC4TePUAVtG0TME+7GE4Ont6iOkAq3WpqV7M9M062Vd/JTtAh8A1OsgEVsk
g7bwB1lLa5TT8gR1tOV0oGB31KI9G3M/AiMAjK/QaOY8MdvBcV1cDg3OJDGl0S3G
W2NMULan0+6Yq10CpQIeLhj952QRQscfrqehkZg2TwayKUkod/SK3SmHC2NnAiI+
g4WPPFxHv/30FacTi1BTf2HD32FQ3KtKdu+hi6v7JeLq
-----END RSA PRIVATE KEY-----"""

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# A -- Alice (Алиса)

# Sim Open Key
A_SOK = """-----BEGIN RSA PUBLIC KEY-----
MEgCQQCguMma2VJJASzjDAC7p+5jYTCHqNyA2nHwKepvujIyeyi9QTtJixxfz+a7
PkE2asXyR0YtKM9zuwOQnNMFJv3dAgMBAAE=
-----END RSA PUBLIC KEY-----"""

# Sim Private Key
A_SPK = """-----BEGIN RSA PRIVATE KEY-----
MIIBPgIBAAJBAKC4yZrZUkkBLOMMALun7mNhMIeo3IDacfAp6m+6MjJ7KL1BO0mL
HF/P5rs+QTZqxfJHRi0oz3O7A5Cc0wUm/d0CAwEAAQJBAI8bOleovb3HUCJyI4zz
wC248i84ye3pk54WlGobTatgkUdhOdVe/WYBEQ22gMDkPHSFYLy9CkD1Y84T5vxz
roECIwDXG3U2CNny9HEe8U/Fgeluy2Ktzlo3Fj2oYZpjyK+mD5etAh8Av0aTJu/h
KQhg4JzaBHVvZ4jrXoNg6/pMyzOX1ITxAiJn1U4/9gfW2h3ctNkv2qTmoXCRu2Ea
5DaBGBQhhJcdDrvFAh8AhzufiFTq7TbWP5fF8IcSx7GfL0hVuyFRMA1/GCsRAiMA
pI5hIQ0AhV/pnnGjsfqGjEqHdBwAv1OLLVwzOmNomKK7zg==
-----END RSA PRIVATE KEY-----"""

# Wallet ID
A_WID = "W:2359780346"

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# B -- Bob (Боб)


B_SOK = """-----BEGIN RSA PUBLIC KEY-----
MEgCQQC5ohEmk4zwb6YdoBrWjkCr/jZLc729AYc7QC8sabaSLiujiRcd6VwL7drx
QJymxN/gHrvHYDU1xxtiuYCk7nF7AgMBAAE=
-----END RSA PUBLIC KEY-----"""

B_SPK = """-----BEGIN RSA PRIVATE KEY-----
MIIBPQIBAAJBALmiESaTjPBvph2gGtaOQKv+Nktzvb0BhztALyxptpIuK6OJFx3p
XAvt2vFAnKbE3+Aeu8dgNTXHG2K5gKTucXsCAwEAAQJAeP+Yqkp3DanY32qi08N5
iCJ1hYz12iMK4KYfmZV15WrMpZFk2/MVJQ1MShGgUqYQn+hx5HRfN6eV/WWoq9ja
8QIjAONqGRRqCO7zVn932/BSPOQGi77OWasaCROCdvc537Trmy0CHwDQ93+pCB/w
2iz9mvrVas6YWIpiUQZ7EidsLPfRCEcCIwDjF3vb6tbo5o4l0+cJYNX1TqQV8bGR
LvqJROrPjjdaTzwxAh5HHsUrIWHFlmvTkIioVCamQRQwLAV5o48ZSSC62wcCIwDa
T92B+tNQFleSvrNVUWUffShTtm18JaF0knNIhhlB0VxC
-----END RSA PRIVATE KEY-----"""

B_WID = "W:6592360235"
