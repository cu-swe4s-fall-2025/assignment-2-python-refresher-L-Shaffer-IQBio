#!/bin/bash 
# Fetch ssshtesting https://github.com/ryanlayer/ssshtest
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Functional tests for sample data output

run test_for_success python print_fires.py --country "Zambia" --country_column 1 \
--fires_column 3 --file_name "unit_tests/Sample_Agrofood.csv" 
assert_in_stdout "[14834, 14834, 14834, 14834, 14834, 14834, 13593, 13156, 14940]"

run test_for_success python print_fires.py --country "Zambia" --country_column 1 \
--fires_column 3 --file_name "unit_tests/Sample_Agrofood.csv" 
assert_exit_code 0

run test_for_success python print_fires.py --country "Zambia" --country_column 1 \
--fires_column 3 --file_name "unit_tests/Sample_Agrofood.csv" --operation "mean"
assert_in_stdout "Mean: 14521.444444444445"

run test_for_success python print_fires.py --country "Zambia" --country_column 1 \
--fires_column 3 --file_name "unit_tests/Sample_Agrofood.csv" --operation "median"
assert_in_stdout "Median: 14834"

run test_for_success python print_fires.py --country "Zambia" --country_column 1 \
--fires_column 3 --file_name "unit_tests/Sample_Agrofood.csv" --operation "std"
assert_in_stdout "Standard Deviation: 622.5201667614402"

# failed test condition
# run test_for_success python print_fires.py --country "Zmbia" --country_column 1 \
# --fires_column 3 --file_name "unit_tests/Sample_Agrofood.csv" 
# assert_exit_code 33