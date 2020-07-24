"""
Created on 23 Jun 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.data.json import JSONify


# --------------------------------------------------------------------------------------------------------------------

class MQTTClient(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, client, logger):
        """
        Constructor
        """
        self.__client = client                                  # greengrasssdk.client
        self.__logger = logger                                  # Logger


    # ----------------------------------------------------------------------------------------------------------------

    def publish(self, publication):
        payload = JSONify.dumps(publication.payload)

        # self.__logger.info("publication: %s" % publication)
        # self.__logger.info("payload: %s" % payload)

        try:
            self.__client.publish(
                topic=publication.topic,
                queueFullPolicy='AllOrException',
                payload=payload,
            )

        except Exception as ex:
            self.__logger.error(repr(ex))


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTClient:{client:%s, logger:%s}" % (self.__client, self.__logger)
