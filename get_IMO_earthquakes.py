#!/usr/bin/python3
# Read instrumental seimological data from the IMO database (1994-present) 
# and write it as a space separated file

import re
import requests

CATALOGUE_FILE_NAME = 'Catalogue_SIL_sorted'

r = requests.get('http://hraun.vedur.is/ja/viku/?F=0')

# header IMO database
# Nr    Dags.    Timi      Breidd     Lengd   Dypi   M     ML
# index date time lat lon depth M Ml
with open(CATALOGUE_FILE_NAME, 'w') as outfile:
  outfile.write("date time lat lon depth M Ml\n")

  # year enumeration 1994-....
  for year in sorted(set([m.group() for m in re.finditer('(20\d\d|199\d)',  r.text)])): 

    r = requests.get('http://hraun.vedur.is/ja/viku/' +year+ '/?F=0&P=vika*')

    # week enumeration
    weeks = sorted(set([m.group() for m in re.finditer('vika_\d\d',  r.text)]))
    print('current year '+ year + ' number of weeks ' + str(len(weeks)))

    for week in weeks:
      print('available week ' + week)
      r = requests.get('http://hraun.vedur.is/ja/viku/' +year+ '/' +week+ '/listi')

      # remove multiple headers and weekly indexes
      removed_header = re.sub(r'^.*\n', '', r.text)
      removed_first_index = re.sub(r'^ *\d* *', '', removed_header)
      removed_index = re.sub(r'\n *\d* *', '\n', removed_first_index)

      outfile.write(removed_index)
