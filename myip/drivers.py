import random
import re
import requests


class _Drivers(object):
    def ipify(self):
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data['ip']

    def myexternalip(self):
        response = requests.get('https://myexternalip.com/json')
        data = response.json()
        return data['ip']

    def dyndns(self):
        response = requests.get('http://checkip.dyndns.org/')
        matches = re.search('Current IP Address: ([0-9\.]+)', response.text)
        return matches.group(1)

    def httpbin(self):
        response = requests.get('http://httpbin.org/ip')
        data = response.json()
        return data['origin']

    def ipecho(self):
        response = requests.get('https://ipecho.net/json')
        data = response.json()
        return data['ip']

    def icanhazip(self):
        response = requests.get('http://icanhazip.com/')
        return response.text.strip()

    def aws(self):
        response = requests.get('https://checkip.amazonaws.com/')
        return response.text.strip()


class Drivers(object):
    drivers = _Drivers()
    choices = tuple(attr for attr in dir(drivers) if not attr.startswith('_'))

    @classmethod
    def random(cls):
        return random.choice(cls.choices)

    def __getattr__(self, attr):
        return getattr(self.drivers, attr)
