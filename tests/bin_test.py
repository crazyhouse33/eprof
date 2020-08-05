import pytest
import os

def dont_fail(cmd, path_out):
    assert os.WEXITSTATUS( os.system(cmd)) ==0
    assert os.path.isfile(path_out)

def test_bin():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    dont_fail("PYTHONPATH=.. python3.7 ../eprof/bin/eprof ../libs/C/tests/out/eprof_test -o ./out/kvh_test.kvhf", "./out/kvh_test.kvhf")


