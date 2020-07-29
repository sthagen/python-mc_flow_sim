# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import mc_flow_sim.cli as cli


def test_main_ok_string():
    cli.main("abc")

def test_main_ok_string_list(capsys):
    the_same = "a"
    seq = [the_same, the_same, the_same]
    cli.main(seq)
    out, err = capsys.readouterr()
    assert out == the_same
