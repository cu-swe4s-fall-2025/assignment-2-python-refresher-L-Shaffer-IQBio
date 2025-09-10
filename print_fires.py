country='United States of America'
country_column = 1
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'
from my_utils import get_column

fires = get_column(file_name, country_column, country, fires_column)
print(fires)