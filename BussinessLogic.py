from conf import PathConfig
import os

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
        #autoit.run("E:\sample\TK Praktikum1.trec")
        #autoit.win_wait_active("[CLASS:Notepad]", 3)
        #autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
        #autoit.win_close("[CLASS:Notepad]")
        #autoit.control_click("[Class:#32770]", "Button2")
