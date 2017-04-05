from automate import Automate
from BussinessLogic import business_logic
from conf import Config
from logger import log
import sys
import os, time

#Initialization
log = log()
Auto = Automate()
log.logger.info('Automate initialized')
bi = business_logic()

#Get the files already present in the watch directory
before = dict([(f, None) for f in os.listdir(Auto.__configuration__.Original_Path)])
log.logger.info("Files aready existing:")
while 1:
    #Check new added files after every 10 seconds
    time.sleep (10)
    #Get the new added trek files
    after = dict ([(f, None) for f in os.listdir (Auto.__configuration__.Original_Path)])
    added = [f for f in after if not f in before]

    if added:
        print "Added: ", ", ".join (added)
        #log.logger.info("Files added:",",".join(added))
        for file in added:
            rendered_file_name = bi.convert_files(file)
            if rendered_file_name :
                log.logger.info('Rendering Successful')
            #print "Rendering Succesfull!!"
            #print "Start renaming to index.html"
            backslash = "\\"
            full_path_of_rendered_file = Auto.__configuration__.Saved_Path+backslash+rendered_file_name
            rendered_html_file = rendered_file_name+".html"
            Auto.renameFile(full_path_of_rendered_file,rendered_html_file)
            log.logger.info("Renaming Successful!")

    before = after
