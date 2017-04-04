from automate import Automate
from BussinessLogic import business_logic
from conf import Config
from logger import log
import sys
import os, time


log = log()
Auto = Automate()
log.logger.info('Automate initialized')

before = dict([(f, None) for f in os.listdir(Auto.__configuration__.Original_Path)])
while 1:
    time.sleep (10)
    after = dict ([(f, None) for f in os.listdir (Auto.__configuration__.Original_Path)])
    added = [f for f in after if not f in before]

    if added:
        print "Added: ", ", ".join (added)
        bi = business_logic()
        for file in added:
            file_name = bi.convert_files(file)
            print "Rendering Succesfull!!"
            print "Start renaming to index.html"
            backslash = "\\"
            x = Auto.__configuration__.Saved_Path+backslash+file_name
            y = file_name+".html"
            Auto.renameFile(x,y)

    before = after
