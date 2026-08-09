```vb
Function SetClipBoardText(ByVal Text As Variant) As Boolean
SetClipBoardText = CreateObject("htmlfile").ParentWindow.ClipboardData.SetData("Text", Text)
End Function

'Adds a link to the currently selected message to the clipboard
Sub ObsidianLink()

Dim objMail As Object
Dim txtObsLink As String
Dim exito As Boolean

Dim doClipboard As New DataObject

'One and ONLY one message muse be selected
If Application.ActiveExplorer.Selection.Count <> 1 Then
MsgBox ("Select one and ONLY one message.")
Exit Sub
End If

Set objMail = Application.ActiveExplorer.Selection.Item(1)

If objMail.Class = olMail Then
txtObsLink = "[[" + Format(objMail.ReceivedTime, "YYYYMMDDHHmm") + " E= " + objMail.Subject + " (" + objMail.SenderName + ")]] [Link](outlook:" + objMail.EntryID + ")"

ElseIf objMail.Class = olAppointment Then
    txtObsLink = "[MEETING: " + objMail.Subject + " (" + objMail.Organizer + ")](outlook:" + objMail.EntryID + ")"
ElseIf objMail.Class = olTask Then
    txtObsLink = "[TASK: " + objMail.Subject + " (" + objMail.Owner + ")](outlook:" + objMail.EntryID + ")"
ElseIf objMail.Class = olContact Then
    txtObsLink = "[CONTACT: " + objMail.Subject + " (" + objMail.FullName + ")](outlook:" + objMail.EntryID + ")"
ElseIf objMail.Class = olJournal Then
    txtObsLink = "[JOURNAL: " + objMail.Subject + " (" + objMail.Type + ")](outlook:" + objMail.EntryID + ")"
ElseIf objMail.Class = olNote Then
    txtObsLink = "[NOTE: " + objMail.Subject + " (" + " " + ")](outlook:" + objMail.EntryID + ")"
Else
    txtObsLink = "[ITEM: " + objMail.Subject + " (" + objMail.MessageClass + ")](outlook:" + objMail.EntryID + ")"

End If

doClipboard.SetText txtObsLink
doClipboard.PutInClipboard

exito = SetClipBoardText(txtObsLink)

End Sub
```
