#!/usr/bin/env python3

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

import unittest
import datetime
from datetime import date
from src.holide import Holide
from src_test.unittests.testhelper import school_holiday_data
from src_test.unittests.testhelper import test_zipcodes_data
from src_test.unittests.testhelper import test_federal_state_data

class SchoolHolidaysTest(unittest.TestCase):
  def setUp(self):
    self.holideo = Holide.from_path(parentdir + '/testfiles/cache.json')


  def test_holidays_federal_states(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      for holidays in federal_state_row['holiday']:

        date = holidays['starts_on']
        date -= datetime.timedelta(days=1)
        end_date = holidays['ends_on']

        while date != end_date:
          date += datetime.timedelta(days=1)
          self.assertTrue(self.holideo.is_school_holiday_in_federal_state(date, federal_state),
                          (federal_state + ': ' + str(date)))


  def test_holidays_federal_state_codes(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
      for holidays in federal_state_row['holiday']:

        date = holidays['starts_on']
        date -= datetime.timedelta(days=1)
        end_date = holidays['ends_on']

        while date != end_date:
          date += datetime.timedelta(days=1)
          self.assertTrue(self.holideo.is_school_holiday_in_federal_state(date, federal_state_code),
                          (federal_state + ' / ' + federal_state_code + ': ' + str(date)))


  def test_holidays_zipcodes(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcode = test_zipcodes_data.get_zipcodes(federal_state)[0]
      for holidays in federal_state_row['holiday']:

        date = holidays['starts_on']
        date -= datetime.timedelta(days=1)
        end_date = holidays['ends_on']

        while date != end_date:
          date += datetime.timedelta(days=1)
          self.assertTrue(self.holideo.is_school_holiday_at_zipcode(date, zipcode),
                          (federal_state + ' (' + str(zipcode) + '): ' + str(date)))


  def test_holidays_many_zipcodes(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcode_list = test_zipcodes_data.get_zipcodes(federal_state)
      for zipcode in zipcode_list:
        for holidays in federal_state_row['holiday']:

          date = holidays['starts_on']
          date -= datetime.timedelta(days=1)
          end_date = holidays['ends_on']

          while date != end_date:
            date += datetime.timedelta(days=1)
            self.assertTrue(self.holideo.is_school_holiday_at_zipcode(date, zipcode),
                            (federal_state + ' (' + str(zipcode) + '): ' + str(date)))


  def test_no_holidays_federal_states(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      for holidays in federal_state_row['not-holiday']:

        date = holidays['starts_on']
        date -= datetime.timedelta(days=1)
        end_date = holidays['ends_on']

        while date != end_date:
          date += datetime.timedelta(days=1)
          self.assertFalse(self.holideo.is_school_holiday_in_federal_state(date, federal_state),
                          (federal_state + ': ' + str(date)))


  def test_no_holidays_federal_state_codes(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      federal_state_code = test_federal_state_data.federal_state_iso[federal_state]
      for holidays in federal_state_row['not-holiday']:

        date = holidays['starts_on']
        date -= datetime.timedelta(days=1)
        end_date = holidays['ends_on']

        while date != end_date:
          date += datetime.timedelta(days=1)
          self.assertFalse(self.holideo.is_school_holiday_in_federal_state(date, federal_state_code),
                          (federal_state + ' / ' + federal_state_code + ': ' + str(date)))


  def test_no_holidays_zipcodes(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcode = test_zipcodes_data.get_zipcodes(federal_state)[0]
      for holidays in federal_state_row['not-holiday']:

        date = holidays['starts_on']
        date -= datetime.timedelta(days=1)
        end_date = holidays['ends_on']

        while date != end_date:
          date += datetime.timedelta(days=1)
          self.assertFalse(self.holideo.is_school_holiday_at_zipcode(date, zipcode),
                          (federal_state + ' (' + str(zipcode) + '): ' + str(date)))


  def test_no_holidays_many_zipcodes(self):
    for federal_state_row in school_holiday_data.federal_state_holiday:
      federal_state = federal_state_row['federal_state']
      zipcode_list = test_zipcodes_data.get_zipcodes(federal_state)
      for zipcode in zipcode_list:
        for holidays in federal_state_row['not-holiday']:

          date = holidays['starts_on']
          date -= datetime.timedelta(days=1)
          end_date = holidays['ends_on']

          while date != end_date:
            date += datetime.timedelta(days=1)
            self.assertFalse(self.holideo.is_school_holiday_at_zipcode(date, zipcode),
                            (federal_state + ' (' + str(zipcode) + '): ' + str(date)))


  def test_zipcode_belongs_to_multiple_federal_states(self):
    for zip_code in test_zipcodes_data.more_than_one_federal_state:
      with self.assertRaises(Exception): self.holideo.is_school_holiday_at_zipcode(date(2019, 5, 5), zip_code)


if __name__ == "__main__":
  unittest.main()

