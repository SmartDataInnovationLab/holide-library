#!/usr/bin/env python3

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)

import unittest
from datetime import date
from src.holide import Holide
from src_test.unittests.testhelper import test_zipcodes_data

class ZipcodeTest(unittest.TestCase):
  def setUp(self):
    self.holideo = Holide.from_path(parentdir + '/testfiles/cache.json')


  def test_belongs_to_one_federal_state(self):
    for dataline in test_zipcodes_data.federal_state_zipcode:
      federal_state = dataline['federal_state']
      for zip_code in dataline['zip_codes']:
        self.assertEqual(federal_state, self.holideo.get_federal_state(zip_code), federal_state + ": " + str(zip_code))


  def test_belongs_to_multiple_federal_states(self):
    for zip_code in test_zipcodes_data.more_than_one_federal_state:
      with self.assertRaises(Exception): self.holideo.get_federal_state(zip_code)

if __name__ == "__main__": 
  unittest.main()

