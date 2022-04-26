import sys
sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/userdata')
from userdataroute import create_admin_api
from userdataroute import create_member_api

def test_userdata_admin_api():
    resp = create_admin_api()
    assert resp.status_code==201

def test_userdata_member_api():
    resp = create_member_api()
    assert resp.status_code==201