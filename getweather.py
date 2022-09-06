#!/bin/env python3
import sys
import os

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# Env variables
try:
  city = apiKey = os.environ['OWM_CITY']
except:
  print('OWN CITY not set!')
  sys.exit(1)

try:
  apiKey = os.environ['OWM_API_KEY']
except:
    print('OWM_API_KEY not set!')
    

owm = OWM(apiKey)
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather


print('city="{0}", description="{1}", temperature="{2}", humidity="{3}"'.format(city, w.detailed_status, w.temperature('celsius')['temp'] , w.humidity ))