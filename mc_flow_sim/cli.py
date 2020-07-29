se#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import os
import sys

from mc_flow_sim.mc_flow_sim import walk

DEBUG = os.getenv("MC_FLOW_SIM_DEBUG")


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process ... TODO."""
    argv = sys.argv[1:] if argv is None else argv
    verbose = True if "-v" in argv or "--verbose" in argv else False
    verbose and print(f"No verbose mode implemented")
    print(walk(argv))
