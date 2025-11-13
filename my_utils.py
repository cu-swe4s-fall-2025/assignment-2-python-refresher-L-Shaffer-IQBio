"""Utility helpers for simple CSV column queries.

This module provides lightweight utilities used by small scripts in this
exercise. The functions intentionally avoid heavy dependencies and are
meant for teaching/demo purposes rather than production CSV handling.
"""


def get_column(file_name, query_column, query_value, result_column=1):
    """Return values from `result_column` for rows where
    `query_column` equals `query_value`.

    Arguments:
        file_name (str): Path to a CSV file. The file is expected to
            have a header row.
        query_column (int): 1-based index of the column to match against
            `query_value`.
        query_value (str): The string value to match in the
            `query_column`.
        result_column (int): 1-based index of the column to return for
            matching rows.

    Returns:
        list: A list of numeric values (int when possible, otherwise 0 for
            non-numeric) corresponding to `result_column` for each matching
            row. If the file cannot be found an empty list is returned.

    """
    # Attempt to open and read the file; return an empty list if missing.
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        # Keep behavior simple for learners: print an error and return an
        # empty list.
        print(f"Error: The file {file_name} was not found.")
        return []

    results = []
    # Iterate rows after the header row.
    for line in data[1:]:
        # Trim whitespace/newline and split on commas (simple parser).
        columns = line.strip().split(',')

        # Convert 1-based index to 0-based for Python lists.
        q_idx = query_column - 1
        r_idx = result_column - 1

        # Guard against short/malformed rows.
        if (
            q_idx < 0
            or r_idx < 0
            or q_idx >= len(columns)
            or r_idx >= len(columns)
        ):
            # Skip rows that don't have enough columns.
            continue

        # If the query column matches the requested value, extract the result.
        if columns[q_idx] == query_value:
            result = columns[r_idx]
            # Try to convert numeric-looking values to int when possible.
            try:
                # Convert to float first to handle values like '3.0', then to
                # int if exact.
                num = float(result)
                # Use int if it's mathematically an integer value.
                if num.is_integer():
                    result = int(num)
                else:
                    result = num
            except ValueError:
                # Non-numeric results are normalized to 0 for this exercise.
                result = 0

            results.append(result)

    return results


if __name__ == "__main__":
    # Example usage when run as a script. This helps students quickly inspect
    # function behavior without writing separate test harnesses.
    fires = get_column("Agrofood_co2_emission.csv", 1,
                       "United States of America", 4)
    print(fires)
