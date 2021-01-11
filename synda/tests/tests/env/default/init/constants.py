# -*- coding: utf-8 -*-
##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright "(c)2009 Centre National de la Recherche Scientifique CNRS.
#                             All Rights Reserved"
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################
import os
from synda.tests import tests

from synda.tests.tests.constants import TESTS_DIR as ROOT

subdirectories = [
    ROOT,
    "env",
    "default",
    "init",
]

TESTS_DIR = os.path.join(*subdirectories)
