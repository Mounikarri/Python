from prettytable import PrettyTable

def print_dict_as_table(data_dict):
    # Create a PrettyTable object
    table = PrettyTable()

    # Add columns to the table
    table.field_names = ["Key", "Value"]

    # Add rows to the table from the dictionary
    for key, value in data_dict.items():
        table.add_row([key, value])

    # Print the table
    print(table)

# Example usage
example_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'occupation': 'Engineer'
}

print_dict_as_table(example_dict)
