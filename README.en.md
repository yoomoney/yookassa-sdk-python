# YooKassa API Python Client Library

[![Build Status](https://travis-ci.org/yoomoney/yookassa-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa.svg)](https://pypi.org/project/yookassa/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa.svg)](https://pypi.org/project/yookassa/)
[![License](https://img.shields.io/pypi/l/yookassa.svg)](https://github.com/yoomoney/yookassa-sdk-python)

[Russian](https://github.com/yoomoney/yookassa-sdk-python/blob/master/README.md) | English

This product is used for managing payments under [The YooKassa API](https://yookassa.ru/en/developers/api)
For usage by those who implemented YooKassa using the API method.

## Requirements
1. Python >=3.7
2. pip

## Installation
### Under console using pip

1. Install pip.
2. In the console, run the following command:
```bash
pip install --upgrade yookassa
```

### Under console using easy_install
1. Install easy_install.
2. In the console, run the following command:
```bash
easy_install --upgrade yookassa
```

### Manually

1. In the console, run the following command:
```bash
wget https://pypi.python.org/packages/5a/be/5eafdfb14aa6f32107e9feb6514ca1ad3fe56f8e5ee59d20693b32f7e79f/yookassa-1.0.0.tar.gz#md5=46595279b5578fd82a199bfd4cd51db2
tar zxf yookassa-1.0.0.tar.gz
cd yookassa-1.0.0
python setup.py install
```


## Commencing work

1. Import module
```python
import yookassa
```

2. Configure a Client
```python
from yookassa import Configuration

Configuration.configure('<Account Id>', '<Secret Key>')
```

or

```python
from yookassa import Configuration

Configuration.account_id = '<Account Id>'
Configuration.secret_key = '<Secret Key>'
```

or via oauth

```python
from yookassa import Configuration

Configuration.configure_auth_token('<Oauth Token>')
```

If you agree to participate in the development of the SDK, you can submit data about your framework, cms or module:

```python
from yookassa import Configuration
from yookassa.domain.common.user_agent import Version

Configuration.configure('<Account Id>', '<Secret Key>')
Configuration.configure_user_agent(
    framework=Version('Django', '2.2.3'),
    cms=Version('Wagtail', '2.6.2'),
    module=Version('Y.CMS', '0.0.1')
)
```

3. Call the required API method. [More details in our documentation for the YooKassa API](https://yookassa.ru/en/developers/api)

## Examples of using the API SDK

#### [YooKassa SDK Settings](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/01-configuration.md)
* [Authentication](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/01-configuration.md#Аутентификация)
* [Statistics about the environment used](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/01-configuration.md#Статистические-данные-об-используемом-окружении)
* [Getting information about the store](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/01-configuration.md#Получение-информации-о-магазине)
* [Working with Webhook](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/01-configuration.md#Работа-с-Webhook)
* [Notifications](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/01-configuration.md#Входящие-уведомления)

#### [Working with payments](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md)
* [Request to create a payment](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md#Запрос-на-создание-платежа)
* [Request to create a payment via the builder](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md#Запрос-на-создание-платежа-через-билдер)
* [Request for partial payment confirmation](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md#Запрос-на-частичное-подтверждение-платежа)
* [Request to cancel an incomplete payment](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md#Запрос-на-отмену-незавершенного-платежа)
* [Get payment information](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md#Получить-информацию-о-платеже)
* [Get a list of payments with filtering](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/02-payments.md#Получить-список-платежей-с-фильтрацией)

#### [Working with refunds](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/03-refunds.md)
* [Request to create a refund](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/03-refunds.md#Запрос-на-создание-возврата)
* [Request to create a refund via the builder](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/03-refunds.md#Запрос-на-создание-возврата-через-билдер)
* [Get refund information](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/03-refunds.md#Получить-информацию-о-возврате)
* [Get a list of returns with filtering](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/03-refunds.md#Получить-список-возвратов-с-фильтрацией)

#### [Working with receipts](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/04-receipts.md)
* [Request to create a receipt](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/04-receipts.md#Запрос-на-создание-чека)
* [Request to create a receipt via the builder](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/04-receipts.md#Запрос-на-создание-чека-через-билдер)
* [Get information about the receipt](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/04-receipts.md#Получить-информацию-о-чеке)
* [Get a list of receipts with filtering](https://github.com/yoomoney/yookassa-sdk-python/blob/master/docs/examples/04-receipts.md#Получить-список-чеков-с-фильтрацией)
