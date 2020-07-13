#!/usr/bin/env python3

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)

import unittest
import datetime
from datetime import date
from src.holide import Holide
from src_test.unittests.testhelper import test_federal_state_data

class ZipcodeTestOnline(unittest.TestCase):
  """
  Tests whether the results of an online-Holide-instance and an offline-Holide-instance are equal
  """
  def setUp(self):
    self.holideo = Holide.from_path(parentdir + '/testfiles/cache.json')
    self.online_h = Holide.from_web()


  def test_no_school_in_federal_state(self):
    """
    Tests no_school_in_federal_state function for federal state names
    """
    check_date = date(2018, 5, 5)
    for i in range(70):
      check_date += datetime.timedelta(days=1)
      for federal_state in test_federal_state_data.federal_states:
        self.assertEqual(self.online_h.no_school_in_federal_state(check_date, federal_state),
                            self.holideo.no_school_in_federal_state(check_date, federal_state))


  def test_is_school_holiday_in_federal_state(self):
    """
    Tests is_school_holiday_in_federal_state function for federal state names
    """
    check_date = date(2018, 5, 5)
    for i in range(70):
      check_date += datetime.timedelta(days=1)
      for federal_state in test_federal_state_data.federal_states:
        self.assertEqual(self.online_h.is_school_holiday_in_federal_state(check_date, federal_state),
                            self.holideo.is_school_holiday_in_federal_state(check_date, federal_state))


  def test_is_bank_holiday_in_federal_state(self):
    """
    Tests is_bank_holiday_in_federal_state function for federal state names
    """
    check_date = date(2018, 5, 5)
    for i in range(70):
      check_date += datetime.timedelta(days=1)
      for federal_state in test_federal_state_data.federal_states:
        self.assertEqual(self.online_h.is_bank_holiday_in_federal_state(check_date, federal_state),
                            self.holideo.is_bank_holiday_in_federal_state(check_date, federal_state))
  
  
  def test_no_school_in_federal_state_code(self):
    """
    Tests no_school_in_federal_state function for federal state codes
    """
    check_date = date(2018, 5, 5)
    for i in range(70):
      check_date += datetime.timedelta(days=1)
      for federal_state in test_federal_state_data.federal_states:
        federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
        self.assertEqual(self.online_h.no_school_in_federal_state(check_date, federal_state_code),
                            self.holideo.no_school_in_federal_state(check_date, federal_state_code))


  def test_is_school_holiday_in_federal_state_code(self):
    """
    Tests is_school_holiday_in_federal_state function for federal state codes
    """
    check_date = date(2018, 5, 5)
    for i in range(70):
      check_date += datetime.timedelta(days=1)
      for federal_state in test_federal_state_data.federal_states:
        federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
        self.assertEqual(self.online_h.is_school_holiday_in_federal_state(check_date, federal_state_code),
                            self.holideo.is_school_holiday_in_federal_state(check_date, federal_state_code))


  def test_is_bank_holiday_in_federal_state_code(self):
    """
    Tests is_bank_holiday_in_federal_state function for federal state codes
    """
    check_date = date(2018, 5, 5)
    for i in range(70):
      check_date += datetime.timedelta(days=1)
      for federal_state in test_federal_state_data.federal_states:
        federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
        self.assertEqual(self.online_h.is_bank_holiday_in_federal_state(check_date, federal_state_code),
                            self.holideo.is_bank_holiday_in_federal_state(check_date, federal_state_code))


if __name__ == "__main__": 
  unittest.main()
