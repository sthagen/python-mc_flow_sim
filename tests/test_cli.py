# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import mc_flow_sim.cli as cli


def test_main_ok_string():
    cli.main("abc")
