from setuptools import setup
from pathlib import Path
import re

requires = ["selenium>=3.141.0", "pywin32>=224"]
packages = ["uwstyle"] + [
    "uwstyle." + str(p) for p in Path(".").iterdir()
    if re.match(r"^([a-z]+)$", p.name)]
description = ""
with open("Readme.md") as f:
    description = f.read()
setup(
    name='uwstyle',
    version='0.0.2',
    description='Modules for handling UWSC styles in Python',
    long_description=description,
    url='https://github.com/TakamiChie/UWStyleMethods',
    author='TakamiChie',
    author_email='chie@onpu-tamago.net',
    license='MIT',
    keywords='dialog utility',
    packages=packages,
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)