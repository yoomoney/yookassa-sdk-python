# -*- coding: utf-8 -*-
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.en.md") as readme_file:
    long_description = readme_file.read()

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
