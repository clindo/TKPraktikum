from automate import Automate


Files=[]
Auto = Automate()
Paths=Auto.Init()

#Files=Auto.GetFiles(Paths)
#print (Files)

Auto.copyFiles(Paths)