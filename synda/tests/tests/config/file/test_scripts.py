# -*- coding: utf-8 -*-
##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright "(c)2009 Centre National de la Recherche Scientifique CNRS.
#                             All Rights Reserved"
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################
"""
 Tests driven by pytest

 Sub-command : GET
 Optional argument : selection_file
 Operating context : file doesn't exist
"""
import pytest

from synda.tests.manager import Manager
Manager().set_tests_mode()

from synda.source.config.file.scripts.models import Config


@pytest.mark.on_all_envs
def test_selection():

    config = Config()

    for identifier in config.get_filenames_identifiers():
        assert config.exists(identifier)

