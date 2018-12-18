# Can't import COUNTRIES from pygal.i18n
# https://stackoverflow.com/questions/35770931/cant-import-countries-from-pygal-i18n
# Solution:
# https://ehmatthes.github.io/pcc/chapter_16/README.html

from pygal.maps.world import COUNTRIES


for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
