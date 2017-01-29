from automate import Automate
from BussinessLogic import business_logic
from conf import Config
from logger import log
import sys

#Globals
Files=[]

log = log()
Auto = Automate()
#Initializes from the configuration file
log.logger.info('Initialization called')
status = Auto.Init()
if status == 0:
    log.logger.error('Initialization failed.Exiting application')


Path = Config()
#Copy the files from src path to dest path inorder to create a backup
status = Auto.copyFiles(Path.Original_Path,Path.Moved_Path)

if status == 0:
    log.logger.error('Copying files failed. Exiting Application')
    sys.exit(0)
else:
    log.logger.info('File copy successfull')

#Get the files from the dest folder to start the conversion process
Files=Auto.GetFiles(Path.Moved_Path)
bi = business_logic()
for file in Files:
    bi.convert_files(file)
