from conf import Config
import os
import shutil
from logger import log
import sys

#Initialization Class for Automation
class Automate:

    #Initialize logging
    log = log()

    #Init function, reads the configuration parameters
    def __init__(self):
        #Read configuration
        self.__configuration__ = Config()
        status = self.__configuration__.read_config()
        if status == 1:
            log.logger.info("Configuration read success")
        else:
            log.logger.info("Configuration read not successful!")
            sys.exit()

    #Helper function to get the files from a directory
    def GetFiles(self, paths):
        files = []
        for file in os.listdir(paths):
            files.append(file)
        return files

    #Helper function to copy files from a src dir to dest dir
    def copyFiles(self, src_folder,dest_folder,added):
        if src_folder == "" or dest_folder == "":
            log.logger.error('Source or Destination Folder does not exists')
            return 0

        if not os.listdir(src_folder):
            log.logger.error('No files found in src folder')
            return 0

        #for file in os.listdir(src_folder):
        for file in added:
            print ("File being moved -----> " + file)
            full_file_name = os.path.join( src_folder, file )
            if os.path.isfile(full_file_name):
                try:
                    shutil.copy( full_file_name, dest_folder )
                except shutil.Error as e:
                    log.logger.error('Could not copy the files %s',e)
                    return 0
        return 1

    #Helper function to rename the rendered trek file embedded HTML to index.html
    def renameFile(self,path,tochangefilename):
        fileName = os.listdir(path)
        for files in fileName:
            if(files == tochangefilename):
                os.rename(path+"\\"+tochangefilename, path+"\\"+"index.html")
                return 1
        return 0

    #Helper function to calculate wait time for rendering based on File Size
    def renderTime(self, file, renderingPerMB):
        st = os.stat(file)
        sizeBytes = st.st_size
        sizeBytes /= (1024 * 1024)
        renderTime = sizeBytes * renderingPerMB
        renderTime /= 1000
        return renderTime

    #Check is a duplicate exists and delete the duplicate folder
    def check_duplicate(self,filename):
        directories = os.listdir(self.__configuration__.Saved_Path)
        for dir in directories:
            if dir == filename:
                shutil.rmtree(self.__configuration__.Saved_Path+'\\'+filename)
                return 1

        return 0
