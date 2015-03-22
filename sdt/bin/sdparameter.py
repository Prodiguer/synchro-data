#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synchro-data
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @svn_file       $Id: sdparameter.py 12605 2014-03-18 07:31:36Z jerome $
#  @version        $Rev: 12609 $
#  @lastrevision   $Date: 2014-03-18 08:36:15 +0100 (Tue, 18 Mar 2014) $
#  @license        CeCILL (http://dods.ipsl.jussieu.fr/jripsl/synchro_data/LICENSE)
##################################

"""This module contains func used to retrieve information from 'parameter' token list."""

import argparse
import sdpipeline
import sdstream
import sdi18n

def extract_values_from_parameter(parameter,name):
    facets_groups=sdpipeline.parse(parameter)
    values=sdstream.get_facet_values(facets_groups,name)
    return values

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('parameter',nargs='*',default=[],help=sdi18n.m0001)
    args = parser.parse_args()

    # test
    values=extract_values_from_parameter(args.parameter,'project')
    print values
