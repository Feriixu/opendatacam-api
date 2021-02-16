import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
#README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="opendatacam-api",
    version="1.0",
    description="API Wrapper for Opendatacam",
    url="https://github.com/Feriixu/opendatacam-api",
    author="feriixu",
    author_email="",
    license="GNU GPL v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU GPL v3.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["requests", "sseclient"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)