#!/usr/bin/env python3

from tempfile import NamedTemporaryFile
from urllib.request import urlopen
import tarfile

theme_url = 'https://github.com/MaTachi/norrmalm/releases/download/v0.1/norrmalm.tar.gz'
response = urlopen(theme_url).read()
tmp_file = NamedTemporaryFile()
tmp_file.write(response)
tar = tarfile.open(tmp_file.name)
tar.extractall('themes/norrmalm')
tar.close()
