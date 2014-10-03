"""Functions which manipulate or retrieve records about devices under test.

If you have a database hooked up it will be used, otherwise where possible
these will be a no-op.
"""

from bvtlib.settings import MONGODB_HOST
from bvtlib.mongodb import get_autotest

def clear_test_failure(dut):
    """Clear test failure on a dut"""
    if MONGODB_HOST is None:
        return
    get_autotest().duts.update({'name':dut}, {'$unset': {'test_failed':1}})
