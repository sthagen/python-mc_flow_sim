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


def test_walk_ok_string():
    string = "abc"
    assert mc.walk(string) in string


def test_walk_ok_string_list():
    the_same = "a"
    seq = [the_same, the_same, the_same]
    assert mc.walk(seq) == the_same
