"""
Tools for working with dictionary lists.
"""

def get_all_where(data, compare):
  """
  Gets all dictionaries in list that fit to compare-dictionary.

  :param data: List with dictionaries
  :param compare: Dictionary with keys for comparison {'key';'expected value'}
  :return: list with dictionaries that fit to compare
  """
  def check_line(dataline):
    for dictkey in compare.keys():
      if dataline[dictkey] != compare[dictkey]:
        return False
        
    return True

  result = []
  for dataline in data:
    if check_line(dataline):
      result.append(dataline)
      
  return result
  
def get_first_where(data, compare):
  """
  Gets first dictionary in list that fit to compare-dictionary.

  :param data: List with dictionarys
  :param compare: Dictionary with keys for comparison {'key';'expected value'}
  :return: list with dictionarys that fit to compare
  """
  l = get_all_where(data, compare)
  if len(l) < 1:
    raise Exception('Data not found! (' + str(compare) + ')')
  return l[0]

