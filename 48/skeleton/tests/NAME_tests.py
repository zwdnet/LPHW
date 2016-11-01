# -*- coding:utf-8 -*-
from nose.tools import *
from NAME.ex48 import lexicon

def test_directions():
    l = lexicon()
    assert_equal(l.scan("north"), [('direction', 'north')])
    result = l.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    l = lexicon()
    assert_equal(l.scan("go"), [('verb', 'go')])
    result = l.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    l = lexicon()
    assert_equal(l.scan("the"), [('stop', 'the')])
    result = l.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    l = lexicon()
    assert_equal(l.scan("bear"), [('noun', 'bear')])
    result = l.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    l = lexicon()
    assert_equal(l.scan("1234"), [('number', 1234)])
    result = l.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    l = lexicon()
    assert_equal(l.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = l.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])