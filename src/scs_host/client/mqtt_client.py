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

    @classmethod
    def on_message_handler(cls, _subscriber):
        pass


    @classmethod
    def on_topic_message_handler(cls, _subscriber, _msg):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, client, logger, *subscribers):
        """
        Constructor
        """
        self.__client = client                                  # greengrasssdk.client
        self.__logger = logger                                  # Logger
        self.__subscribers = subscribers                        # array of MQTTSubscriber


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
        subscribers = '[' + ', '.join(str(subscriber) for subscriber in self.__subscribers) + ']'

        return "MQTTClient:{client:%s, logger:%s, subscribers:%s}" % (self.__client, self.__logger, subscribers)


# --------------------------------------------------------------------------------------------------------------------

class MQTTSubscriber(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, topic, handler):
        """
        Constructor
        """
        self.__topic = topic
        self.__handler = handler


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def topic(self):
        return self.__topic


    @property
    def handler(self):
        return self.__handler


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTSubscriber:{topic:%s, handler:%s}" % (self.topic, self.handler)
