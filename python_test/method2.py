# from test1.method_one import add
# # import sys
# # sys.path.append('/root/workspace/python_test/test1')
# print(add(1,2))

from paramiko import SSHClient, AutoAddPolicy
from tools.gateway_connection_diags import *
from lib.palmetto.cli import Palmctl
from lib.palmetto.cli import Palmops
import os
import json

import paramiko
import sys
import time
import json
import yaml
import argparse
import pprint
import re
from base64 import b64decode

# CLIs initialization
sys.path.append(f'{os.path.dirname(__file__)}/..')
palmctl = Palmctl(is_verbose=False)
palmops = Palmops(is_verbose=False)

gw_ip_dict={}
request = palmctl.get(resource="gateways")
gateways = request['gateways']
for gateway in gateways:
    # print("\""+gateway['name']+"\" ip is \""+gateway['public_ip']+"\"")
    gw_ip_dict[gateway['name']] = gateway['public_ip']

print(gw_ip_dict)