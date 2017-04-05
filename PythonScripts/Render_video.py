from conf import Config
from pywinauto.application import Application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
from logger import log
import time
import os
import datetime
import time

class render_video:

    def convert_files(self,file):
        _config = Config()
        backslash = "\\"
        app_path = _config.Original_Path+backslash+file
        #print(app_path)
        os.startfile(app_path)
        time.sleep(_config.App_time)
        print("Sleep End!!!")
        #app = Application().connect(path=r"C:\Program Files\TechSmith\Camtasia 9\CamtasiaStudio.exe")

        try:
            app = Application().connect(path=_config.Camtasia_Path)
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


        #for TRIAL
        if _config.Trial == 'YES':
            #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').SetFocus()
            app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
            time.sleep(_config.Dialog_wait_time)
        #end for TRIAL
        child_elements = app[u'Camtasia 9']
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
            app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()

        #app.Window_(best_match='Dialog', top_level_only=True).PrintControlIdentifiers()
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(time.time())
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(file)
        stripped_file_name = os.path.splitext(os.path.basename(file))[0]
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(stripped_file_name)
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="C:\\Users\\sachinbm\\Documents\\Camtasia Studio",class_name="Edit").SetText("E:\\testcamtasia")
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
        time.sleep(_config.Rendering_wait_time)
        #child_elements.Wait('visible',timeout=20)
        app.kill_()
        time.sleep(_config.Dialog_wait_time)
        #print("Rendering Succcessful")

        return stripped_file_name
        #Finish rendering
