import random
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


class HttpbinDriver(object):
    @property
    def ip(self):
        response = requests.get('http://httpbin.org/ip')
        data = response.json()
        return data['origin']


class Drivers(object):
    choices = ('ipify', 'myexternalip', 'dyndns', 'httpbin')

    @classmethod
    def random(cls):
        return random.choice(cls.choices)

    def ipify(self):
        return IpifyDriver()

    def myexternalip(self):
        return MyexternalipDriver()

    def dyndns(self):
        return DyndnsDriver()

    def httpbin(self):
        return HttpbinDriver()
