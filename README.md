### Installation

Download data set

```bash
curl -L "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr" -o Agrofood_co2_emission.csv
```

### Dependencies

- python3
- argparse

### Usage

```bash
#correct command
python3 print_fires.py --country "Zimbabwe" --country_column 1 \
--fires_column 3 --file_name "Agrofood_co2_emission.csv"

#incorrect output
#additional underscore in _country_column
#misprint in file name
python3 print_fire.py --country "Zimbabwe" --_country_column 1 \
--fires_column 3 --file_name "Agrofood_co2_emission.csv"

#incorrect output
#column numbers were off | resulting open list
python3 print_fires.py --country "Zimbabwe" --country_column 5 \
--fires_column 2 --file_name "Agrofood_co2_emission.csv"
```

### changelog

- get_column implemented to process csv line by line
- my_utils.py & print_fires.py updated
- United States forest fires printed
- conversion to float & int
- addition of argparse command line interface
- v2.1 docstrings incorporated & README update
