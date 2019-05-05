from setuptools import setup, find_packages


setup(
    name='myip',
    version='2019.4.28',
    description='Queries internet resources for your current external IP address.',
    author='Andy Palmer',
    author_email='andrew.t.palmer@parker.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['myip=myip.main:main'],
    },
    install_requires=[
        'requests',
        'argparse',
    ],
)
