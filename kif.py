"""
Kif is a collection of attack scripts for OpenStack.
Initially this is a loose collection of scripts, but as they grow and
dependencies are clarified, it should be refactored into a collective
project.
"""

import logging
import os
import yaml


def main():
    _init_logger()
    logging.info('Starting program.')
    # get list of files in conf/
    config_dir = 'conf/'
    config_files = []
    for item in config_dir:
        config_candidate = os.path.join(config_dir, item)
        if os.path.isfile(config_candidate):
            config_files.append(config_candidate)
        else:
            logging.info(config_dandidate + "is in conf/ but is not a file.")

    # load the yamls
    svc_opts = {}
    for config in config_candidate:
        try:
            svc = yaml.load(config, 'r')
            logging.info("Successfully loaded service config " + config + ".")
            logging.info("Service Options:")
            logging.info(svc)
            # This is probably not right
            svc_opts{config.split('.')[1], svc}
'''
>>> scope = { 'glance': { '/etc/glance.cfg': [ 'logging_blah', 'audit_blah', 'access_blah'], '/etc/glance2.cfg': [ 'users_blah', ] }, 'nova': { '/etc/nova': [ '1', '2' ] } }
>>> scope
>>> {'glance': {'/etc/glance2.cfg': ['users_blah'], '/etc/glance.cfg': ['logging_blah', 'audit_blah', 'access_blah']}, 'nova': {'/etc/nova': ['1', '2']}}
import yaml
yaml.dump(scope)
>>> "glance:\n  /etc/glance.cfg: [logging_blah, audit_blah, access_blah]\n  /etc/glance2.cfg: [users_blah]\nnova:\n  /etc/nova: ['1', '2']\n”
'''

        except:
            logging.info("Unable to load service config " + config)
            logging.info("Invalid YAML?")

    # So we have

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


if __name__ == "__main__":
    main()
