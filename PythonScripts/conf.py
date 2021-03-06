#This file is for reading the configuration.xml

import xml.etree.ElementTree as ET
from logger import log

class Config:
    'Configuration Class for File Paths'
    Original_Path = ""
    Camtasia_Path = ""
    App_Name = ""
    Saved_Path = ""
    Dialogs = 0
    Trial = ""
    Share_Btn_X = 0
    Share_Btn_Y = 0
    Water_Mark_Btn_X = 0
    Water_Mark_Btn_Y = 0
    App_time = 0
    Dialog_wait_time = 0
    Rendering_wait_time = 0
    Polling_time = 0
    log = log()

    #Function to read the configuration.xml
    def read_config(self):
        log.logger.info('Reading configuration file')
        tree = ET.parse('configuration.xml')
        root = tree.getroot()
        #Get the folder path where the files are present
        path = root.find('WatchFolder')
        if path == "":
            log.logger.info('Failed to read the file path attribute')
            return 0

        Config.Original_Path = path.get('path1')
        if Config.Original_Path == "":
            log.logger.info('Failed to read the file path')
            return 0

        #Get the folder path where files are to be moved
        camtasia_path = root.find('CamtasiaPath')
        if camtasia_path == "":
            log.logger.info('Failed to read the Camtasia file path attribute')
            return 0

        Config.Camtasia_Path = camtasia_path.get('path2')
        if Config.Camtasia_Path == "":
            log.logger.info('Failed to read the Camtasia file path')
            return 0

        app_name = root.find('APP_NAME')
        if app_name == "":
            log.logger.info('Failed to read the App name attribute')
            return 0

        Config.App_Name = app_name.get('app_name')
        if Config.App_Name == "":
            log.logger.info('Failed to read App name')
            return 0

        #Get the folder path where files are to be saved after rendering
        saved_path = root.find('SAVING_PATH')
        if saved_path == "":
            log.logger.info('Failed to read the saved file path attribute')
            return 0

        Config.Saved_Path = saved_path.get('path3')
        if Config.Saved_Path == "":
            log.logger.info('Failed to read the saving path')
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
        #Get the sleep time for Camtasia app to start
        app_time = root.find('APP_START_TIME')
        Config.App_time = app_time.get('time')
        Config.App_time = int(Config.App_time)

        #Get the wait time for Dialog box
        dialog_wait_time = root.find('DIALOG_WAIT_TIME')
        Config.Dialog_wait_time = dialog_wait_time.get('time2')
        Config.Dialog_wait_time = float(Config.Dialog_wait_time)


        #Get the rendering wait time
        rendering_wait_time = root.find('REND_WAIT_TIME')
        Config.Rendering_wait_time = rendering_wait_time.get('time3')
        Config.Rendering_wait_time = float(Config.Rendering_wait_time)

        #Get the watch folder polling time
        polling_time = root.find('POLLING_TIME')
        Config.Polling_time = polling_time.get('time4')
        Config.Polling_time = int(Config.Polling_time)
        return 1



    def get_Moved_Path(self):
        return Config.Moved_Path

    def get_Original_Path(self):
        return Config.Original_Path

