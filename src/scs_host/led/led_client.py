"""
Created on 18 Aug 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.data.json import JSONify

from scs_dfe.led.led_state import LEDState


# --------------------------------------------------------------------------------------------------------------------

class LEDClient(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, led_uds, logger):
        """
        Constructor
        """
        self.__led_uds = led_uds                                # UDSWriter
        self.__logger = logger                                  # Logger


    # ----------------------------------------------------------------------------------------------------------------

    def state(self, colours):
        try:
            self.__led_uds.connect()
            self.__led_uds.write(JSONify.dumps(LEDState(colours[0], colours[1])), True)

        except OSError as ex:
            self.__logger.error(repr(ex))

        finally:
            self.__led_uds.close()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LEDClient:{led_uds:%s, logger:%s}" % (self.__led_uds, self.__logger)
