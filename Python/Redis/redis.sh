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
prog="redis"
# Start daemons.
start() {
if [ -e $redis_pid -a ! -z $redis_pid ];then
	echo $prog" already running...."
	exit 1
fi
echo -n $"Starting $prog "
# Single instance for all caches
$redis_path $redis_conf
RETVAL=$?
[ $RETVAL -eq 0 ] && {
	touch /var/lock/subsys/$prog
	success $"$prog"
}
echo
	return $RETVAL
}
# Stop daemons.
stop() {
	echo -n $"Stopping $prog "
	killproc -d 10 $redis_path
	echo
	[ $RETVAL = 0 ] && rm -f $redis_pid /var/lock/subsys/$prog
	RETVAL=$?
	return $RETVAL
}
# See how we were called.
case "$1" in
	start)
		start
	;;