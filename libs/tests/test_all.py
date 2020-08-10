import sys
from generic_output_check import check
import os
import pytest


def additional_tests():
    # Run Timer of C libs tests
    current = os.getcwd()
    os.chdir('../C/build')

    assert os.WEXITSTATUS(
        os.system(
            "cmake -DCMAKE_BUILD_TYPE=Debug ..")) == 0

    assert os.WEXITSTATUS(os.system("cmake --build . --target all")) == 0
    # Cmake is stupid and output on failure dont work alone
    assert os.WEXITSTATUS(
        os.system("ctest --verbose --output-on-failure")) == 0
    os.chdir(current)

def generate_lib_prods(it):

    # C lib

    # Cmake is stupid and dont offer possibility to test out of build
    current = os.getcwd()
    os.chdir('../C/build')

    assert os.WEXITSTATUS(
        os.system(
            "cmake -DPRODUCT_NUM_IT={} -DCMAKE_BUILD_TYPE=Debug ..".format(it))) == 0

    assert os.WEXITSTATUS(os.system("cmake --build . --target all")) == 0
    # Cmake is stupid and output on failure dont work alone
    assert os.WEXITSTATUS(
        os.system("ctest --verbose --output-on-failure -R product ")) == 0
    os.chdir(current)


def test_all_libs():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    for it in [100000, 1000, 100]:  #  we finish by small for other tests
        generate_lib_prods(it)
        check('C', it)

    additional_tests()
