import os

from setuptools import (
    setup,
    find_packages,
)

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='corylus',
    version='0.1',
    url='https://git.elenet.me/cheng.gush/corylus',
    license='MIT',
    packages=find_packages(here),
    author='gucheng',
    author_email='cheng.gush@ele.me',
    description='Render url to png as your wish',
    install_requires=[
        "Flask==0.11.1",
        "Flask-RESTful==0.3.5",
        "Flask-SQLAlchemy==2.1",
        "huey==1.2.0",
        "PyMySQL==0.7.9",
        "redis==2.10.5",
        "SQLAlchemy==1.0.15",
        "arrow==0.8.0"
    ]
)
