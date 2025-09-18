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



if __name__ == "__main__":
    # Example usage
    fires = get_column("Agrofood_co2_emission.csv", 1, "United States of America", 4)
    print(fires)