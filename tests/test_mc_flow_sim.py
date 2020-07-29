# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import mc_flow_sim.mc_flow_sim as mc


def test_walk_ok_empty_string(capsys):
    empty = ''
    assert mc.walk(empty) is None
    out, err = capsys.readouterr()
    assert out.strip() == empty


def test_walk_ok_empty_list():
    seq = []
    assert mc.walk(seq) is None
