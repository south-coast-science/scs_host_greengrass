"""
Created on 14 Jul 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

praxis.meteo.val.hmd,praxis.meteo.val.tmp,praxis.pmx.val.per,praxis.pmx.val.bin:0,praxis.pmx.val.bin:1,praxis.pmx.val.bin:2,praxis.pmx.val.bin:3,praxis.pmx.val.bin:4,praxis.pmx.val.bin:5,praxis.pmx.val.bin:6,praxis.pmx.val.bin:7,praxis.pmx.val.bin:8,praxis.pmx.val.bin:9,praxis.pmx.val.bin:10,praxis.pmx.val.bin:11,praxis.pmx.val.bin:12,praxis.pmx.val.bin:13,praxis.pmx.val.bin:14,praxis.pmx.val.bin:15,praxis.pmx.val.bin:16,praxis.pmx.val.bin:17,praxis.pmx.val.bin:18,praxis.pmx.val.bin:19,praxis.pmx.val.bin:20,praxis.pmx.val.bin:21,praxis.pmx.val.bin:22,praxis.pmx.val.bin:23,praxis.pmx.val.mtf1,praxis.pmx.val.mtf3,praxis.pmx.val.mtf5,praxis.pmx.val.mtf7,praxis.pmx.val.sfr,praxis.pmx.val.sht.hmd,praxis.pmx.val.sht.tmp
"""

import json
import boto3

from collections import OrderedDict


# -----------------------------------------------------------------------------

class S1N3PMxDatum(object):
    """
    classdocs
    """

    # -------------------------------------------------------------------------
    # ml.t2.medium

    EXG_NAME = 's1/N3/h1'

    PM1_ENDPOINT_NAME = 'AutoML-pm1-h1-notebook-run-19-13-52-32'
    PM2p5_ENDPOINT_NAME = 'AutoML-pm2p5-h1-notebook-run-19-19-47-51'
    PM10_ENDPOINT_NAME = 'AutoML-pm10-h1-notebook-run-19-16-27-25'

    # -------------------------------------------------------------------------

    RUNTIME = boto3.client('runtime.sagemaker')


    # -------------------------------------------------------------------------

    @classmethod
    def __infer(cls, model_endpoint_name, csv):
        response = cls.RUNTIME.invoke_endpoint(EndpointName=model_endpoint_name,
                                               ContentType='text/csv',
                                               Body=csv)

        return json.loads(response['Body'].read().decode())


    # -------------------------------------------------------------------------

    def __init__(self, pmx_jdict, climate_jdict):
        """
        Constructor
        """
        self.__pmx_jdict = pmx_jdict                    # jdict
        self.__climate_jdict = climate_jdict            # jdict


    # -------------------------------------------------------------------------

    def infer(self):
        csv = self.as_csv()

        # pm1 = self.__infer(self.PM1_ENDPOINT_NAME, csv)
        pm2p5 = self.__infer(self.PM2p5_ENDPOINT_NAME, csv)
        # pm10 = self.__infer(self.PM10_ENDPOINT_NAME, csv)

        # return pm1, pm2p5, pm10
        return None, pm2p5, None


    # -------------------------------------------------------------------------

    def as_csv(self):
        pmx_val = self.__pmx_jdict['val']
        climate_val = self.__climate_jdict['val']

        cells = [
            climate_val['hmd'],
            climate_val['tmp'],
            pmx_val['per']
        ]

        cells.extend(pmx_val['bin'])

        cells.extend((
            pmx_val['mtf1'],
            pmx_val['mtf3'],
            pmx_val['mtf5'],
            pmx_val['mtf7'],
            pmx_val['sfr'],
            pmx_val['sht']['hmd'],
            pmx_val['sht']['tmp']
        ))

        return ','.join([str(cell) for cell in cells])


    def as_json(self, pm1, pm2p5, pm10):
        jdict = self.__pmx_jdict

        if 'exg' not in jdict:
            jdict['exg'] = OrderedDict()

        jdict['exg'][self.EXG_NAME] = OrderedDict()

        jdict['exg'][self.EXG_NAME]['pm1'] = None if pm1 is None else round(pm1, 1)
        jdict['exg'][self.EXG_NAME]['pm2p5'] = None if pm1 is None else round(pm2p5, 1)
        jdict['exg'][self.EXG_NAME]['pm10'] = None if pm1 is None else round(pm10, 1)

        return jdict


    # -----------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "S1N3PMxDatum:{pmx_jdict:%s, climate_jdict:%s}" % \
               (self.__pmx_jdict, self.__climate_jdict)
