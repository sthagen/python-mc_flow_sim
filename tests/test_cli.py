# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import mc_flow_sim.cli as cli


def test_main_ok_empty_list(capsys):
    seq = []
    assert cli.main(seq) is None
    out, err = capsys.readouterr()
    assert out.strip() == str(None)


def test_main_ok_string(capsys):
    string = "abc"
    assert cli.main(string) is None
    out, err = capsys.readouterr()
    assert out.strip() in string


def test_main_ok_string_list(capsys):
    the_same = "a"
    seq = [the_same, the_same, the_same]
    assert cli.main(seq) is None
    out, err = capsys.readouterr()
    assert out.strip() == the_same
