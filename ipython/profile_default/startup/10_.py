#!/usr/bin/env python3
# @file: 10_.py
# @date: 2023-03-26T21:14:50
# @author: Aroldo Souza-Leite
# @description: 
"""
Startup script for Ipython.
"""
import os, sys
from pathlib import Path
from IPython import get_ipython


######## magic commands ######
magic = get_ipython().run_line_magic
magic("reload_ext", "autoreload")
magic("autoreload", "2")

