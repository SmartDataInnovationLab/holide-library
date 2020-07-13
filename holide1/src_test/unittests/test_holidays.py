#!/usr/bin/env python3

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

import unittest
from src.holide import Holide
from src_test.unittests.testhelper import test_zipcodes_data
from src_test.unittests.testhelper import holiday_data
from src_test.unittests.testhelper import test_federal_state_data

class Holidays(unittest.TestCase):
  def setUp(self):
    self.holideo = Holide.from_path(parentdir + '/testfiles/cache.json')


  def test_holidays_federal_states(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      for holiday_date in federal_state_row['bank-holiday']:
        self.assertTrue(self.holideo.is_bank_holiday_in_federal_state(holiday_date, federal_state), str(holiday_date))


  def test_not_holiday_federal_states(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      for holiday_date in federal_state_row['not-bank-holiday']:
        self.assertFalse(self.holideo.is_bank_holiday_in_federal_state(holiday_date, federal_state), str(holiday_date))


  def test_holidays_federal_state_codes(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
      for holiday_date in federal_state_row['bank-holiday']:
        self.assertTrue(self.holideo.is_bank_holiday_in_federal_state(holiday_date, federal_state_code), str(holiday_date))


  def test_not_holiday_federal_state_codes(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
      for holiday_date in federal_state_row['not-bank-holiday']:
        self.assertFalse(self.holideo.is_bank_holiday_in_federal_state(holiday_date, federal_state_code), str(holiday_date))


  def test_holidays_zipcode(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcode = test_zipcodes_data.get_zipcodes(federal_state)[0]
      for holiday_date in federal_state_row['bank-holiday']:
        self.assertTrue(self.holideo.is_bank_holiday_at_zipcode(holiday_date, zipcode), str(holiday_date))


  def test_holidays_many_zipcodes(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcodelist = test_zipcodes_data.get_zipcodes(federal_state)
      for holiday_date in federal_state_row['bank-holiday']:
        for zipcode in zipcodelist:
          self.assertTrue(self.holideo.is_bank_holiday_at_zipcode(holiday_date, zipcode), str(holiday_date))


  def test_no_holiday_zipcode(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcode = test_zipcodes_data.get_zipcodes(federal_state)[0]
      for holiday_date in federal_state_row['not-bank-holiday']:
        self.assertFalse(self.holideo.is_bank_holiday_at_zipcode(holiday_date, zipcode), str(holiday_date))


  def test_no_holiday_many_zipcodes(self):
    for federal_state_row in holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcodelist = test_zipcodes_data.get_zipcodes(federal_state)
      for holiday_date in federal_state_row['not-bank-holiday']:
        for zipcode in zipcodelist:
          self.assertFalse(self.holideo.is_bank_holiday_at_zipcode(holiday_date, zipcode), str(holiday_date))


if __name__ == "__main__":
  unittest.main()
