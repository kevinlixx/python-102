import mod
import read_csv
import charts


def run():
  data = read_csv.read_csv(
      './app/data.csv'
  )  #esta linea de codigo lo que hace es llamar a la funcion read_csv que esta en el modulo read_csv
  data = list(filter(lambda item: item['Continent'] == 'South America',data)) #esta linea de codigo lo que hace es filtrar la lista de diccionarios con el contin
  
  countries = list(map(lambda x: x['Country/Territory'], data)) #esta linea de codigo lo que hace es crear una lista con los paises de la lista de diccion
  
  porcentages = list(map(lambda x: x['World Population Percentage'], data))#esta linea de codigo lo que hace es crear una lista con los porcentajes de la lista de diccion
  
  charts.generate_pie_chart(countries, porcentages) #esta linea de codigo lo que hace es generar un grafico de torta con los datos de 
  '''
  country = input('Type Country => ')
  
  result = mod.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = mod.get_population(country)
    charts.generate_bar_chart( labels, values)
    
'''


if __name__ == '__main__':
  run()
