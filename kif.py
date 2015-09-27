"""
Kif is a collection of attack scripts for OpenStack.
Initially this is a loose collection of scripts, but as they grow and
dependencies are clarified, it should be refactored into a collective
project.
"""

import logging
import os


#import lib.defaults as default
import lib.parse_service_configs.py as parse_service_configs


def main():
    _init_logger()
    logger.info('Starting program.')

    _check_root()  # I don't think we care if we're root, but it's here just in case
    
    # Try non-intrusive recon first, so check if we can get into service logs
    services = parse_service_configs.get_service_list()
    for service in services:
        # log attempted load
        # load service yaml
        # if successful, log config details to kif.log
        pass
    
    # Is there a way to determine OpenStack release (juno, havana, kilo, etc...)?
    
    # Probably going to use requests lib for REST query
    # Determine API endpoints
    # Get token
    # Source openrc
    # Enumerate attacks in modules/
    # Call with populated options


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
