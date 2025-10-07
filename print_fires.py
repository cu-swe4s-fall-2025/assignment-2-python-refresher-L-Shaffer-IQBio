from my_utils import get_column
import argparse

parser = argparse.ArgumentParser(
    prog='print_fires',
    description='Country fires separated by column specification',
    epilog="")

# country='United States of America'
# country_column = 1
# fires_column = 4
# file_name = 'Agrofood_co2_emission.csv'


parser.add_argument('--country', type=str, help='Country name')
parser.add_argument('--country_column', type=int, help='Country column number')
parser.add_argument('--fires_column', type=int, help='Fires column number')
parser.add_argument('--file_name', type=str,
                    default='Agrofood_co2_emission.csv', help='CSV file name')
parser.add_argument('--operation', type=str, default=None,
                    help='Operation to perform on data (mean, median, std)')

args = parser.parse_args()
# print(args.country, args.country_column, args.fires_column, args.file_name)

fires = get_column(args.file_name, args.country_column,
                   args.country, args.fires_column)

if args.operation:
    from my_utils import mean, median, standard_deviation
    if args.operation == 'mean':
        print("Mean:", mean(fires))
    elif args.operation == 'median':
        print("Median:", median(fires))
    elif args.operation == 'std':
        print("Standard Deviation:", standard_deviation(fires))
    else:
        print("Unknown operation. Please use 'mean', 'median', or 'std'.")
else:
    print(fires)
    # esult_column=fires_column
