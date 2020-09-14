# myip

Query internet resources to determine your external IP address.

## Installation

Clone the latest version of this repository and install:

    git clone https://github.com/atpalmer-python/myip.git
    python3 -m pip install myip --user

## Usage

Simple usage:

    myip

A specific driver may be applied using the `--driver` flag:

    myip --driver httpbin

A list of available drivers is available using help:

    myip --help

The `--debug` flag will show debug info for the underlying HTTP library (urllib3):

    $ myip --debug
    DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): icanhazip.com:80
    DEBUG:urllib3.connectionpool:http://icanhazip.com:80 "GET / HTTP/1.1" 200 15
    98.227.173.157
