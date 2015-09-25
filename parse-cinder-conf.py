cinder:
    cinder_conf_dir:        /etc/cinder/
    cinder_conf_file:       cinder.conf
        cinder_conf_options:    use_syslog=true
    cinder_rootwrap_conf:   rootwrap.conf
        cinder_rootwrap_opt:    sql_connection = mysql://user:grp@host/cinder
        cinder_api_opt:         api_paste_config = /etc/cinder/api-paste.ini
        cinder_rabbit_host:     rabbit_host = 10.0.0.1
        cinder_rabbit_user:     rabbit_userid = user
        cinder_rabbit_pw:       rabbit_password = pw
    cinder_log_dir:         /var/log/cinder/
    cinder_api_log:         api.log
    cinder_manage_log:      cinder-manage.log
    cinder_scheduler_log:   scheduler.log
    cinder_volume_log:      volume.log
# from juno current config ref
# logger_<service>
# level = DEBUG \| INFO \| WARNING \| ERROR

