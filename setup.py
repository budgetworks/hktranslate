from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hktranslate/__init__.py
from hktranslate import __version__ as version

setup(
	name="hktranslate",
	version=version,
	description="Translate and Custom for HK Translate",
	author="Victor Tong",
	author_email="em3888@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
