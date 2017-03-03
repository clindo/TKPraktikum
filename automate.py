from conf import Config
import os
import shutil
from logger import log


class Automate:
    #Initialization Class for Automation
    log = log()

    def Init(self):
        __configuration__ = Config()
        status = __configuration__.read_config()
        if status == 0:
            return 0
        return 1

    def GetFiles(self, paths):
        files = []
        for file in os.listdir(paths):
            files.append(file)
        return files

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

