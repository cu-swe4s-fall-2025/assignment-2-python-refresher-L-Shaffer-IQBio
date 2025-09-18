#!/bin/bash
#correct command
python3 print_fires.py --country "Zimbabwe" --country_column 1 \
--fires_column 3 --file_name "Agrofood_co2_emission.csv"

#additional underscore in _country_column
#misprint in file name
python3 print_fire.py --country "Zimbabwe" --_country_column 1 \
--fires_column 3 --file_name "Agrofood_co2_emission.csv"

#column numbers were off | resulting open list 
python3 print_fires.py --country "Zimbabwe" --country_column 5 \
--fires_column 2 --file_name "Agrofood_co2_emission.csv"