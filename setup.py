import os
from setuptools import setup, find_packages

setup(
        name='ghelper'
        version='0.1dev'
        packages=find_packages('src')
        package_dir={'','src'}
        description="Helper Tools for Google API"
        long_description=read('README.md')
        url='git@github.com:Juniped/ghelper.git'
        install_requires=[

        ]
}
