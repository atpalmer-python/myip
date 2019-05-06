# myip

Query internet resources to determine your external IP address.

## Installation

Install the latest version from this repository:

    pip install https://github.com/atpalmer/myip#egg=myip --user

## Usage

Simple usage:

    myip

A specific driver may be applied using the `--driver` flag:

    myip --driver httpbin

A list of available drivers is available using help:

    myip --help
