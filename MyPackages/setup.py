from setuptools import setup, find_packages

setup(
    name='mypackage',
    Version="0.1",
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Example Python Package',
    long_description=open('README.MD').read(),
    install_requires=['numpy'],
    url='https://github.com/Amr-Yasser08/MyPackages',
    author='Amr Yasser'

)