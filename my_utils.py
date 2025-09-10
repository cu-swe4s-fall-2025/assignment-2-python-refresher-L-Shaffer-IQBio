def get_column(file_name, query_column, query_value, result_column=1):
    with open(file_name, 'r') as file:
        data = file.readlines()
        results = []
        for line in data [1:]:  # Skip header
            columns = line.strip().split(',')
            if columns[query_column-1] == query_value:
                results.append(columns[result_column-1])
        return results
#print (get_column("Agrofood_co2_emission.csv", 0, "Zimbabwe", 2))


