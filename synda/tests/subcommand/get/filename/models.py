# -*- coding: utf-8 -*-
##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright "(c)2009 Centre National de la Recherche Scientifique CNRS.
#                             All Rights Reserved"
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################
from synda.tests.subcommand.get.models import SubCommand as Base
from synda.tests.exceptions import MethodNotImplemented


class DestFolderGetSubCommand(Base):

    def __init__(self, context, exceptions_codes=None):
        super(DestFolderGetSubCommand, self).__init__(
            context,
            exceptions_codes=exceptions_codes,
            description="Download configuration is given by command line",
        )

        self.configure(
            context.get_file().get_folder(),
            context.get_file().get_filename(),
        )

    def configure(self, dest_folder, filename):

        self.set_argv(
            ['', self.name, "--verify_checksum", "--dest_folder", dest_folder, filename],
        )


class ConfigSubCommand(Base):

    def __init__(self, context):
        super(ConfigSubCommand, self).__init__(
            context,
            description="Download configuration is given by file",
        )
        self.configure(
            context.get_file().get_filename(),
        )

    def configure(self, filename):

        self.set_argv(
            ['synda', self.name, "--verify_checksum", filename],
        )
