"""
Created on 23 Jun 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os

from scs_core.sys.node import Node
from scs_core.sys.persistence_manager import FilesystemPersistenceManager


# --------------------------------------------------------------------------------------------------------------------

class Host(Node, FilesystemPersistenceManager):
    """
    Greengrass core
    """

    # ----------------------------------------------------------------------------------------------------------------
    # directories and files...

    __HOME_DIR =            "/"                                 # hard-coded abs path

    __SCS_DIR =             "SCS"                               # hard-coded rel path

    __LATEST_UPDATE =       "latest_update.txt"                 # hard-coded rel path


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def software_update_report(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------
    # network identity...

    @classmethod
    def name(cls):
        raise NotImplementedError


    @classmethod
    def server_ipv4_address(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def home_path(cls):
        return cls.__HOME_DIR


    @classmethod
    def scs_path(cls):
        return os.path.join(cls.home_path(), cls.__SCS_DIR)
