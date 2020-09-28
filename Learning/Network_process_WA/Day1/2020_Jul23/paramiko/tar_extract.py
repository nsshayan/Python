#!/usr/bin/env python
from tarfile import TarFile
from sys import stdin
tar = TarFile(fileobj=stdin, mode="r")
tar.extractall()
