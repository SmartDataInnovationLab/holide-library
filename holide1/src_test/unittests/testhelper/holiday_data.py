from datetime import date

bank_holidays = [date(2018, 1, 1), date(2018, 3, 30), date(2018, 4, 2),
  date(2018, 5, 1), date(2018, 5, 10), date(2018, 5, 21),
  date(2018, 10, 3), date(2018, 12, 25), date(2018, 12, 26)]
  
not_bank_holidays = [date(2018, 1, 6),
  date(2018, 5, 31), date(2018, 8, 8), date(2018, 10, 31),
  date(2018, 11, 1), date(2018, 11, 21)]


federal_state_holiday = [] 


federal_state_holiday.append({'federal_state' : "Baden-Württemberg", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 1, 6), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 6, 20), date(2019, 10, 3), date(2019, 11, 1), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Bayern", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 1, 6), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 6, 20), date(2019, 10, 3), date(2019, 11, 1), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Berlin", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 3, 8), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Brandenburg", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Bremen", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Hamburg", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Hessen", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 6, 20), date(2019, 10, 3), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Mecklenburg-Vorpommern", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Niedersachsen", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Nordrhein-Westfalen", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 6, 20), date(2019, 10, 3), date(2019, 11, 1), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Rheinland-Pfalz", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 6, 20), date(2019, 10, 3), date(2019, 11, 1), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Saarland", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 6, 20), date(2019, 8, 15), date(2019, 10, 3), date(2019, 11, 1), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Sachsen", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 11, 20), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Sachsen-Anhalt", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 1, 6), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Schleswig-Holstein", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })

federal_state_holiday.append({'federal_state' : "Thüringen", 
  'bank-holiday' : [date(2019, 1, 1), date(2019, 4, 19), date(2019, 4, 22), date(2019, 5, 1), date(2019, 5, 30), date(2019, 6, 10), date(2019, 10, 3), date(2019, 10, 31), date(2019, 12, 25), date(2019, 12, 26)],
  'not-bank-holiday' : [date(2019, 5, 7)]
  })




