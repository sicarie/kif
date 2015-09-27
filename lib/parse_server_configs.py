
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

# look through conf for .yaml files, get list of ones we have

# for service, pull in yaml file
# check for conf file, log pass/fail
# parse values from yaml file
