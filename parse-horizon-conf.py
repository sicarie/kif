dashboard:
    horizon_config_dir:     /etc/openstack-dashboard/
    horizon_config_file:    local_settings.py
        horizon_config_opt_host:    OPENSTACK_HOST = "127.0.0.1"
        horizon_config_opt_url:     "http://%s:5000/v2.0" % OPENSTACK_HOST 
        horizon_config_opt_role:    "Member"
        horizon_config_opt_logging: LOGGING = {json}
    horizon_apache_config_dir:  /etc/apache2/
        horizon_apache_port_file:   ports.conf
        horizon_apache_conf_file:   conf.d/openstack-dashboard.conf
    horizon_rhel_conf_dir:  /var/log/httpd
    horizon_deb_conf_dir:   /var/log/apache2
    horizon_config_file_opts:   access_log
                                error_log
