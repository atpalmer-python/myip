from setuptools import setup, find_packages


setup(
    name='myip',
    version='2020.9.13',
    description='Queries internet resources for your current external IP address.',
    url='https://github.com/atpalmer-python/myip',
    author='Andy Palmer',
    author_email='atp@sdf.org',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['myip=myip.main:main'],
    },
    install_requires=[
        'requests',
        'argparse',
    ],
)
