# This code runs on Python 2.7

"""
Missing the following country codes:
    South America:
        French Guiana (gf)
    Asia:
        Taiwan (Republic of China) (tw)

Middle East:

Africa:
    Western Sahara (eh)

Europe:
"""

# from pygal.i18n import COUNTRIES
from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # South America Countries with ERROR messages/lost data:
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Bolivia':
            return 'bo'
        # Asia Countries with ERROR messages/lost data:
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Lao PDR':
            return 'la'
        # Middle East Countries with ERROR messages/lost data:
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        # African Countries with ERROR messages/lost data:
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        # European Countries with ERROR messages/lost data:
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Moldova':
            return 'md'
    # If the country wasn't found, return None.
    return None

