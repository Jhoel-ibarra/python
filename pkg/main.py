import util
import read_csv
import charts
import pandas as pd


def run():
  data = read_csv.read_csv('data.csv')
  country = input("country => ")
  result= util.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values= util.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"],labels, values)


def poblacion():
  '''
  data = read_csv.read_csv('data.csv')
  country, column = util.column(data)
  '''
  df = pd.read_csv('data.csv')
  df = df[df["Continent"] == "Africa"]
  country = df["Country/Territory"].values
  column = df["World Population Percentage"].values

  charts.generate_pie_chart(country, column)

if __name__ == '__main__':
  run()
  poblacion()