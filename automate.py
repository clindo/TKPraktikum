from conf import PathConfig
import os


class Automate:
    'Initialization Class for Automation'

    files = []

    def Init(self):
        Path = PathConfig( );
        FolderPaths = []
        Path.SetPath( );
        FolderPaths = Path.getPath( );
        return FolderPaths
        # print (FolderPaths)

    def GetFiles(self, paths):
        for file in os.listdir( paths[0] ):
            Automate.files.append( file )
        return Automate.files
