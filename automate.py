from conf import PathConfig
import os
import shutil


class Automate:
    'Initialization Class for Automation'


    def Init(self):
        Path = PathConfig( )
        Path.SetPath()

    def GetFiles(self, paths):
        files = []
        for file in os.listdir( paths ):
            files.append( file )
        return files

    def copyFiles(self, src_folder,dest_folder):
        for file in os.listdir( src_folder ):
            print ("File being moved -----> " + file)
            full_file_name = os.path.join( src_folder, file )
            if os.path.isfile(full_file_name):
                shutil.move( full_file_name, dest_folder )
