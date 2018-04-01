#NoEnv
#Persistent ; Keep the script running until the user exits it.
#SingleInstance

; Close possible existing tracker

Process,Close,pythonw.exe

; Start tracker to run in background

Run, %A_ScriptDir%\tracker.pyw "%A_ScriptDir%\values.txt"

; Get effective screensize to show settings GUI in bottom right corner on start

SysGet, Mon, MonitorWorkArea

Bot = %MonBottom%
Width = %MonRight%
y := Bot - 40
x := Width - 100

GuiWidth  = 100
GuiTitle  = 

; Settings GUI

Gui, -Caption +AlwaysOnTop  +owner
Gui, Color, Black
Gui, Font, s14, Verdana
Gui, Add, Text,  x0 y0 w%GuiWidth% h5 +0x4 ,
Gui, Add, Text,  x0 y0 w%GuiWidth% h5 hwndTitleBar Backgroundtrans +0x200 gGuiMove
              ,  % " " GuiTitle

Gui, Add, Text,  cGray x27 y9 vTextColor ,  xxxxx

Gui,show, x%x% y%y% w100 h40,LB

; Read contents of text file containing tracker values and update ticker text and color based on panic index

Loop{

  FileRead, trackerInfo, %A_ScriptDir%\values.txt

  StringSplit, trackerValues, trackerInfo, |

  priceBTC = %trackerValues1%
  panicIndex = %trackerValues2%

  ControlSetText, Static3, %priceBTC% , LB
  if panicIndex < 7
  {
    Gui, Font, cGray
    GuiControl, Font, TextColor
  }
  if panicIndex > 7 and panicIndex < 14
  {
    Gui, Font, c9e622f
    GuiControl, Font, TextColor
  }
  if panicIndex > 14
  {
    Gui, Font, ca03030
    GuiControl, Font, TextColor
  }
  Gui, 1: +AlwaysOnTop
   

  Sleep 1000


}

GuiMove: 
PostMessage, 0xA1, 2,,, A ; Titlebar drag/move
Return 
	

