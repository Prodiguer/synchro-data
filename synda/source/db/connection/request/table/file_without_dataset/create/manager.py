# -*- coding: utf-8 -*-
##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright "(c)2009 Centre National de la Recherche Scientifique CNRS.
#                             All Rights Reserved"
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################
"""
"""
from synda.source.db.connection.request.table.dao.create.manager import Manager as Base

from synda.source.db.connection.request.table.file_without_dataset.create.models import Table

from synda.source.db.connection.request.table.file_without_dataset.create.models import IndexOnFileId

table_name = Table().get_table_name()


class Manager(Base):

    def __init__(self):
        Base.__init__(self, table_name=table_name)
        self.set_data(
            [
                Table(),

                # indexes

                IndexOnFileId(),

            ]
        )
