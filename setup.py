from setuptools import setup, find_packages
from pathlib import Path
import re
from uwstyle import VERSION

requires = ["selenium>=3.141.0", "pywin32>=224"]
description = ""
with open(Path(__file__).parent / "Readme.md") as f:
    description = f.read()
setup(
    name='uwstyle',
    version=VERSION,
    description='Modules for handling UWSC styles in Python',
    long_description=description,
    url='https://github.com/TakamiChie/UWStyleMethods',
    author='TakamiChie',
    author_email='chie@onpu-tamago.net',
    license='MIT',
    keywords='dialog utility',
    packages=["uwstyle",
        "uwstyle.dialogs",
        "uwstyle.excel",
        "uwstyle.overridestd",
        "uwstyle.webbrowser"
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)