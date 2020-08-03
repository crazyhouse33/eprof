import sys
import pytest
import os
sys.path.append(os.path.abspath(__file__+'/../../..'))
from eprof.file import Event_file
from kvhf.file import KVH_file
from kvhf.history_entry import Serie_stats


def check(library, it):

#    script= '../{}/tests/product*'.format(library)

    script_out='../{}/tests/out/eprof_test'.format(library)


    # Testing if everything is okay

    ev_file= Event_file(script_out)
    got = [(key, entry.event.get_occurence_num()) for key, entry in ev_file.dictionnary_events.items()]
    expected=[('in_for',it*10), ('ext_for',it), ('whole',1)]

    assert sorted(expected) == sorted(got)

    it=10*it
    output_dir='../{}/tests/out/{}.kvhf'.format(library, it)

    # Printing precision report
    ev_file_kvhf= ev_file.to_kvh_file()

    to_print= KVH_file() 

    in_for_entry= ev_file_kvhf.dico['in_for']

    to_print.dico['{}{} Events'.format(library, it)] = in_for_entry

    to_print.dump(output_dir)



    


