
import pytest
import os

from ..decoder import *

def test_decoder():
    test_json = os.path.join(os.path.dirname(__file__), "../../../test-data/test.json")
    parsing = []
    with open(test_json) as f:
        chars = f.read()
        f.seek(0)
        for start, end, event, value in basic_parse(f):
             block = None
             if not (start is None or end is None):
                block = chars[start:end]
             comparison = (start,end,event,value,block)
             parsing.append(comparison)
    print(parsing)
