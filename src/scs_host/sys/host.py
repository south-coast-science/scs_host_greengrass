"""
Created on 23 Jun 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os

from scs_core.sys.node import Node


# --------------------------------------------------------------------------------------------------------------------

class Host(Node):
    """
    Greengrass core
    """

    # ----------------------------------------------------------------------------------------------------------------
    # directories and files...

    __HOME_DIR =            "/"                                 # hard-coded abs path

    __SCS_DIR =             "SCS"                               # hard-coded rel path
    __CONF_DIR =            "conf"                              # hard-coded rel path
    __AWS_DIR =             "aws"                               # hard-coded rel path

    __LATEST_UPDATE =       "latest_update.txt"                 # hard-coded rel path


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def software_update_report(cls):
        try:
            f = open(os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__LATEST_UPDATE))
            report = f.read().strip()
            f.close()

            return report

        except FileNotFoundError:
            return None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def name(cls):
        raise NotImplementedError


    @classmethod
    def server_ipv4_address(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def ndir_spi_bus(cls):
        raise NotImplementedError


    @classmethod
    def ndir_spi_device(cls):
        raise NotImplementedError


    @classmethod
    def opc_spi_bus(cls):
        raise NotImplementedError


    @classmethod
    def opc_spi_device(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def disk_usage(cls, volume):
        raise NotImplementedError()


    # ----------------------------------------------------------------------------------------------------------------

    def time_is_synchronized(self):
        raise NotImplementedError()


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def home_dir(cls):
        return cls.__HOME_DIR


    @classmethod
    def lock_dir(cls):
        raise NotImplementedError


    @classmethod
    def tmp_dir(cls):
        raise NotImplementedError


    @classmethod
    def command_dir(cls):
        raise NotImplementedError


    @classmethod
    def scs_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR)


    @classmethod
    def conf_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__CONF_DIR)


    @classmethod
    def aws_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__AWS_DIR)


    @classmethod
    def osio_dir(cls):
        raise NotImplementedError


    @classmethod
    def eep_image(cls):
        raise NotImplementedError
