from automate import Automate

Paths=[]
Files=[]
Auto = Automate()
Paths=Auto.Init()

Files=Auto.GetFiles(Paths)

print (Files)