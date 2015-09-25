keystone:
    keystone_conf_dir:      /etc/keystone/
    keystone_conf_file:     keystone.conf
    keystone_conf_options:  log_config = file
                            use_syslog=true
                            admin_user = admin
                            admin_password = pw
                            admin_endpoint = None
                            admin_token = TOKEN


