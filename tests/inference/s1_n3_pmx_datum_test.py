#!/usr/bin/env python3

"""
Created on 27 Jul 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

{"tag": "scs-bgx-538", "src": "N3", "rec": "2020-07-14T08:48:39Z",
"val": {"per": 4.9, "pm1": 2.4, "pm2p5": 4.6, "pm10": 13.8,
"bin": [815, 83, 17, 4, 4, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
"mtf1": 24, "mtf3": 29, "mtf5": 25, "mtf7": 35, "sfr": 5.67, "sht": {"hmd": 43.4, "tmp": 27.5}},
"exg": {"ISLin/N3/vLGW": {"pm1": 2.5, "pm2p5": 2.1, "pm10": 3.0}}}'
"""

import json

from collections import OrderedDict

from scs_core.data.json import JSONify

from scs_host.inference.s1_n3_pmx_datum import S1N3PMxDatum


# --------------------------------------------------------------------------------------------------------------------

pmx_jstr = '{"tag": "scs-bgx-538", "src": "N3", "rec": "2020-07-14T08:48:39Z", ' \
           '"val": {"per": 4.9, "pm1": 2.4, "pm2p5": 4.6, "pm10": 13.8, ' \
           '"bin": [815, 83, 17, 4, 4, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ' \
           '"mtf1": 24, "mtf3": 29, "mtf5": 25, "mtf7": 35, "sfr": 5.67, "sht": {"hmd": 43.4, "tmp": 27.5}}, ' \
           '"exg": {"ISLin/N3/vLGW": {"pm1": 2.5, "pm2p5": 2.1, "pm10": 3.0}}}'

climate_jstr = '{"tag": "scs-bgx-538", "rec": "2020-07-14T08:50:06Z", ' \
           '"val": {"hmd": 72.6, "tmp": 20.1, "bar": null}}'

pmx_jdict = json.loads(pmx_jstr, object_hook=OrderedDict)
climate_jdict = json.loads(climate_jstr, object_hook=OrderedDict)

datum = S1N3PMxDatum(pmx_jdict, climate_jdict)
print(datum)
print("-")

print(datum.as_csv())
print("-")

print(JSONify.dumps(datum.as_json(None, None, None)))
print("-")
