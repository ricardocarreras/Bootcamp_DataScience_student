# El primer paso es convertir una fecha estática en dinámica
from datetime import datetime

# Problema: Calcular la edad basada en la fecha de nacimiento
years = [1964, 1950, 1981, 1880, 1980, 1981, 1963, 2001]

# Definición de la función get_average_age
def get_average_age(birth_year):
    # El primer paso es convertir una fecha estática en dinámica
  from datetime import datetime
  this_year = datetime.today().year
  ages = []
  for year in birth_year:
    age = this_year - year
    ages.append(age)
  print(ages)
  age_mean = sum(ages) / len(ages)

  print("***"*20)
  return age_mean # en este caso devolvemos un resultado de la variable age_mean
  print("/$"*20)


get_average_age(years)