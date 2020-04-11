# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in payment_recon_addons/__init__.py
from payment_recon_addons import __version__ as version

setup(
	name='payment_recon_addons',
	version=version,
	description='Enhancements to ERPNexts Payment Reconciliation Feature',
	author='Bantoo & Jenny Intenet',
	author_email='dev@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
