# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages

def read(fname):
    full_path = os.path.join(os.path.abspath(__file__), fname)
    if os.path.exists(full_path):
        return unicode(codecs.open(full_path).read())

setup(
    name="django-datatables",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    include_package_data=True,
    zip_safe=False,
    author='Dave Fogelson',
    author_email='github@landfillinc.com',
    description='jQuery datatables support for Django',
    keywords='django jquery datatables',
    url='https://github.com/LurkingFrog/django-dataTables',
    long_description=read('README.rst'),
)

# End of file.
