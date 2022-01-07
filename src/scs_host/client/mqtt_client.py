"""
Created on 23 Jun 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#client
"""

from enum import Enum

from scs_core.data.json import JSONify


# --------------------------------------------------------------------------------------------------------------------

class MQTTState(Enum):
    """
    classdocs
    """
    IDLE = 0
    WAITING_FOR_DATA = 1
    PUBLISHING = 2
    QUEUING = 3


# --------------------------------------------------------------------------------------------------------------------

class MQTTClient(object):
    """
    classdocs
    """
    __PUBLISHING_STATE = {
        MQTTState.IDLE:                 ['A', 'R'],
        MQTTState.WAITING_FOR_DATA:     ['G', 'A'],
        MQTTState.PUBLISHING:           ['G', 'G'],
        MQTTState.QUEUING:              ['G', 'R']
    }

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, client, led, logger):
        """
        Constructor
        """
        self.__client = client                                  # greengrasssdk.client
        self.__led = led                                        # LEDClient
        self.__logger = logger                                  # Logger


    # ----------------------------------------------------------------------------------------------------------------

    def publish(self, publication):
        try:
            payload = JSONify.dumps(publication.payload)

            self.__client.publish(
                topic=publication.topic,
                queueFullPolicy='AllOrException',
                payload=payload,
            )

            self.set_led(MQTTState.PUBLISHING)

            return True

        except Exception as ex:
            self.__logger.error(repr(ex))
            self.set_led(MQTTState.QUEUING)

            return False


    # ----------------------------------------------------------------------------------------------------------------

    def set_led(self, state):
        try:
            colours = self.__PUBLISHING_STATE[state]

        except KeyError as ex:
            self.__logger.error(repr(ex))
            return

        self.__led.state(colours)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTClient:{client:%s, led:%s, logger:%s}" % (self.__client, self.__led, self.__logger)
