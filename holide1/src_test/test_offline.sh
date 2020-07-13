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

start_test unittests/test_zipcodes.py

start_test unittests/test_holidays.py

start_test unittests/test_no_school.py

start_test unittests/test_school_holidays.py
