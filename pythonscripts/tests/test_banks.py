import sys
sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/banksandbranches')
from banksandbranchesroute import banks_generator_api
from banksandbranchesroute import branch_generator_api


def test_banks_api():
    resp = banks_generator_api()
    assert resp.status_code==201

def test_branch_api():
    resp = branch_generator_api()
    assert resp.status_code==201