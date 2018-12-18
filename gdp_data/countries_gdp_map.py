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
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# Load the data into a list.
filename = 'gdp.json'
with open(filename) as f:
    # Changed pop_data to gdp_data
    gdp_data = json.load(f)

# Print the GDP for each country.
# Building a dictionary for GDP data.
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp_value = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp_value
        # Prints Error value keypairs
        #     print(code + ": " + str(gdp_value))
        # else:
        #     print('ERROR - ' + country_name)

        # print(country_name + ": " + str(gdp_value))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Gross Domestic Product in 2016, by Country'
wm.add('2016', cc_gdp)

wm.render_to_file('gross_domestic_product.svg')






