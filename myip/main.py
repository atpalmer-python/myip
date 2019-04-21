from .drivers import Drivers


CONFIG = {
    'driver': 'ipify',
}


def get_driver(driver_name):
    drivers = Drivers()
    return getattr(drivers, driver_name)()


def main():
    driver = get_driver(CONFIG['driver'])
    print(driver.ip)
