"""Small script to print values from a CSV by country and column indices.

This script is a minimal CLI wrapper around `get_column` in
`my_utils.py`. It demonstrates use of `argparse` and how to wire a small
utility function into a script for interactive use or simple automation.

Usage example:
    python print_fires.py --country "United States of America" \
        --country_column 1 --fires_column 4
"""

from my_utils import get_column
import argparse


# Configure the CLI for the small script.
parser = argparse.ArgumentParser(
    prog='print_fires',
    description='Country fires separated by column specification',
    epilog=""
)

# Define expected CLI arguments. Column indices are 1-based to match
# spreadsheet-like expectations used in the classroom materials.
parser.add_argument('--country', type=str, help='Country name')
parser.add_argument('--country_column', type=int, help='Country column number')
parser.add_argument('--fires_column', type=int, help='Fires column number')
parser.add_argument(
    '--file_name',
    type=str,
    default='Agrofood_co2_emission.csv',
    help='CSV file name',
)


def main():
    """Parse arguments and print matching column values.

    The function is separated from top-level code so this module can be
    imported in tests without executing the script body immediately.
    """
    args = parser.parse_args()

    # Echo the parsed arguments so users can confirm what the script will do.
    print(args.country, args.country_column, args.fires_column, args.file_name)

    # Call the utility function and print the returned list.
    fires = get_column(
        args.file_name, args.country_column, args.country, args.fires_column
    )
    print(fires)


if __name__ == '__main__':
    main()
