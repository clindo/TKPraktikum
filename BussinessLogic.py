from conf import PathConfig
from pywinauto.application import Application
import autoit
import time
import os
import datetime
import time

class business_logic:

    def convert_files(self,file):
        Path = PathConfig( )
        #app = application.Application()
        backslash = "\\"
        FolderPaths = Path.getPath()
        print(FolderPaths[1])
        print(file)
        app_path = FolderPaths[1]+backslash+file
        print(app_path)
        os.startfile(app_path)
        time.sleep(100)
        print("Sleep End!!!")
        app = Application().connect(path=r"C:\Program Files\TechSmith\Camtasia 9\CamtasiaStudio.exe")
        #for TRIAL
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
        #end for TRIAL
        hwndwrappercamtasiastudioexebbedcaecbaeffaf = app[u'Camtasia 9']

        hwndwrappercamtasiastudioexebbedcaecbaeffaf.ClickInput(coords=(200, 20))
        hwndwrappercamtasiastudioexebbedcaecbaeffaf.TypeKeys("{DOWN}")
        hwndwrappercamtasiastudioexebbedcaecbaeffaf.TypeKeys("{ENTER}")
        time.sleep(10)
        print("Sleep End!!!")
        #for TRIAL
        hwndwrappercamtasiastudioexebbedcaecbaeffaf.ClickInput(coords=(400, 600))
        #end for TRIAL
        time.sleep(2)
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
        time.sleep(2)
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
        time.sleep(2)
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
        time.sleep(2)
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
        time.sleep(2)
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
        #app.Window_(best_match='Dialog', top_level_only=True).PrintControlIdentifiers()
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(title="Untitled Project",class_name="Edit").SetText(time.time())
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
        app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Finish').Click()
       # static.SetWindowText("sachin")
        #print(datetime.datetime.now())
        #print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Next').Click()
        #app = Application().connect(path=r"C:\Program Files\TechSmith\Camtasia 9\CamtasiaStudio.exe")
        #hwndwrappercamtasiastudioexebcfebfcbbefbad  = app[u'Camtasia 9']
        #hwndwrappercamtasiastudioexebcfebfcbbefbad.Minimize()
        #app.Window_(title='Camtasia 9').MenuSelect('File')
        #app.CamtasiaStudio.draw_outline()
        #app['Camtasia 9'].menu_select("Share")
        #xyz = app.CamtasiaStudio.Menu_select("Help->About Camtasia")
        #app.Share.print_control_identifiers()
        #app.PopupMenu.Menu().get_menu_path("Cancel")[0].click()
        #app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='Cancel').Click()
        #os.startfile(app_path)
        #autoit.run("E:\sample\TK Praktikum1.trec")
        #autoit.win_wait_active("[CLASS:Notepad]", 3)
        #autoit.win_close("[CLASS:Notepad]")
        #autoit.control_click("[Class:#32770]", "Button2")
