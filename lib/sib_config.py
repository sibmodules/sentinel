import sys
import os
import io
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from misc import printdbg
from dash_config import DashConfig


class SibcoinConfig(DashConfig):

    @classmethod
    def get_rpc_creds(self, data, network='mainnet'):
        # get rpc info from dash.conf
        match = re.findall(r'rpc(user|password|port)=(.*?)$', data, re.MULTILINE)

        # python >= 2.7
        creds = {key: value for (key, value) in match}

        # standard Dash defaults...
        default_port = 1944 if (network == 'mainnet') else 11944

        # use default port for network if not specified in dash.conf
        if not ('port' in creds):
            creds[u'port'] = default_port

        # convert to an int if taken from dash.conf
        creds[u'port'] = int(creds[u'port'])

        # return a dictionary with RPC credential key, value pairs
        return creds

