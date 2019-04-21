import re
import requests


class IpifyDriver(object):
    @property
    def ip(self):
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data['ip']


class MyexternalipDriver(object):
    @property
    def ip(self):
        response = requests.get('https://myexternalip.com/json')
        data = response.json()
        return data['ip']


class DyndnsDriver(object):
    @property
    def ip(self):
        response = requests.get('http://checkip.dyndns.org/')
        matches = re.search('Current IP Address: ([0-9\.]+)', response.text)
        return matches.group(1)


class Drivers(object):
    choices = ('ipify', 'myexternalip', 'dyndns')
    default = 'ipify'

    def ipify(self):
        return IpifyDriver()

    def myexternalip(self):
        return MyexternalipDriver()

    def dyndns(self):
        return DyndnsDriver()
