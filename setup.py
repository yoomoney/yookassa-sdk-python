# -*- coding: utf-8 -*-
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

long_description = """
# YooKassa API Python Client Library

[![Build Status](https://travis-ci.org/yoomoney/yookassa-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa.svg)](https://pypi.org/project/yookassa/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa.svg)](https://pypi.org/project/yookassa/)
[![License](https://img.shields.io/pypi/l/yookassa.svg)](https://github.com/yoomoney/yookassa-sdk-python)

[Russian](https://github.com/yoomoney/yookassa-sdk-python/blob/master/README.md) | English

This product is used for managing payments under [The YooKassa API](https://yookassa.ru/en/developers/api)
For usage by those who implemented YooKassa using the API method.

## Requirements
1. Python 2.7 or Python 3.x
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
"""

with open('src/yookassa/__init__.py') as fp:
    version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

setup(
    name="yookassa",
    author="YooMoney",
    author_email="cms@yoomoney.ru",
    version=version,
    keywords="yoomoney, yookassa, payout, sdk, python",
    description="YooKassa API SDK Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoomoney/yookassa-sdk-python",
    package_dir={"": "src"},
    packages=find_packages('src'),
    install_requires=["requests", "urllib3", "distro", "deprecated"],
    zip_safe=False,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)
