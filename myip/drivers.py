import re
from .requests_wrapper import requests_wrapper as requests


class Driver(object):
    def __init__(self, get_ip_func):
        self.name = get_ip_func.__name__
        self.get_ip = get_ip_func


@Driver
def ipify():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    return data['ip']


@Driver
def myexternalip():
    response = requests.get('https://myexternalip.com/json')
    data = response.json()
    return data['ip']


@Driver
def dyndns():
    response = requests.get('http://checkip.dyndns.org/')
    matches = re.search('Current IP Address: ([0-9\.]+)', response.text)
    return matches.group(1)


@Driver
def httpbin():
    response = requests.get('http://httpbin.org/ip')
    data = response.json()
    return data['origin'].partition(',')[0]


@Driver
def ipecho():
    response = requests.get('https://ipecho.io/json')
    data = response.json()
    return data['ip']


@Driver
def icanhazip():
    response = requests.get('http://icanhazip.com/')
    return response.text.strip()


@Driver
def aws():
    response = requests.get('https://checkip.amazonaws.com/')
    return response.text.strip()


@Driver
def identme():
    response = requests.get('https://ident.me')
    return response.text


@Driver
def ifconfigme():
    response = requests.get('https://ifconfig.me/ip')
    return response.text


_DRIVERS = {
    attr.name: attr
    for attr in globals().values()
    if isinstance(attr, Driver)
}


CHOICES = tuple(_DRIVERS.keys())


def get_ip(driver_name):
    return _DRIVERS[driver_name].get_ip()
