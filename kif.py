"""
Kif is a collection of attack scripts for OpenStack.
Initially this is a loose collection of scripts, but as they grow and
dependencies are clarified, it should be refactored into a collective
project.
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
    logging.basicConfig(filename='kif.log',level=logging.DEBUG)
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
