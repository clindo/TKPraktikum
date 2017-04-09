#include, Gdip.ahk 
FileReadLine, __Width, Resolution_Configuration.txt, 2
FileReadLine, __Height, Resolution_Configuration.txt, 3

f5:: 
  try{               
    ppt := ComObjActive("PowerPoint.Application")
	objppt := ppt.ActivePresentation
	TotalSlides:=% objppt.Slides.Count
	FileCreateDir, temp
  }
  catch e {
	return 
  }
  SysGet, MonitorCount, MonitorCount
  ppt := objppt.SlideShowSettings
  ppt.Run
Return

Space::
	try{
		ppt := ComObjActive("PowerPoint.Application")
		objppt := ppt.ActivePresentation
		SlideNum :=% objppt.SlideShowWindow.View.Slide.SlideIndex
	}
	catch e {
		ExitApp
	}
	saveScreenshot(SlideNum)
	objppt.SlideShowWindow.View.Next
	monitorDisplay(objppt, MonitorCount)
	return
	
v::
	try{
		ppt := ComObjActive("PowerPoint.Application")
		objppt := ppt.ActivePresentation
		objppt.SlideShowWindow.View.Previous
	}
	catch e {
		ExitApp
	}
	monitorDisplay(objppt, MonitorCount)
	return

;Select the slides and calls setDisplay
monitorDisplay(objppt, MonitorCount){
	try{
		CurrentSlideNumber :=% objppt.SlideShowWindow.View.Slide.SlideIndex
		}
	catch{
		FileRemoveDir, temp, 1
		ExitApp
		}
	monitor := MonitorCount-1
	var2 := 0
	Loop %monitor%{
		var2++
		setDisplay(var2, CurrentSlideNumber-1)
		CurrentSlideNumber--
	}
}	

;Coordinates for setting the display are returned
getCoordinates(MonitorNumber){
	SysGet, MonitorCount, MonitorCount
	SysGet, MonitorPrimary, MonitorPrimary
	Array := Object()
	Loop, %MonitorCount%
	{
		ArrayCount += 1 
		SysGet, MonitorName, MonitorName, %A_Index%
		SysGet, Monitor, Monitor, %A_Index%
		SysGet, MonitorWorkArea, MonitorWorkArea, %A_Index%
		Array.Insert(MonitorLeft)
	}
	SortArray(Array)
	if(MonitorNumber = 1)
		return Array[2]
	if(MonitorNumber = 2)
		return Array[3]
}

;Using the coordinates returned from getCoordintes
;The screenshots are set to the external displays
setDisplay(MonitorNumber, PreviousSlideNumber){
global
	coord := getCoordinates(MonitorNumber)
	SetEnv file, %A_WorkingDir%\temp\%PreviousSlideNumber%.png
	Gui, %MonitorNumber%:destroy
	Gui, %MonitorNumber%:+AlwaysOnTop +LastFound +Owner -Caption
	Gui, %MonitorNumber%:Color, Black
	Gui, %MonitorNumber%:Add, Picture, w%__Width% h%__Height%, %file%	
	Gui, %MonitorNumber%:Show, x%coord% y0 maximize
}

;Uses gdip library to get the screenshots 
;screen variable is of the format x coordinate| y coordinate| width| height
Screenshot(outfile)
{
    pToken := Gdip_Startup()
    screen=0|0|%A_ScreenWidth%|%A_ScreenHeight%
    pBitmap := Gdip_BitmapFromScreen(screen)

    Gdip_SaveBitmapToFile(pBitmap, outfile, 100)
    Gdip_DisposeImage(pBitmap)
    Gdip_Shutdown(pToken)
}

;Screenshot is saved into a temp folder with slide number as the names
saveScreenshot(SlideNumber){
	file := A_WorkingDir . "\temp\" . SlideNumber . ".png"
	Screenshot(file)
}

;Coordinates of the display are sorted using this function 
SortArray(Array, Order="A") {
    ;Order A: Ascending, D: Descending, R: Reverse
    MaxIndex := ObjMaxIndex(Array)
    If (Order = "R") {
        count := 0
        Loop, % MaxIndex 
            ObjInsert(Array, ObjRemove(Array, MaxIndex - count++))
        Return
    }
    Partitions := "|" ObjMinIndex(Array) "," MaxIndex
    Loop {
        comma := InStr(this_partition := SubStr(Partitions, InStr(Partitions, "|", False, 0)+1), ",")
        spos := pivot := SubStr(this_partition, 1, comma-1) , epos := SubStr(this_partition, comma+1)    
        if (Order = "A") {    
            Loop, % epos - spos {
                if (Array[pivot] > Array[A_Index+spos])
                    ObjInsert(Array, pivot++, ObjRemove(Array, A_Index+spos))    
            }
        } else {
            Loop, % epos - spos {
                if (Array[pivot] < Array[A_Index+spos])
                    ObjInsert(Array, pivot++, ObjRemove(Array, A_Index+spos))    
            }
        }
        Partitions := SubStr(Partitions, 1, InStr(Partitions, "|", False, 0)-1)
        if (pivot - spos) > 1    ;if more than one elements
            Partitions .= "|" spos "," pivot-1        ;the left partition
        if (epos - pivot) > 1    ;if more than one elements
            Partitions .= "|" pivot+1 "," epos        ;the right partition
    } Until !Partitions
}

ESC::
	objppt.SlideShowWindow.View.Exit
	FileRemoveDir, temp, 1
	ExitApp
