#!/usr/bin/env python2
import smolder
from nose.tools import raises

def test_set_port_and_protocol_overide_protocol_from_testfile():
    test = {'protocol': 'ftp'}
    smolder.set_port_and_protocol('http://f.com:321', test)
    assert test['protocol'] == 'ftp'

def test_set_port_and_protocol_overide_protocol_from_host():
    test = {}
    smolder.set_port_and_protocol('ssh://f.com:321', test)
    assert test['protocol'] == 'ssh'

def test_set_port_and_protocol_overide_port_from_testfile():
    test = {'port': 123}
    smolder.set_port_and_protocol('http://f.com:321', test)
    assert test['port'] == 123

def test_set_port_and_protocol_overide_port_from_host():
    test = {}
    smolder.set_port_and_protocol('http://f.com:321', test)
    assert test['port'] == 321

def test_set_port_and_protocol_defaults():
    test = {}
    smolder.set_port_and_protocol('', test)
    assert test['port'] == 80
    assert test['protocol'] == 'http'
