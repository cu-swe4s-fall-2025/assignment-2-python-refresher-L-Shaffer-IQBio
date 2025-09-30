def get_column(file_name, query_column, query_value, result_column=1):
    # Catch file reading errors
    try:
        #read in table file
        with open(file_name, 'r') as file:
            data = file.readlines()
            results = []
            #process each line after the header
            for line in data [1:]:  # Skip header
                columns = line.strip().split(',')
                #alter column indexing
                if columns[query_column-1] == query_value:
                    result = columns[result_column-1]
                    #catch conversion errors
                    try:
                        result = float(result)  # Try converting to float
                        result = int(result)  # Then to int if possible
                    except ValueError:
                        result = 0  # Ensure it's a float if conversion fails 
                    results.append(result)
            return results
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return []

def mean(values):
    if not values:
        return 0
    return sum(values) / len(values)

def median(values):
    if not values:
        return 0
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]
    
def standard_deviation(values):
    if not values:
        return 0
    avg = mean(values)
    # variance = sum((x - avg) ** 2 for x in values) / len(values)
    variance = 0
    for x in values:
        variance += (x - avg) ** 2      
    variance /= len(values)
    return variance ** 0.5

if __name__ == "__main__":
    # Example usage
    fires = get_column("Agrofood_co2_emission.csv", 1, "United States of America", 4)
    print(fires)