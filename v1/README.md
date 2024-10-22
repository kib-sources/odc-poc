# Open Digital Cash -- Proof Of Consept

Проверка концепта ODC.

Написана для быстроты проверки на Python. 

Оригинальная криптографическая библиотека должна быть написана на C\C++\Rust\... для скорости

https://github.com/kib-sources/odc-poc

## Обозначения

| Аббревиатура | расшифровка | назначение |
| --- | --- | ---| 
| bin | БИН, банковский идентификатор | Идентификатор банка-эмитента цифровой купюры |
| bnid | banknote ID | уникальный идентификатор банкноты в рамках **bid** | 
| spk | SIM private key | Приватный ключ, зашитый в SIM карту |
| sok | SIM open key | Публичный ключ SIM карты |
| otok | One Time open key | Одноразовый открытый ключ, для верификации блокчейна |
| otpk | One Time Private Key | Одноразовый ключ для подписи. Хранится в SIM карте (в рамках POC, в реале -- на телефоне, а в SIM использоватся будет фильтр Блума и регистрация otpk ключей) |

## Процесс работы

### Общий принцип

...


## 