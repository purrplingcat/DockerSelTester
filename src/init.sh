#!/bin/sh

: ${DEBUG:=0}

if [ $# -lt 1 ]; then
	echo "${0}: Missing command"
	exit 1;
fi

if [ "${1}" = "--help" ]; then
	echo "Usage: ${0} [--noxinit] <command>"
	exit 1;
fi

if [ "${1}" = "--noxinit" ]; then
	shift
else
	service xvfb start
	export DISPLAY=:10
	echo ""
fi

if [ $DEBUG -gt 0 ]; then
	echo "Debug level: $DEBUG"
	echo "Running command:  $@"
fi

exec $@
