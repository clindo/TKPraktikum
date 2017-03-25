from automate import Automate
from BussinessLogic import business_logic
from conf import Config
from logger import log
import sys
import os, time

log = log()
Auto = Automate()
log.logger.info('Automate initialized')

try:
    before = dict([(f, None) for f in os.listdir(Auto.__configuration__.Original_Path)])
except OSError:
    log.logger.info("Path not found : Enter a valid path in configuration.xml")


while 1:
            print "Inside while loop"
            time.sleep(5)
            try:
              after = dict([(f, None) for f in os.listdir(Auto.__configuration__.Original_Path)])
            except OSError:
                log.logger.info("Path not found : Enter a valid path in configuration.xml")

            # try:
            added = [f for f in after if not f in before]
            # except OSError:
            #     log.logger.info("Path not found : Enter a valid path in configuration.xml")


            if added:
                    print "Added: ", ", ".join(added)
                    bi = business_logic()
            for file in added:
                    try:
                        file_name = bi.convert_files(file)
                    except OSError:
                        log.logger.info("Path not found : Enter a valid path in configuration.xml")
                    print "Rendering Succesfull!!"
                    print "Start renaming to index.html"
                    backslash = "\\"
                    x = Auto.__configuration__.Saved_Path + backslash + file_name
                    y = file_name + ".html"
                    Auto.renameFile(x, y)

            before = after
