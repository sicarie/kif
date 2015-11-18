"""
Kif is a collection of attack scripts for OpenStack.
Initially this is a loose collection of scripts, but as they grow and
dependencies are clarified, it should be refactored into a collective
project.
"""

import logging
import os
import requests
import sys
import yaml


def main(argv):
    _init_logger()
    _load_openrc()
    logging.info('Starting program.')
    try:
        opts, args = getopt.getopt(argv,"he",["endpoint_url="])
    except getopt.GetoptError:
        print 'kif.py <endpoint_url>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'kif.py -e <endpoint_url>'
        elif opt in ("-e", "--endpoint"):
            endpoint_url = arg

    # parse openrc and get token
    _load_openrc()
    '''
    curl -s -X POST http://203.0.113.10:35357/v2.0/tokens \
-d '{"auth": {"passwordCredentials": {"username":"test-user", \
                                      "password":"test-password"},  \
                                      "tenantName":"test-project"}}' \
-H "Content-type: application/json" | jq .
    '''


    # query endpoints

    # run attacks that don't require authentication
    #TODO determine how to pass endpoint details
    noauth_attacks()

    # run auth attacks
    auth_attacks()


def _init_logger():
    """
    Initialize global logging

    :return: -
    """
    logging.basicConfig(filename='kif.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    logging.info('Logging initialized.')


def _load_openrc(rc_file="conf/openrc.sh"):
    """
    Use an openrc file to get creds for interaction.

    :parameters: rc_file - the openrc.sh file containing connection info of the target

    :return: -
    """
    # TODO: fix this to project default dir
    default_dir = '/home/sicarie/projects/kif/'
    openrc_path = default_dir + rc_file
    # TODO: put this in try block & catch non-loadable openrc
    subprocess.check_output('source', openrc_path)
    # TODO: get tests set up - check vars in openrc


def api_discovery():
    # get endpoints


def noauth_attacks():
    # run attacks not requiring authorization


def auth_attacks():
    # get auth
    # run auth attacks


def try_recon(config_file='conf/recon.yaml'):
    config_file = 'conf/recon.yaml'

    try:
        svc = yaml.load(config_file, 'r')
        logging.info("Successfully loaded service config " + config_file + ".")
        logging.info("Service Options:")
        logging.info(svc)
        # TODO: change this from config.split to yaml.dump and real parsing
        try:
            #svc_opts{config.split('.')[1], svc}
        except SyntaxError as e:
                print "ERROR: Unable to parse recon.yaml."
                print "ERROR: Error message: "
                print e

    except:
        logging.info("Unable to load service config " + config_file)
        logging.info("Invalid YAML?")


if __name__ == "__main__":
    main(sys.argv[1:])
