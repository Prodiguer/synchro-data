#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synchro-data
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @svn_file       $Id: sdeventdao.py 3049 2014-02-09 15:52:49Z jripsl $
#  @version        $Rev: 3049 $
#  @lastrevision   $Date: 2014-02-09 16:52:49 +0100 (Sun, 09 Feb 2014) $
#  @license        CeCILL (http://dods.ipsl.jussieu.fr/jripsl/synchro_data/LICENSE)
##################################

"""Contains event DAO SQL queries."""

import argparse
import sdapp
import sddb
import sdsqlutils
import sdconst
import sdconfig
from sdtypes import Event

def add_event(event,commit=True,conn=sddb.conn):
    keys_to_insert=['name', 'status', 'project', 'model', 'dataset_pattern', 'variable', 'filename_pattern', 'crea_date', 'priority']

    if sdconfig.config.get('daemon','post_processing')=='1':
        sdsqlutils.insert(event,keys_to_insert,commit,conn)

def get_events(limit=None,conn=sddb.conn,**search_constraints):
    """
    Note
      - one search constraint must be given at least
      - if 'limit' is None, retrieve all records
    """
    events=[]

    search_placeholder=sdsqlutils.build_search_placeholder(search_constraints)
    orderby="priority DESC, crea_date ASC"
    limit_clause="limit %i"%limit if limit is not None else ""

    c = conn.cursor()
    q="select * from event where %s order by %s %s"%(search_placeholder,orderby,limit_clause)
    c.execute(q,search_constraints)
    rs=c.fetchone()
    while rs!=None:
        events.append(sdsqlutils.get_object_from_resultset(rs,Event))
        rs=c.fetchone()
    c.close()

    return events

def update_events(events,commit=True,conn=sddb.conn):
    keys=['status'] # TODO: maybe add this too => ,'last_mod_date'

    for e in events:
        rowcount=sdsqlutils.update(e,keys,commit,conn)
    
        # check
        if rowcount==0:
            raise SDException("SDEVEDAO-001","event not found (event_id=%s)"%e.event_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    for e in get_events(limit=10,status=sdconst.EVENT_STATUS_NEW):
        print str(e)
