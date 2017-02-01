f5:: 
  try{
    ppt := ComObjActive("PowerPoint.Application")
	objppt := ppt.ActivePresentation
	TotalSlides:=% objppt.Slides.Count
	FileCreateDir, temp
  }
  catch e {
	MsgBox % "Error in " e.Message ", which was called at line " e.Line 
  }
  Loop %TotalSlides%{
	var++
	;MsgBox %var%
	saveppt := objppt.Slides(var).Export(A_ScriptDir . "\temp\" . var . ".png", "PNG")
  }
  ;pt := ppt.ActivePresentation.(test, ppSaveAsPNG)
  SysGet, MonitorCount, MonitorCount
  ;MsgBox %MonitorCount%
  MsgBox saved
  ;MsgBox inside %MonitorCount%
  ppt := objppt.SlideShowSettings
  ppt.Run
  ;monitorDisplay(objppt, MonitorCount)
Return

Right::
	objppt.SlideShowWindow.View.Next
	monitorDisplay(objppt, MonitorCount)
	return

monitorDisplay(objppt, MonitorCount){
	CurrentSlideNumber :=% objppt.SlideShowWindow.View.Slide.SlideIndex
	;MsgBox %CurrentSlideNumber% is the current slide
	monitor := MonitorCount-1
	Loop %monitor%{
		;MsgBox insideloop
		var2++
		;MsgBox var2(MonitorNumber) val = %var2%
		setDisplay(var2, CurrentSlideNumber-1)
		var2 := 0
		;MsgBox end of Loop monitor var2 = %var2%
	}
}	
	
getCoordinates(MonitorNumber){
	coord := 1920*MonitorNumber
	return coord
}

;SetEnv file, C:\Users\SK\Documents\AutoHotKey\1.png

setDisplay(MonitorNumber, PreviousSlideNumber){
global
	coord := getCoordinates(MonitorNumber)
	SetEnv file, C:\Users\SK\Documents\AutoHotKey\temp\%PreviousSlideNumber%.png
	;file := "C:\Users\SK\Documents\AutoHotKey\" . %CurrentSlideNumber% . ".png"
	;file := "C:\Users\SK\Documents\AutoHotKey\1.png"
	;MsgBox %coord%,%MonitorNumber%,%PreviousSlideNumber%,%file%
	Gui, 1:destroy
	Gui, 1:+AlwaysOnTop +LastFound +Owner -Caption
	Gui, 1:Color, Black
	Gui, 1:Add, Picture, w%A_ScreenWidth% h-1, %file%	
	Gui, 1:Show, x%coord% y0 maximize
}