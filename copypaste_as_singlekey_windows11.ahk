^!F1::
ClipPrev := Clipboard
Send, ^c
if (Clipboard = "" or Clipboard = ClipPrev) {    ;if nothing is selected
        Clipboard := Stored1
        Send, ^v
    }
else         ;if something is selected
    Stored1 := Clipboard
Clipboard := ClipPrev
return
