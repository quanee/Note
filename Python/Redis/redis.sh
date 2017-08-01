#!/bin/sh
# chkconfig:   2345 90 10
# description:  Redis is a persistent key-value database
# redis    Startup script for redis processes
# processname: redis
redis_path="/usr/local/bin/redis-server"
redis_conf="/etc/redis.conf"
redis_pid="/var/run/redis.pid"
# Source function library.
. /etc/rc.d/init.d/functions
[ -x $redis_path ] || exit 0
RETVAL=0