from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="python-periods",
    version="0.1.0",
    description="",
    author="Johanna Eriksson",
    author_email="johanna.eriksson@booli.se",
    maintainer="Olof Sjöbergh",
    maintainer_email="olofsj@gmail.com",
    url="https://github.com/iloob/python-periods",
    license="MIT",
    packages=[
        "periods",
    ],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
