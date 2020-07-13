import json
import requests

class Webcache:
  """
  A simple webcache for text and json.
  Using this makes sure that webcontent will be downloaded once only.
  """
  def __init__(self):
    self.textcache = {}
    self.jsoncache = {}

  def get_json(self, url):
    """
    Gets json from cache.
    The json will be added to cache if it is not in cache

    :param url: Url of json
    :type url: str
    :return:
    """
    try:
      test = self.jsoncache[url]
    except KeyError as e:
      r = requests.get(url)
      json_r = r.json()
      self.jsoncache[url] = json_r
    return self.jsoncache[url]

  def get_text(self, url):
    """
    Gets text from cache.
    The text will be added to cache if it is not in cache

    :param url: Url of text
    :type url: str
    :return:
    """
    try:
      test = self.textcache[url]
    except KeyError as e:
      r = requests.get(url)
      text_r = r.text
      self.textcache[url] = text_r
    return self.textcache[url]
