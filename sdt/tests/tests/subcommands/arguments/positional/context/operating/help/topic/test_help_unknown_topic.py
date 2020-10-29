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
 Optional argument : help
 Operating context : Topic not found
"""
import sys
import pytest

from sdt.bin import synda
from sdt.tests.stderr import HELP_UNKNOWN_TOPIC


@pytest.mark.on_all_envs
def test_help_unknown_topic(capsys):

    sys.argv = ['synda', "help", "unknown topic"]

    with pytest.raises(BaseException) as exception:
        synda.run()
    assert exception.value.code in [0, 1]

    captured = capsys.readouterr()
    assert captured.err == "{}\n".format(
        HELP_UNKNOWN_TOPIC,
    )
