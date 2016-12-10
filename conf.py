import xml.etree.ElementTree as ET

class PathConfig:
    'Configuration Class for File Paths'

    filePaths=[]

    def SetPath(self):
        tree = ET.parse('configuration.xml')
        root = tree.getroot()
        for path in root:
            PathConfig.filePaths.append(path.get('value'))
           # print(path.get('value'))


    def getPath(self):
        return PathConfig.filePaths


