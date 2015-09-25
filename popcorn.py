"""
Popcorn is an OpenStack information profiling tool that parses
files and automates architeture diagrams.
"""

import logging
import os

#import lib.defaults as default

def main():
    _init_logger()
    logger.info('Starting program.')

    _check_root()


def _init_logger():
    """
    Initialize global logging

    :return: -
    """
    logging.basicConfig(filename='popcorn.log',level=logging.DEBUG)
    logging.info('Logging initialized.')
    #formatter = default.format_string
    formatter = logging.Formatter(fmt=format_string)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)


def _check_root():
    """
    Ensure we are the root user, and raise error if not

    :return: -
    """
    logger = getLogger(default.loggerName)
    if os.getuid() != 0:
        logger.error("Must be run as root.")
        exit(2)

if __name__ == "__main__":
    main()
