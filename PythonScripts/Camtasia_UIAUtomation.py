from helper import Automate
from Render_video import render_video
from conf import Config
from logger import log
import sys
import os, time

#Initialization
log = log()
Auto = Automate()
log.logger.info('Automate initialized')
bi = render_video()

#Get the files already present in the watch directory
if os.path.exists(Auto.__configuration__.Original_Path):
    before = dict([(f, None) for f in os.listdir(Auto.__configuration__.Original_Path)])
    log.logger.info("Already existing files:")
    log.logger.info(before)
else:
    log.logger.info("Trek file path is invalid.")
    sys.exit()
while 1:
    #Check new added files after every 10 seconds
    time.sleep (Auto.__configuration__.Polling_time)
    #Get the new added trek files
    if os.path.exists(Auto.__configuration__.Original_Path):
        after = dict ([(f, None) for f in os.listdir (Auto.__configuration__.Original_Path)])
        added = [f for f in after if not f in before]
    else:
        log.logger.info("Trek file path does not exists!")
        sys.exit()

    if added:
        #print "Added: ", ", ".join (added)
        log.logger.info("Files added:")
        log.logger.info(added)
        for file in added:
            log.logger.info(file)
            rendered_file_name = bi.convert_files(file)
            if rendered_file_name :
                log.logger.info('Rendering Successful')
            else:
                log.logger.info('Rendering not successful')
            backslash = "\\"
            full_path_of_rendered_file = Auto.__configuration__.Saved_Path+backslash+rendered_file_name
            rendered_html_file = rendered_file_name+".html"

            if os.path.exists(full_path_of_rendered_file):
                status = Auto.renameFile(full_path_of_rendered_file,rendered_html_file)
                if status == 1:
                    log.logger.info("Renaming Successful!")
                else:
                    log.logger.info("Renaming not Successful!")
            else:
                log.logger.info("Rendered file does not exists!")
                sys.exit()

    before = after
