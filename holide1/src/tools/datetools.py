from datetime import date

def date_from_isoformat(isostring):
  """
  Converts an isostring to date

  :param isostring: The date-string
  :return: The date created from string
  """
  parts = isostring.split("-")
  return date(int(parts[0]), int(parts[1]), int(parts[2]))


def is_between(check, start, end):
  """
  Checks whether a date is between two other dates.

  :param check:
  :type check: date
  :param start:
  :type start: date
  :param end:
  :type end: date
  :return: True or False
  """
  if check < start or end < check:
    return False
  else:
    return True
