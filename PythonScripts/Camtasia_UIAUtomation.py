#This file contains the basic workflow of Camtasia UI Automation

from helper import Automate
from Render_video import render_video
from conf import Config
from logger import log
import sys
import os, time

#Initialization
#Creates an instane of logger class.
log = log()

#Creates an instane of Automate class.
#which contains the helper functions.
Auto = Automate()
#Reads the configuration.xml to get configuration parameters
Auto.readConfig()

log.logger.info('Automate initialized')
#Creates an instance of render_video class.
#Which is done by pywinauto library
bi = render_video()

#Get the files already present in the watch directory
if os.path.exists(Auto.__configuration__.Original_Path):
    before = dict([(f, None) for f in os.listdir(Auto.__configuration__.Original_Path)])
    log.logger.info("Already existing files:")
    log.logger.info(before)
else:
    log.logger.error("-------> Trec file path is invalid. Recheck the configuration.xml, and RESTART THE APP ----->")
    sys.exit() #Exits the automation app if configuration is not correct

#Infinite loop to watch file changes in the WatchFolder
while 1:

    fileNames = []
    #Checking wether files currently present are already rendered successfully.
    with open("SuccessfullyRenderedFiles.txt") as file:
        for line in file:
            line = line.strip()
            fileNames.append(line)
    differenceList= list(set(before.keys())-set(fileNames))
    differenceJSON =dict([(f, None) for f in differenceList])


    #Check new added files after Polling_time
    time.sleep (Auto.__configuration__.Polling_time)
    #Get the new added trec files
    if os.path.exists(Auto.__configuration__.Original_Path):
        after = dict ([(f, None) for f in os.listdir (Auto.__configuration__.Original_Path)])
        added = [f for f in after if not f in before]
        added+=differenceJSON
        # print  " addedJSON"+added
    else:
        log.logger.info("Trec file path does not exists!")
        sys.exit()

    if added:
        log.logger.info("Files added:")
        log.logger.info(added)
        for file in added:
            log.logger.info(file)
            rendered_file_name = bi.convert_files(file)
            if rendered_file_name :
                log.logger.info('Rendering Successful')
                backslash = "\\"
                full_path_of_rendered_file = Auto.__configuration__.Saved_Path+backslash+rendered_file_name
                rendered_html_file = rendered_file_name+".html"

                if os.path.exists(full_path_of_rendered_file):
                    status = Auto.renameFile(full_path_of_rendered_file,rendered_html_file)
                    #If the file is renamed successfully, then we are adding it to the SuccessfullyRenderedFiles.txt
                    if status == 1:
                        renderedFileList= open("SuccessfullyRenderedFiles.txt","a+")
                        # print rendered_file_name
                        renderedFileList.write("%s.trec\n" % rendered_file_name)
                        renderedFileList.close()
                        log.logger.info("Renaming Successful!")
                    else:
                        log.logger.info("Renaming not Successful!")
                else:
                    log.logger.info("Rendered file does not exists!")
                    sys.exit()
            else:
                log.logger.info('Rendering not successful')

    before = after
