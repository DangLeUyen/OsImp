from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='OsImputation',
    version='0.1.0',
    description='My awesome OsImp package',
    url='https://github.com/DangLeUyen/OsImp.git',
    package_dir={"": "src"},
    install_requires=requirements,
    keywords='python package',
    python_requires='>=3.6',
)