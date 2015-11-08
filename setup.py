# coding: utf-8
from setuptools import setup
from setuptools import find_packages


setup(name='yandex.dictionary',
      version='0.1.0',
      author="yandex.dictionary contributors",
      author_email="wdport@yahoo.com",
      description='Python library for Yandex.Dictionary API.',
      license="DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE",
      keywords="yandex yandex-dictionary dictionary",
      url="https://github.com/kz20/python-yandex-dictionary",
      packages=find_packages(),
      package_dir={'yandex_dictionary': 'yandex_dictionary'},
      provides=['yandex_dictionary'],
      classifiers=[
          'Intended Audience :: Developers',
          'Development Status :: 3 - Alpha',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
      ],
      platforms=['All'],
      install_requires=['requests>=1.2.3'],
      )
