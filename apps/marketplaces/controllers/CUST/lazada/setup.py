#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='lazop-sdk-python',
    version='1.1.0',
    author='top',
    author_email='xuteng.xt@alibaba-inc.com',
    packages=find_packages(),
    install_requires=[],
    license='MIT',
)

# Should Get from Database
config = {
  "endpoint_sg": "https://api.lazada.sg/rest",
  "appkey": "108986",
  "appSecret": "GbDUTQw7T2qzRG0hmfsvthSQO213QaM0",
  "access_token": "50000200309bbhqacuxDw125aa93dlknuvmwCB3oYGjQCRSh8cdvhrwTcI8brSJu"
}