import requests


class IpifyDriver(object):
    @property
    def ip(self):
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data['ip']


class Drivers(object):
    def ipify(self):
        return IpifyDriver()
