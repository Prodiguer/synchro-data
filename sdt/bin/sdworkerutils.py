#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module contains worker related objects."""

import traceback
import sys
import threading
import sdapp
import sdlog
import sdconfig
from sdexception import CertificateRenewalException

class WorkerThread(threading.Thread):
    """This class is the thread that take care of the file transfer."""

    def __init__(self,instance,queue,service):
        threading.Thread.__init__(self)
        self._queue=queue       # the queue where to push the item once work is done to deferre database I/O
        self._instance=instance # the item being processed
        self._service=service   # the service used to process the item

    def run(self):
        try:
            self._service.run(self._instance)
            self._queue.put(self._instance) # add item in queue to handle database I/O in the main process
        except CertificateRenewalException, e:
            sdlog.error("SDWUTILS-003","Certificate error: the daemon must be stopped")
            sdlog.error("SDWUTILS-001","Thread didn't complete successfully")

            # no need to log stacktrace here as exception is already logged downstream

            self._service.exception_occurs=True

        except Exception, e:
            sdlog.error("SDWUTILS-002","Thread didn't complete successfully")
            sdtrace.log_exception(stderr=True)
            self._service.exception_occurs=True
