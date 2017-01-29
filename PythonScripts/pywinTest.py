from pywinauto.application import Application
app = Application().start("notepad.exe")
app.UntitledNotepad.TypeKeys("%FadfojhuaifhasidfhsiudX")
app.UntitledNotepad.MenuSelect("File->SaveAs")
app.SaveAs.ComboBox5.Select("UTF-8")
app.SaveAs.edit1.SetText("Example-utf8.txt")
app.SaveAs.Save.Click()
