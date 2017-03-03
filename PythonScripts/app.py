from automate import Automate
from BussinessLogic import business_logic
from conf import Config
from logger import log
import sys
import os, time


log = log()
Auto = Automate()
path_to_watch = "E:/testserver"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
    time.sleep (10)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print "Added: ", ", ".join (added)
    #if removed: print "Removed: ", ", ".join (removed)
    #before = after
    #Globals
        Files=[]
        #Initializes from the configuration file
        log.logger.info('Initialization called')
        status = Auto.Init()
        if status == 0:
            log.logger.error('Initialization failed.Exiting application')


        Path = Config()
        #Copy the files from src path to dest path inorder to create a backup
        status = Auto.copyFiles(Path.Original_Path,Path.Moved_Path,added)

        if status == 0:
            log.logger.error('Copying files failed. Exiting Application')
            sys.exit(0)
        else:
            log.logger.info('File copy successfull')

        #Get the files from the dest folder to start the conversion process
        Files=Auto.GetFiles(Path.Moved_Path)
        bi = business_logic()
        for file in Files:
            status = bi.convert_files(file)
            if status == 1:
                print "Rendering Succesfull!!"

    before = after
