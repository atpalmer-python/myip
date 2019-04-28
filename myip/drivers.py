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


class IpechoDriver(object):
    @property
    def ip(self):
        response = requests.get('https://ipecho.net/json')
        data = response.json()
        return data['ip']


class IcanhazipDriver(object):
    @property
    def ip(self):
        response = requests.get('http://icanhazip.com/')
        return response.text.strip()


class AmazonAwsDriver(object):
    @property
    def ip(self):
        response = requests.get('https://checkip.amazonaws.com/')
        return response.text.strip()


class _Drivers(object):
    def ipify(self):
        return IpifyDriver()

    def myexternalip(self):
        return MyexternalipDriver()

    def dyndns(self):
        return DyndnsDriver()

    def httpbin(self):
        return HttpbinDriver()

    def ipecho(self):
        return IpechoDriver()

    def icanhazip(self):
        return IcanhazipDriver()

    def aws(self):
        return AmazonAwsDriver()


class Drivers(object):
    drivers = _Drivers()
    choices = tuple(attr for attr in dir(drivers) if not attr.startswith('_'))

    @classmethod
    def random(cls):
        return random.choice(cls.choices)

    def __getattr__(self, attr):
        return getattr(self.drivers, attr)
