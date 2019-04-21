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


class Drivers(object):
    choices = ('ipify', 'myexternalip')
    default = 'ipify'

    def ipify(self):
        return IpifyDriver()

    def myexternalip(self):
        return MyexternalipDriver()
