from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'a basic hello package'
LONG_DESCRIPTION = 'a basic hello package long description'

# Setting up
setup(
    name="hellopackage",
    version=VERSION,
    author="amirul",
    author_email="amirul@gmail.com",
    description=DESCRIPTION,
    package_dir={"": "lib"},
    packages=find_packages(),
    install_requires=['pytest'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
