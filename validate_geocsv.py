#!/usr/bin/env python

from geocsv import geocsv

c = geocsv('SKQ201715S_control.geoCSV')

print(c.validate())
