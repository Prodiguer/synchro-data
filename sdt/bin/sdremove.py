#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module contains 'synda remove' related routines."""

import sys
import argparse
from sdtools import print_stderr
import sdexception
import sddelete
import sddeletefile
import sddeletedataset
import sdoperation

def run(args):
    import syndautils

    syndautils.check_daemon()

    try:
        metadata=syndautils.file_full_search(args)
    except sdexception.EmptySelectionException, e:
        print_stderr('No packages will be installed, upgraded, or removed.')
        return 0

    if not args.dry_run:
        import humanize, sdsimplefilter, sdconst, sdutils

        # filtering

        metadata=sdsimplefilter.run(metadata,'status',sdconst.TRANSFER_STATUS_NEW,'remove')
        metadata=sdsimplefilter.run(metadata,'status',sdconst.TRANSFER_STATUS_DELETE,'remove') # maybe not needed as we now do immediate delete

        count_delete=metadata.count()

        metadata_done=sdsimplefilter.run(metadata.copy(),'status',sdconst.TRANSFER_STATUS_DONE,'keep')
        size_delete=metadata_done.size

        if count_delete>0:

            print_stderr('%i file(s) will be removed.'%count_delete)
            print_stderr('After this operation, %s of disk space will be freed.'%humanize.naturalsize(size_delete,gnu=False))

            # ask user for confirmation
            interactive=not args.yes
            if interactive:
                if sdutils.query_yes_no('Do you want to continue?', default="no"):
                    suppression_confirmed=True
                else:
                    print_stderr('Abort.')
                    return 1
            else:
                suppression_confirmed=True

            # perform deletion
            if suppression_confirmed:
                remove(metadata)
                return 0

        else:
            print_stderr('Nothing to delete.')
            return 0

def remove(files):

    # first step, change the files status from 'done' to 'delete' (update metadata)
    nbr=sddelete.run(files)
    print_stderr("%i file(s) removed"%nbr)

    # second step, do the deletion (remove files on filesystem and remove files metadata)
    # (to do a deferred deletion (i.e. by the daemon), comment line below)
    sddeletefile.delete_transfers()

    # Third step is to remove orphan dataset
    sddeletedataset.purge_orphan_datasets()

    # Fourth step is to remove orphan folder.
    sdoperation.cleanup_tree()

# init.

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
