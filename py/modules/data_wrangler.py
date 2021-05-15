#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################################################
### title:  datawrangler
### author: Josias Bruderer
### date:   14.05.2021
### desc:   this module takes care of all tasks that are
###         related to juggling files and datasets. 
##########################################################

import os
import sys
import requests
import zipfile

class DataWrangler:
    def __init__(self, tmp_dir, data_dir):
        self.tmp_dir = tmp_dir
        self.data_dir = data_dir
        self.init()
    
    def init(self):
        try:
            # create tmp directory if not existing yet
            if not os.path.exists(self.tmp_dir):
                os.mkdir(self.tmp_dir)
        except:
            print ("Unexpected error: ", sys.exc_info()[0])
            raise

        try:
            # create data directory if not existing yet
            if not os.path.exists(self.data_dir):
                os.mkdir(self.data_dir)
        except:
            print ("Unexpected error: ", sys.exc_info()[0])
            raise
    
    def process_zip(self, data_url, name):
        try:
            # download zip file
            r = requests.get(data_url, allow_redirects=True)
            open(self.tmp_dir + "/" + name + ".zip", 'wb').write(r.content)
        except:
            print ("Unexpected error: ", sys.exc_info()[0])
            raise

        try:
            # extract zip file to data directory
            with zipfile.ZipFile(self.tmp_dir + "/" + name + ".zip", 'r') as zip_ref:
                zip_ref.extractall(self.data_dir)
        except:
            print ("Unexpected error: ", sys.exc_info()[0])
            raise