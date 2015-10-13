#!/usr/bin/env python
from urlparse import urlparse

# This will mutate test. Use only if you know what you are doing.
def set_port_and_protocol(host, test):
    uri = urlparse(host)
    test['port'] = test.get('port', uri.port) or 80
    test['protocol'] = test.get('protocol', uri.scheme) or 'http'
