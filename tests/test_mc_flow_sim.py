# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import mc_flow_sim.mc_flow_sim as mc


def test_walk_ok_empty_string():
    empty = ''
    assert mc.walk(empty) is None


def test_walk_ok_empty_list():
    seq = []
    assert mc.walk(seq) is None


def test_walk_ok_empty_set():
    seq = {}
    assert mc.walk(seq) is None


def test_walk_ok_empty_dict():
    seq = dict()
    assert mc.walk(seq) is None


def test_walk_ok_empty_tuple():
    seq = tuple()
    assert mc.walk(seq) is None


def test_walk_ok_string():
    string = "abc"
    step = mc.walk(string)
    assert len(step) == 1
    assert step in string


def test_walk_ok_string_list():
    the_same = "a"
    seq = [the_same, the_same, the_same]
    assert mc.walk(seq) == the_same


def test_walk_ok_range():
    a_range = range(42)
    step = mc.walk(a_range)
    assert step in a_range
    assert isinstance(step, int)


def test_walk_ok_int_dict():
    seq = {0: "a", 1: "b"}
    assert mc.walk(seq) in seq.values()


def test_walk_nok_string_dict():
    seq = {"a": "b"}
    message = r"0"
    with pytest.raises(KeyError, match=message):
        mc.walk(seq)


def test_walk_nok_wrong_type_none():
    bad = None
    assert mc.walk(bad) is None


def test_walk_nok_wrong_type_object():
    bad = object
    message = r"object of type 'type' has no len\(\)"
    with pytest.raises(TypeError, match=message):
        mc.walk(bad)


def test_walk_nok_wrong_type_int():
    bad = 42
    message = r"object of type 'int' has no len\(\)"
    with pytest.raises(TypeError, match=message):
        mc.walk(bad)


def test_walk_nok_wrong_type_generator_expression():
    message = r"object of type 'generator' has no len\(\)"
    with pytest.raises(TypeError, match=message):
        mc.walk(n for n in range(1234))
