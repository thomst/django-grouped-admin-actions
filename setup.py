#!/usr/bin/env python

import os
from pathlib import Path
from setuptools import setup
from setuptools import find_namespace_packages


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as file:
        return file.read()


def version():
    namespace = {}
    path = Path("grouped_admin_actions", "__version__.py")
    exec(path.read_text(), namespace)
    return namespace["__version__"]


version = version()
if 'dev' in version:
    dev_status = 'Development Status :: 3 - Alpha'
elif 'beta' in version:
    dev_status = 'Development Status :: 4 - Beta'
else:
    dev_status = 'Development Status :: 5 - Production/Stable'


setup(
    name="django-grouped-admin-actions",
    version=version,
    description="TODO",
    long_description=read("README.rst"),
    author="Thomas Leichtfuß",
    author_email="thomas.leichtfuss@posteo.de",
    url="https://github.com/thomst/django-grouped-admin-actions",
    license="BSD License",
    platforms=["OS Independent"],
    packages=find_namespace_packages(exclude=["tests.*", "tests"]),
    package_data={"grouped_admin_actions": ["static/**", "templates/**"]},
    include_package_data=True,
    install_requires=[
        "Django>=2.2",
    ],
    classifiers=[
        dev_status,
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    zip_safe=True,
)
