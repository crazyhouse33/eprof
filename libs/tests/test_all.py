import sys
from generic_output_check import check
import os
import pytest 


def generate_lib_prods(it):

    #C lib

    assert os.WEXITSTATUS( os.system("cmake -DPRODUCT_NUM_IT={} ../C/build".format(it))) ==0

    assert os.WEXITSTATUS( os.system("cmake --build ../C/build --target product")) ==0
    assert os.WEXITSTATUS( os.system("cmake --build ../C/build --target test")) ==0

def test_all_libs():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    for it in [ 100000, 1000, 100]: # we finish by small for other tests
        generate_lib_prods(it)
        check('C', it)

