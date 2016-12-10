from conf import PathConfig
import os
import shutil


class Automate:
    'Initialization Class for Automation'

    files = []

    def Init(self):
        Path = PathConfig( )
        FolderPaths = []
        Path.SetPath( )
        FolderPaths = Path.getPath( )
        return FolderPaths
        # print (FolderPaths)

    def GetFiles(self, paths):
        for file in os.listdir( paths[0] ):
            Automate.files.append( file )
        return Automate.files

    def copyFiles(self, paths):
        for file in os.listdir( paths[0] ):
            print ("File being moved -----> " + file)
            full_file_name = os.path.join( paths[0], file )
            if os.path.isfile(full_file_name):
                shutil.move( full_file_name, paths[1] )

                #shutil.copy( full_file_name, paths[1] )
