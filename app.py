from automate import Automate
from BussinessLogic import business_logic
Files1=[]
Files2=[]
Auto = Automate()
Paths=Auto.Init()

Files1=Auto.GetFiles(Paths[0])
print (Paths[0])
print (Files1)

#Auto.copyFiles(Paths)

Files2=Auto.GetFiles(Paths[1])
print (Paths[1])
print (Files2)

bi = business_logic()
bi.convert_files(Files2[0])