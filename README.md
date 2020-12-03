# YooKassa API Python Client Library

[![Build Status](https://travis-ci.org/yoomoney/yookassa-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa.svg)](https://pypi.org/project/yookassa/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa.svg)](https://pypi.org/project/yookassa/)
[![License](https://img.shields.io/pypi/l/yookassa.svg)](https://github.com/yoomoney/yookassa-sdk-python)

Russian | [English](https://github.com/yoomoney/yookassa-sdk-python/blob/master/README.en.md)

Клиент для работы с платежами по [API ЮKassa](https://yookassa.ru/developers/api)
Подходит тем, у кого способ подключения к ЮKassa называется API.

## Требования

1. Python 2.7 or Python 3.x
2. pip

## Установка
### C помощью pip

1. Установите pip.
2. В консоли выполните команду
```bash
pip install --upgrade yookassa
```

### С помощью easy_install
1. Установите easy_install.
2. В консоли выполните команду
```bash
easy_install --upgrade yookassa
```

### Вручную

1. В консоли выполните команды:
```bash
wget https://pypi.python.org/packages/5a/be/5eafdfb14aa6f32107e9feb6514ca1ad3fe56f8e5ee59d20693b32f7e79f/yookassa-1.0.0.tar.gz#md5=46595279b5578fd82a199bfd4cd51db2
tar zxf yookassa-1.0.0.tar.gz
cd yookassa-1.0.0
python setup.py install
```

## Начало работы

1. Импортируйте модуль
```python
import yookassa
```
2. Установите данные для конфигурации
```python
from yookassa import Configuration

Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
```

или

```python
from yookassa import Configuration

Configuration.account_id = '<Идентификатор магазина>'
Configuration.secret_key = '<Секретный ключ>'
```

или через oauth

```python
from yookassa import Configuration

Configuration.configure_auth_token('<Oauth Token>')
```

Если вы согласны участвовать в развитии SDK, вы можете передать данные о вашем фреймворке, cms или модуле:
```python
from yookassa import Configuration
from yookassa.domain.common.user_agent import Version

Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
Configuration.configure_user_agent(
    framework=Version('Django', '2.2.3'),
    cms=Version('Wagtail', '2.6.2'),
    module=Version('Y.CMS', '0.0.1')
)
```

3. Вызовите нужный метод API. [Подробнее в документации к API ЮKassa](https://yookassa.ru/developers/api)


