#!/bin/bash

scriptdir=$(cd $(dirname $0); pwd -P)

start_test() {
  echo "================================="
  echo "================================="
  echo "$1"
  $scriptdir/$1
  echo ""
  echo ""
  echo ""
  echo ""
}

start_test unittests/test_zipcodes_online.py
start_test unittests/test_equals_online.py
