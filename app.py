from automate import Automate
from BussinessLogic import business_logic
from conf import PathConfig
from MACROS import MACROS
Files=[]

Auto = Automate()
#Initializes from the configuration file
Auto.Init()

Path = PathConfig( )
#Get the folder paths to copy from src to dest
#src_folder = Path.get_Original_Path()
#dest_folder = Path.get_Moved_Path()
Auto.copyFiles(Path.Original_Path,Path.Moved_Path)

#Get the files from the dest folder to start the conversion process
Files=Auto.GetFiles(Path.Moved_Path)

for file in Files:
    bi = business_logic()
    bi.convert_files(file)
