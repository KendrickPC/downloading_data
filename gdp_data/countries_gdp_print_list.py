# Open Knowledge Foundation GDP Data
# http://data.okfn.org/data/core/gdp/

"""
Writing a program that generates a dictionary with Pygal's
two-letter country codes as its keys and chosen data from
the file as its values.
Plotting data on a Worldmap and style the map.
"""

import json

from pygal.maps.world import World
from countries_gdp import get_country_code

# Load the data into a list.
filename = 'gdp.json'
with open(filename) as f:
    # Changed pop_data to gdp_data
    gdp_data = json.load(f)

# Print the GDP for each country.
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp_value = int(float(gdp_dict['Value']))
        print(country_name + ": " + str(gdp_value))
