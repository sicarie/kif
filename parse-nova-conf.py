"""
nova:
    log_dir:         /var/log/nova/
    log_files:       api.log
                     cert.log
                     compute.log
                     conductor.log
                     consoleauth.log
                     network.log
                     nova-manage.log
                     scheduler.log
    log_config_file: /etc/nova/logging.conf
    nova_dir:        /etc/nova/
    nova_conf_file:  nova.conf
    nova_reference:  http://docs.openstack.org/juno/config-reference/content/list-of-compute-config-options.html
"""

import lib/parse_conf.py as parse_conf

nova_conf = '/etc/nova/nova.conf'
nova_options = {}

nova_options = parse-conf.get_conf(nova_conf)
