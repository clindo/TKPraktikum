import xml.etree.ElementTree as ET

class Config:
    'Configuration Class for File Paths'
    Original_Path = ""
    Moved_Path = ""
    Dialogs = 0
    Trial = ""
    Share_Btn_X = 0
    Share_Btn_Y = 0
    Water_Mark_Btn_X = 0
    Water_Mark_Btn_Y = 0

    #def __init__(self):
    #    self.Original_Path = ''
    #    self.Moved_Path = ''

    def read_config(self):
        tree = ET.parse('configuration.xml')
        root = tree.getroot()
        #Get the folder path where the files are present
        path = root.find('Path')
        #PathConfig.filePaths.append(path.get('path1'))
        Config.Original_Path = path.get('path1')
        #Get the folder path where files are to be moved
        move_path = root.find('MovePath')
        Config.Moved_Path = move_path.get('path2')
        #Get the no. of dialogs screens during coversion
        no_screens = root.find('No_Screens')
        Config.Dialogs = no_screens.get('dialog')
        Config.Dialogs = int(Config.Dialogs)
        #Get if Camtasia has Trial license
        trial = root.find('TRIAL')
        Config.Trial = trial.get('trial')
        #Get the co-ordinates of the share button
        share_btn = root.find('Share_BTN_COOR')
        Config.Share_Btn_X = share_btn.get('x')
        Config.Share_Btn_X = int(Config.Share_Btn_X)
        Config.Share_Btn_Y = share_btn.get('y')
        Config.Share_Btn_Y = int(Config.Share_Btn_Y)
        #Get the co-ordinates Watermark
        watermark_btn = root.find('WATER_MARK_COOR')
        Config.Water_Mark_Btn_X = watermark_btn.get('x')
        Config.Water_Mark_Btn_X = int(Config.Water_Mark_Btn_X)
        Config.Water_Mark_Btn_Y = watermark_btn.get('y')
        Config.Water_Mark_Btn_Y = int(Config.Water_Mark_Btn_Y)



    def get_Moved_Path(self):
        return Config.Moved_Path

    def get_Original_Path(self):
        return Config.Original_Path

