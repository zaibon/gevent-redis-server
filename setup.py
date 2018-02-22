from setuptools import setup

from gedis import __version__

setup(
    name="gedis",
    version=__version__,
    author="Christophe de Carvalho",
    author_email="christophe@gig.tech",
    description=("A simple gevent TCP server that speaks the Redis Protocol."),
    url="https://github.com/zaibon/gevent-redis-server",
    license="MIT",
    packages=['gedis'],
    long_description=open('README.md').read(),
    install_requires=['redis>=2.4.1']
)
