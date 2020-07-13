#!/usr/bin/env python3

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)

import unittest
from datetime import date
from src.holide import Holide
from src_test.unittests.testhelper import test_zipcodes_data

class ZipcodeTestOnline(unittest.TestCase):
  def setUp(self):
    self.holideo = Holide.from_path(parentdir + '/testfiles/cache.json')
    self.online_h = Holide.from_web()


  def test_belongs_to_one_federal_state(self):
    for zip_code in test_zipcodes_data.zipcodes:
      self.assertEqual(self.holideo.get_federal_state(zip_code), self.online_h.get_federal_state(zip_code),
                       ('result of online- and offline-version do not equal (' + str(zip_code) + ')'))


  def test_belongs_to_multiple_federal_states(self):
    for zip_code in test_zipcodes_data.more_than_one_federal_state:
      with self.assertRaises(Exception): self.online_h.get_federal_state(zip_code)


if __name__ == "__main__": 
  unittest.main()
