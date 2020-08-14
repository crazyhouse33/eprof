import sys
from generic_output_check import check
import os
import pytest
import subprocess


#the tests are really messy and coupled cause of me trying to using cmake for no reasons. TODO just run product and stop reconfiguring for no reason

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

import shlex
def generate_multi_proc_prods(num_proc, it):
    wd = os.getcwd()
    os.chdir("../C/tests/out")
    Cprocs=[]
    Cprocs.append(subprocess.Popen(shlex.split("../../build/bin/product {}".format(it))))
    for i in range(num_proc-1):
        Cprocs.append( subprocess.Popen(shlex.split("../../build/bin/product {} append".format(it))))
    for proc in Cprocs:
        proc.wait()
        assert proc.returncode ==0
    os.chdir(wd)


def test_all_libs():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    #Test one proc
    for it in [100000, 1000, 10]:  #  we finish by small for other tests
        generate_lib_prods(it)
        check('C', it)

    # Test multi one
    num_proc=50
    generate_multi_proc_prods(num_proc,it)
    check('C',it, num_proc)

    additional_tests()
