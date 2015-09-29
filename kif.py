"""
Kif is a collection of attack scripts for OpenStack.
Initially this is a loose collection of scripts, but as they grow and
dependencies are clarified, it should be refactored into a collective
project.
"""

import logging
import os


def main():
    _init_logger()
    logging.info('Starting program.')


def _init_logger():
    """
    Initialize global logging

    :return: -
    """
    logging.basicConfig(filename='kif.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    logging.info('Logging initialized.')


if __name__ == "__main__":
    main()
