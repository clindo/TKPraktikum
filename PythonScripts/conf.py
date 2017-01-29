import xml.etree.ElementTree as ET
from logger import log

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
    log = log()

    def read_config(self):
        log.logger.info('Reading configuration file')
        tree = ET.parse('configuration.xml')
        root = tree.getroot()
        #Get the folder path where the files are present
        path = root.find('Path')
        if path == "":
            log.logger.info('Failed to read the file path attribute')
            return 0

        Config.Original_Path = path.get('path1')
        if Config.Original_Path == "":
            log.logger.info('Failed to read the file path')
            return 0

        #Get the folder path where files are to be moved
        move_path = root.find('MovePath')
        if move_path == "":
            log.logger.info('Failed to read the copy file path attribute')
            return 0

        Config.Moved_Path = move_path.get('path2')
        if Config.Moved_Path == "":
            log.logger.info('Failed to read the copy file path')
            return 0

        #Get the no. of dialogs screens during coversion
        no_screens = root.find('No_Screens')
        if no_screens == "":
            log.logger.error('Failed to read the no. of dialog box attribute')
            return 0

        Config.Dialogs = no_screens.get('dialog')
        if Config.Dialogs == "":
            log.logger.error('Failed to read the no. of dialog boxes')
            return 0

        Config.Dialogs = int(Config.Dialogs)

        #Get if Camtasia has Trial license
        trial = root.find('TRIAL')
        if trial == "":
            log.logger.error('Failed to read the trial license attribute')
            return 0
        Config.Trial = trial.get('trial')
        if Config.Trial == "":
            log.logger.error('Failed to read the trial license value')
            return 0

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
        return 1



    def get_Moved_Path(self):
        return Config.Moved_Path

    def get_Original_Path(self):
        return Config.Original_Path

