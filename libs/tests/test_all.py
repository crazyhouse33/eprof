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

    for it in [ 100, 1000, 100000]:
        generate_lib_prods(it)
        check('C', it)

