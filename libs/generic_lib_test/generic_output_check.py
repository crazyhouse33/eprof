import sys
import pytest
from eprof.event.parser import Event_parser

def check(library):

    script= '../{}/tests/product.*'.format(library)
    script_out='../../dev/data/libprod/{}'.format(library)
    output_dir='../../dev/data/perf/{}.svg'.format(library
    kvh_output_dir='../../dev/data/perf/{}last_result.kvhf'.format(library)


    # Testing if everything is okay
    ev_file= Event_parser(script_out)
    got = [key, entry.event.get_occurence_num() for key, entry in ev_file.dictionnary_events.items()]
    expected=[('whole',1),('ext_for',1000),('in_for',5*1000)]('',),
    assert expected.sort() == got.sort()

    # Printing precision report
    ev_file_kvhf= ev_file_kvhf.to_kvh_file()

    to_print= KVH_file() 

    whole_entry= Serie_stat(means=ev_file_kvhf.dico['whole'].means]
    #
    ext_for_entry= ev_file_kvhf.dico['ext_for']
    in_for_entry= ev_file_kvhf.dico['in_for']

    to_print.dico['{} total_performance'.format(library)] = whole_entry

    to_print.dico['{} nested_event'.format(library)] = ext_for_entry

    to_print.dico['{} glued_event'.format(library)] = in_for_entry

    to_print.dump(kvh_output_dir)


