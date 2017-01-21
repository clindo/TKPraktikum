import xml.etree.ElementTree as ET

class PathConfig:
    'Configuration Class for File Paths'
    Original_Path = ""
    Moved_Path = ""

    #def __init__(self):
    #    self.Original_Path = ''
    #    self.Moved_Path = ''

    def SetPath(self):
        tree = ET.parse('configuration.xml')
        root = tree.getroot()
        #Get the folder path where the files are present
        path = root.find('Path')
        #PathConfig.filePaths.append(path.get('path1'))
        PathConfig.Original_Path = path.get('path1')
        #Get the folder path where files are to be moved
        move_path = root.find('MovePath')
        PathConfig.Moved_Path = move_path.get('path2')
        #PathConfig.filePaths.append(move_path.get('path2'))


        #for path in root:
            #PathConfig.filePaths.append(path.get('path1'))
            #PathConfig.filePaths.append(path.get('path2'))
            #print(path.get('path'))



    def get_Moved_Path(self):
        return PathConfig.Moved_Path

    def get_Original_Path(self):
        return PathConfig.Original_Path

