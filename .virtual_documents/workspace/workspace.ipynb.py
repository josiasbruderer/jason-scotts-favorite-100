#get_ipython().getoutput("/usr/bin/env python3")
# -*- coding: utf-8 -*-

# load the necessary libraries

import sys
from pathlib import Path
import textacy
import spacy
import codecs

project_path = Path.cwd().parent

# prepare to load project specific libraries
module_path = str(project_path / "py/")
if module_path not in sys.path:
    sys.path.append(module_path)

# import data_wrangler module
from modules import data_wrangler


data_url = "http://archives.textfiles.com/100.zip"
data_name = "100"
data_dir = str(project_path / "data/")
tmp_dir = str(project_path / ".tmp/")

dw = data_wrangler.DataWrangler(tmp_dir, data_dir)

dw.process_zip(data_url, data_name)


def get_texts(dir_texts):
    """
    Sequentially stream all documents from a given folder,
    including metadata.
    """
    p = Path(dir_texts) # set base dir
    
    # iterate over all documents
    for fname in p.glob('**/*'): # ** = all subdirectories
             
            
        
        content = codecs.open(fname, 'r', encoding='utf-8', errors='replace').read()

        #content = next(textacy.io.text.read_text(fname, encoding="utf-8"))
        # join lines as there are hard line-breaks
        # content = content.replace('\n', ' ')
        # further modify the text content here if needed

        # parse year from filename and set a metadata
        # example: 1920_parteiprogramm_d.txt --> year=1920
        #try:
        #    year = int(fname.name.split('_')[0])
        #except ValueError:
        #    print('WARNING: Parsing meta data failed:', fname.name)
        #    continue

        # add more metadata here if needed
        metadata = {'name': fname.name, 'length': len(content)}
        
        # return documents one after another (sequentially)
        yield (metadata, content)
        
texts = get_texts(data_dir + "/" + data_name)

f = open("top100_generated.csv", "w+")

for item in texts:
    f.write(item[0]["name"]+","+str(item[0]["length"])+"\r\n")

f.close()






