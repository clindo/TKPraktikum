from conf import Config
from pywinauto.application import Application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
from pywinauto.findbestmatch import MatchError
from logger import log
from helper import Automate
import time
import os
import datetime
import time
import sys

class render_video:

    def convert_files(self,file):
        _config = Config()
        backslash = "\\"
        app_path = _config.Original_Path+backslash+file
        #print(app_path)
        Auto=Automate()
        renderTime=Auto.renderTime(app_path,_config.Rendering_wait_time)
        IsFileCopied=Auto.IsCopyFinished(app_path)
        if IsFileCopied ==0:
            return
        if os.path.exists(app_path):
            os.startfile(app_path)
        else:
            log.logger.info("Trek file does not exists")
            return
        time.sleep(_config.App_time)
        print("Sleep End!!!")
        #app = Application().connect(path=r"C:\Program Files\TechSmith\Camtasia 9\CamtasiaStudio.exe")

        try:
            if os.path.exists(_config.Camtasia_Path):
                app = Application().connect(path=_config.Camtasia_Path)
            else:
                log.logger.info("Camtasia executable not found!")
                return

            # Access app's window object
            app_dialog = app.top_window_()
            app_dialog.Minimize()
            app_dialog.Restore()
            #app_dialog.SetFocus()
        except(WindowNotFoundError):
            print ' not found Camtasia'
            pass
        except(WindowAmbiguousError):
            print 'There are too many Camtasia windows found'
            pass

        if os.path.exists(app_path):
            os.startfile(app_path)
        else:
            log.logger.info("Trek file does not exists... Exiting App")
            app.kill()
            return

        #for TRIAL
        if _config.Trial == 'YES':
            #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').SetFocus()
            try:
                app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
            except(MatchError):
                print ' Not found Finish Dialog'
                log.logger.info("Not found Finish Dialog... Exiting App")
                app.kill()
                return
            # except(WindowAmbiguousError):
            #     print 'Too many Finish Dialog'
            #     log.logger.info("Too many Finish Dialog... Exiting App")
            #     return

        time.sleep(_config.Dialog_wait_time)
        #end for TRIAL
        child_elements = app[_config.App_Name]
        #remark
        child_elements.ClickInput(coords=(_config.Share_Btn_X, _config.Share_Btn_Y))
        child_elements.TypeKeys("{DOWN}")
        child_elements.TypeKeys("{ENTER}")
        time.sleep(_config.Dialog_wait_time)

        #for TRIAL
        if _config.Trial == 'YES':
            child_elements.Wait('visible',timeout=20)
            child_elements.ClickInput(coords=(_config.Water_Mark_Btn_X, _config.Water_Mark_Btn_Y))
            time.sleep(_config.Dialog_wait_time)
        #end for TRIAL
        for i in range(_config.Dialogs):
        #for no_dialogs in _config.Dialogs:
            time.sleep(2)
            child_elements.Wait('visible',timeout=20)

            try:
                app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
            except(MatchError):
                print ' Not found Dialog to click the first Next. Check if coordinates are mentioned correctly in configuration.xml'
                log.logger.info("Not found Dialog to click the first Next. Check if coordinates are mentioned correctly in configuration.xml. Exiting App")
                app.kill()
                return


        #app.Window_(best_match='Dialog', top_level_only=True).PrintControlIdentifiers()
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(time.time())
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(file)
        stripped_file_name = os.path.splitext(os.path.basename(file))[0]
        dup_dir = Auto.check_duplicate(stripped_file_name,_config.Saved_Path);
        if dup_dir == 1:
            log.logger.info("Duplicate exists.The rendering will overwrite the existing directory")

        try:
            app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(stripped_file_name)
        except(MatchError):
            print ' Not found Dialog to rename the project'
            log.logger.info("Not found Dialog to rename the project... Exiting App")
            app.kill()
            return
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="C:\\Users\\sachinbm\\Documents\\Camtasia Studio",class_name="Edit").SetText("E:\\testcamtasia")
        try:
            app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
        except(MatchError):
            print ' Not found Dialog to click Finish'
            log.logger.info("Not found Dialog to click Finish... Exiting App")
            app.kill()
            return

        time.sleep(renderTime)
        #child_elements.Wait('visible',timeout=20)
        app.kill_()
        time.sleep(_config.Dialog_wait_time)
        #print("Rendering Succcessful")

        return stripped_file_name
        #Finish rendering
