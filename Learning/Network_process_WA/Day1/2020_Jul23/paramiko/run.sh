#!/bin/sh
echo $$ > /tmp/service.pid
exec "$@"
