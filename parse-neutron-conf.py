"""
neutron:
    neutron_conf_file_dir:  /etc/neutron
    neutron_conf_files:     neutron.conf
                            api-paste.conf
                            policy.json
                            rootwrap.conf
                            dhcp_agent.ini
                            l3_agent.ini
                            lbaas_agent.ini
                            metadata_agent.ini
    neutron_conf_options:   admin_password = None
                            admin_tenant_name = None
                            admin_user = None
    neutron_log_options:    backdoor_port = None
                            disable_process_locking = False
    neutron_log_dir:        /var/log/neutron/
    neutron_log_files:      dhcp-agent.log
                            l3-agent.log
                            lbaas-agent.log
                            linuxbridge-agent.log
                            metadata-agent.log
                            metering-agent.log
                            openvswitch-agent.log
                            server.log
"""

import lib/parse_conf.py as parse_conf

neutron_config = "/etc/neutron/neutron.conf"
neutron_log_dir = "/var/log/neutron"
neutron_log_files = ['dhcp-agent.log',
                     'l3-agent.log',
                     'lbaas-agent.log',
                     'linuxbridge-agent.log',
                     'metadata-agent.log',
                     'metering-agent.log',
                     'openvswitch-agent.log',
                     'server.log'
                    ]

logs = []
neutron_options = {}
passwords = {}

neutron_options = parse_conf.get_conf(neutron_config)

# look through file for passwords
passwords = parse_conf.pwds_from_cfg(neutron_options)

# if debug = True, parse neutron logfile for passwords
for logfile in neutron_log_files:
    if os.path.exists(neutron_log_dir + logfile):
        with open(neutron_log_dir + logfile, 'rb') as file:
            logs = file.read()
        file.close()
    # what am I looking for inside each file?

# what is neutron backdoor_port and how is it used?
