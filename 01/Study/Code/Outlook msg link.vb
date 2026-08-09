Set Outlook = CreateObject("Outlook.Application")
Set SelectedItem = Outlook.ActiveExplorer.Selection.Item(1)
Set Shell = CreateObject("Shell.Application")
Shell.ShellExecute "cmd", "/c echo Outlook:" & SelectedItem.entryID & " | clip", "", "runas", 1