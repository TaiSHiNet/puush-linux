#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "puush",
  version = "1.0",
  packages = [],
  scripts = ["scripts/puush"],
  install_requires = ["docopt", "requests", "notify2"],
  author = "Felix \"KoffeinFlummi\" Wiegand",
  author_email = "koffeinflummi@gmail.com",
  description = "Python implementation of puush. For Linux.",
  long_description = read("README.md"),
  license = "MIT",
  keywords = "screenshot cloud images image",
  url = "https://github.com/KoffeinFlummi/puush-linux",
  classifiers=[
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
    "Topic :: Utilities"
  ]
)
