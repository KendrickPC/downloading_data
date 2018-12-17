"""
Working with population_data.py data file first.
Note that Year and Population are integers and not strings in
population_data_two.py
"""
import json

# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ": " + str(population))
