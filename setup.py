from setuptools import setup, find_packages

setup(
    name="smpp.pdu3",
    version="0.5",
    author="Roger Hoover",
    author_email="roger.hoover@gmail.com",
    description="Python3 Library for parsing Protocol Data Units (PDUs) in SMPP protocol",
    license='Apache License 2.0',
    packages=find_packages(exclude=["tests"]),
    keywords="smpp pdu",
    url="https://github.com/jookies/smpp.pdu",
    py_modules=["smpp.pdu3"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Networking",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
