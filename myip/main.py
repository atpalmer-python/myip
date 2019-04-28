from argparse import ArgumentParser
import logging
from .drivers import Drivers


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--driver', choices=Drivers.choices, default=Drivers.random())
    parser.add_argument('--debug', action='store_true', default=False)
    return parser.parse_args()


def get_driver(driver_name):
    drivers = Drivers()
    return getattr(drivers, driver_name)


def main():
    args = get_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    driver = get_driver(args.driver)
    print(driver())
