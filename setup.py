# -*- coding: utf-8 -*-
from distutils.core import setup

setup (
    name='Opsworks Tools',
    version='0.1',
    author='Adinata',
    author_email='mail.dieend@gmail.com',
    url='http://github.com/dieend/aws-opsworks-tools',
    description='This is tools to make easier managing aws opsworks. I used this in jenkins',
    long_description=open('README.md').read(),
    scripts=['scripts/opsworks'],
    requires=['boto (==2.34.0)', 'clize (==2.4)']
)
