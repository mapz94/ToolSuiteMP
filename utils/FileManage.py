import win32ui
import os

def OpenDialog(fileType = "",extension = ""):
    #print("For testing, this will only display PDF Files!")
    o = win32ui.CreateFileDialog( 1, fileType, None, 0,fileType +  " Files (*" + extension + ")|*"+ extension + "|All Files (*.*)|*.*|")
    o.DoModal()
    #print (self.o.GetPathName())
    return o.GetPathName()
    