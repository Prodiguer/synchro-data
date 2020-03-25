#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright (c)2009 Centre National de la Recherche Scientifique CNRS.
#                             All Rights Reserved
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module translates facets names.

Note
    - this module is not exactly the reverse of the 'sdremote2local' module,
      (e.g. non injective because of 'time_frequency' and 'instance_id')
"""
from sdt.bin.commons.facets import sdtranslate

name_rules = {
    'frequency': 'time_frequency',
    'datanode': 'data_node',
    'filename': 'title',
    'file_functional_id': 'instance_id',
    'dataset_functional_id': 'dataset_id'
}


def run(facets_groups):
    facets_groups_new = []
    # Just a fix for CMIP5 specific translations.
    for facets_group in facets_groups:
        # shallow copy of the rules
        local_name_rules = name_rules
        if 'project' in facets_group.keys():
            if facets_group['project'] == ['CMIP6']:
                del local_name_rules['frequency']
        facets_group = sdtranslate.translate_name(facets_group, local_name_rules)
        facets_groups_new.append(facets_group)
    return facets_groups_new
