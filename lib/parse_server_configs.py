
"""
Parse service configuration files, if we're able to.
For each service configuration file to analyze, there needs to be a
corresponding <service>.yaml file in conf/. Then parse-config will
attempt to extract the values inside that YAML file for each config
file it is able to read.

These are then stored both in memory and in the kif logfile.
"""


# imports


# initialize logger


"""
Library function to help parse service configuration and log files.

:param: -
:returns: List of services that we have conf/<service>.yaml files for
"""
def enum_services():
  # look through conf for .yaml files, get list of ones we have
  services = []


"""
Function to load the YAML files discovered in conf/

:param services: The list of services we are going to try to load values for
:returns: A dict of files and values to search for inside those files
"""
def load_service_yaml(services):
  # for service, pull in yaml file
  # check for conf file, log pass/fail


"""
Function to get values for those things we enumerated

:param dict: The dict containing the files and values we want to extract
:returns: A dict of values we were able to access, these are also logged
"""
def enum_vals(dict):
  # parse values from yaml file
