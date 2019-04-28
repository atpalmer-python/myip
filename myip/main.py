from argparse import ArgumentParser
import logging
import random
from . import drivers


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--driver', choices=drivers.CHOICES, default=random.choice(drivers.CHOICES))
    parser.add_argument('--debug', action='store_true', default=False)
    return parser.parse_args()


def main():
    args = get_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    print(drivers.get_ip(args.driver))
