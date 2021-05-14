#get_ipython().getoutput("/usr/bin/env python3")
# -*- coding: utf-8 -*-

# load the necessary libraries

import sys
from pathlib import Path

# prepare to load project specific libraries
module_path = str(Path.cwd() / "py")
if module_path not in sys.path:
    sys.path.append(module_path)

# import data_wrangler module
from modules import data_wrangler


data_url = "http://archives.textfiles.com/100.zip"
data_dir = sys.path[0] + "/data/"
tmp_dir = sys.path[0] + "/.tmp/"

dw = data_wrangler.DataWrangler(tmp_dir, data_dir)

dw.process_zip(data_url, "100")
