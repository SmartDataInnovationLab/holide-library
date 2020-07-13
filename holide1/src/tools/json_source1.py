import json
import requests
from contextlib import closing
import csv
import codecs
if __package__ is None or __package__ is "":
  from webcache import Webcache
  import dictionarylisttools
else:
  from .webcache import Webcache
  from . import dictionarylisttools


def get_json():
  """
  Creates a json with data for holide from web.

  :return: json
  """
  w_cache = Webcache()

  def get_iso_3166_2():
    iso_3166_2 = {}
    json_content = w_cache.get_json('https://www.spiketime.de/feiertagapi/bundeslaender')

    for element in json_content:
      iso_3166_2[element['Name']] = element['Abkuerzung']

    return iso_3166_2


  def get_data(table):
    url='https://www.mehr-schulferien.de/api/v1.0/' + table

    data = w_cache.get_json(url)['data']
    return data

  def get_federal_state_id_by_name(name):
    data = get_data('federal_states')
    return dictionarylisttools.get_first_where(data, {'name': name})['id']


  def get_countries():
    result = []
    def add_country(id, name):
      dictionary = {"id" : id, "name" : name}
      result.append(dictionary)

    data = get_data('countries')
    for dataline in data:
      add_country(dataline['id'], dataline['name'])

    return result


  def get_federal_states():
    result = []

    iso_3166_2 = get_iso_3166_2()
    def add_federal_state(id, name, country_id, iso3166_2):
      dictionary = {"id" : id, "name" : name, "country_id" : country_id, "iso3166_2" : iso3166_2}
      result.append(dictionary)

    data = get_data('federal_states')
    for dataline in data:
      iso = iso_3166_2[dataline['name']]
      add_federal_state(dataline['id'], dataline['name'], dataline['country_id'], iso)

    return result


  def get_cities():
    result = []
    def add_city(id, name, zip_code, federal_state_id):
      dictionary = {"id" : id, "name" : name, "zip_code" : zip_code,
          "federal_state_id" : federal_state_id}
      result.append(dictionary)

    url = 'https://www.suche-postleitzahl.org/download_files/public/zuordnung_plz_ort_landkreis.csv'
    lines = w_cache.get_text(url).splitlines()
    reader = csv.DictReader(lines, delimiter=',')

    for row in reader:
      federal_state = row['bundesland']
      state_id = get_federal_state_id_by_name(federal_state)
      add_city(row['osm_id'], row['ort'], row['plz'], state_id)

    return result


  def get_periods():
    result = []
    def add_period(start_on, ends_on, name, federal_state_id):
      dictionary = {"starts_on" : start_on, "ends_on" : ends_on,
          "name" : name, "federal_state_id" : federal_state_id}
      result.append(dictionary)

    data = get_data('periods')
    for dataline in data:
      add_period(dataline['starts_on'], dataline['ends_on'], dataline['name'], dataline['federal_state_id'])

    return result


  def get_holidays():
    result = []
    def add_country(day, name, federal_state_id):
      dictionary = {"day" : day, "name" : name,
          "federal_state_id" : federal_state_id}
      result.append(dictionary)

    url = 'https://www.spiketime.de/feiertagapi/feiertage/csv/1998/2020'
    lines = w_cache.get_text(url).splitlines()
    reader = csv.DictReader(lines, delimiter=';')

    for row in reader:
      federal_state = row['Land']
      state_id = get_federal_state_id_by_name(federal_state)
      add_country(row['Datum'], row['Feiertag'], state_id)

    return result


  data = {"countries" : get_countries(),
    "federal_states" : get_federal_states(),
    "cities" : get_cities(),
    "periods" : get_periods(),
    "holidays" : get_holidays()}

  return data



