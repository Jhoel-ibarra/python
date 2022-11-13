def get_population(data):
  population_dict = {
    '2022' : int(data['2022 Population']),
    '2020' : int(data['2020 Population']),
    '2015' : int(data['2015 Population']),
    '2010' : int(data['2010 Population']),
    '2000' : int(data['2000 Population']),
    '1990' : int(data['1990 Population']),
    '1980' : int(data['1980 Population']),
    "1970" : int(data['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
  #print(country)
 # print(data)
  result = list(filter(lambda item: item['Country/Territory'] == country, data))

  return result

def column(data):
  data = list(filter(lambda item: item["Continent"] == "South America", data))
  country = list(map(lambda item : item['Country/Territory'], data))
  column = list(map(lambda item : item['World Population Percentage'], data))
  return country, column  
  
