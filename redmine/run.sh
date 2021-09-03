#!/bin/bash

echo "mode: $MODE"

if [ "$MODE" == 'master' ]; then
  locust --master
elif [ "$MODE" == 'slave' ]; then
  locust --slave --master-host=locust-master
fi