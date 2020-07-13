import json
from datetime import date
if __package__ is None or __package__ is "":
  from tools import json_source1
  from tools import datetools
  from tools import dictionarylisttools as jsontools
else:
  from .tools import json_source1
  from .tools import datetools
  from .tools import dictionarylisttools as jsontools


__author__ = 'Jonas Greifenhain'

class Holide():
  """
  Implementation of Holide
  """

  def __init__(self, data):
    self.data = data
    
  @classmethod
  def from_web(cls):
    """
    Creates new Holide that uses data from web.

    :return: New Holide-object
    """
    return cls(json_source1.get_json())
    
  @classmethod
  def from_path(cls, path):
    """
    Creates new Holide that uses data from json-file.

    :param path: Path of json-file
    :return: New Holide-object
    """
    with open(path) as json_file:  
      return cls(json.load(json_file))
    
      
  def save_data(self, path):
    """
    Saves data that Holide is using to JSON-file

    :param path:
    :return:
    """
    with open(path, 'w') as outfile:  
      json.dump(self.data, outfile)
  
  
  def get_federal_state_names(self):
    """
    Returns a list of all federal-state-names in database.
    
    :return: The list
    """
    result = []

    for row in self.data['federal_states']:
      result.append(row['name'])
    return result
  
  
  def belongs_to_only_one_federal_state(self, zipcode):
    """
    Checks whether a zipcode belongs to only one federal state.

    :param zipcode: the federal state
    :return: True/False
    """
    comp = str(zipcode)
    if len(comp) == 4:
      comp = "0" + comp
    data = jsontools.get_all_where(self.data['cities'], {'zip_code': comp})
    
    federal_state_id = -1
    
    for row in data:
      if federal_state_id == -1:
        federal_state_id = row['federal_state_id']
      else:
        if row['federal_state_id'] != federal_state_id:
          return False
    
    assert (federal_state_id != -1), 'Zip-Code ' + str(comp) + ' is not in database!'
          
    return True
  
  
  def __check_zip_code(self, zipcode):
    assert (self.belongs_to_only_one_federal_state(zipcode)), 'This zipcode (' + str(zipcode) + ') belongs to more than one federal state'
  
  def __get_federal_state_id(self, zipcode):
    self.__check_zip_code(zipcode)
    comp = str(zipcode)
    if len(comp) == 4:
      comp = "0" + comp
    return jsontools.get_first_where(self.data['cities'], {'zip_code': comp})['federal_state_id']


  def get_federal_state(self, zipcode):
    """
    Gets the federal state of a zipcode.
    For that the zipcode has to belong to only one federal state

    :param zipcode: The zipcode
    :return: The name of the federal state
    """
    state_id = self.__get_federal_state_id(zipcode)
    return jsontools.get_first_where(self.data['federal_states'], {'id' : state_id})['name']
  
  
  def get_federal_state_code(self, federal_state_name):
    """
    Returns ISO 3166-2-code of federal state

    :param federal_state_name: Name of the federal state
    :return: ISO 3166-2 of federal state
    """
    return jsontools.get_first_where(self.data['federal_states'], {'name' : federal_state_name})['iso3166_2']
  
  
  def get_federal_state_name(self, federal_state_code):
    """
    Returns federal state name that belongs to ISO 3166-2.

    :param federal_state_code: ISO 3166-2 code of federal state.
    :return: Name of federal state
    """
    return jsontools.get_first_where(self.data['federal_states'], {'iso3166_2' : federal_state_code})['name']
    
    
  def __is_federal_state_code(self, code):
    return (len(code) == 2)
  
  
  def __convert_federal_state_code_if_needed(self, code):
    if self.__is_federal_state_code(code):
      code = self.get_federal_state_name(code)
    return code
  

  def __dictionary_contains_date(self, checkdate, dictionary):
    startdate = datetools.date_from_isoformat(dictionary['starts_on'])
    enddate = datetools.date_from_isoformat(dictionary['ends_on'])
    return datetools.is_between(checkdate, startdate, enddate)
    
  
  def is_bank_holiday_in_federal_state(self, checkdate, federal_state):
    """
    Checks whether a date is a bank holiday in a federal state

    :param checkdate: The date
    :param federal_state: The federal state name or ISO 3166-2
    :return: True/False
    """
    federal_state = self.__convert_federal_state_code_if_needed(federal_state)
    federal_state_id = jsontools.get_first_where(self.data['federal_states'], {'name' : federal_state})['id']
    holidays = jsontools.get_all_where(self.data['holidays'], {'federal_state_id' : federal_state_id, 'day' : checkdate.isoformat()})
    if len(holidays) > 0:
      return True
    else:
      return False
  
    
  def is_bank_holiday(self, checkdate):
    """
    Checks whether a date is a bank


    :param checkdate: The date
    :return: True/False
    """
    country_id = jsontools.get_first_where(self.data['countries'], {'name' : 'Deutschland'})['id']
    federal_states = jsontools.get_all_where(self.data['federal_states'], {'country_id' : country_id})
    
    for dataline in federal_states:
      if not (self.is_bank_holiday_in_federal_state(checkdate, dataline['name'])):
        return False
    return True


  def is_bank_holiday_at_zipcode(self, checkdate, zipcode):
    """
    Checks whether a date is a bank holiday at zipcode.

    :param checkdate: The date
    :param zipcode: The zipcode
    :return: True/False
    """
    federal_state_id = self.__get_federal_state_id(zipcode)
    holidays = jsontools.get_all_where(self.data['holidays'], {'federal_state_id' : federal_state_id, 'day' : checkdate.isoformat()})
    if len(holidays) > 0:
      return True
    else:
      return False


  def is_school_holiday_in_federal_state(self, checkdate, federal_state):
    """
    Checks whether a date is a school holiday in federal state.

    :param checkdate: The date
    :param federal_state: The federal state name or ISO 3166-2
    :return: True/False
    """
    federal_state = self.__convert_federal_state_code_if_needed(federal_state)
    federal_state_id = jsontools.get_first_where(self.data['federal_states'], {'name' : federal_state})['id']
    holidays = jsontools.get_all_where(self.data['periods'], {'federal_state_id' : federal_state_id})
    
    for dataline in holidays:
      if self.__dictionary_contains_date(checkdate, dataline):
        return True
    return False


  def is_school_holiday_at_zipcode(self, checkdate, zipcode):
    """
    Checks whether a date is a school holiday at a zipcode.
    The zipcode has to belong to only one federal state.

    :param checkdate: The date
    :param zipcode: The zipcode
    :return: True/False
    """
    federal_state_id = self.__get_federal_state_id(zipcode)
    federal_state = jsontools.get_first_where(self.data['federal_states'], {'id' : federal_state_id})['name']
    return self.is_school_holiday_in_federal_state(checkdate, federal_state)
  
  
  def no_school_in_federal_state(self, checkdate, federal_state):
    """
    This functions checks for a federal state whether a day is off school.

    :param checkdate: The day to check
    :type checkdate: date
    :param federal_state The federal state name or ISO 3166-2
    :return: True or False
    """
    federal_state = self.__convert_federal_state_code_if_needed(federal_state)
    if checkdate.weekday() == 6:
      return True
    
    if self.is_bank_holiday_in_federal_state(checkdate, federal_state):
      return True
    
    if self.is_school_holiday_in_federal_state(checkdate, federal_state):
      return True
      
    return False
    
    
  def no_school_at_zipcode(self, checkdate, zipcode):
    """
    This functions checks for a zipcode whether a day is off school.

    :param checkdate: The day to check
    :type checkdate: date
    :param zipcode: The zipcode of the location
    :return: True or False
    """
    federal_state_id = self.__get_federal_state_id(zipcode)
    federal_state = jsontools.get_first_where(self.data['federal_states'], {'id' : federal_state_id})['name']
    return self.no_school_in_federal_state(checkdate, federal_state)
