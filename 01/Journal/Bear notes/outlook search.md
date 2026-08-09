# outlook search
For the Macro technique, use the following code:
~~~~~~~Create a unified inbox~~~~~~~
Sub UnifiedInbox()
Dim myOlApp As New Outlook.Application
txtSearch = “folder:Inbox received: (this week)”
myOlApp.ActiveExplorer.Search txtSearch, olSearchScopeAllFolders
Set myOlApp = Nothing
End Sub
~~~~~~~~~~~~~~
~~~~~~~Create a Unified Sent Folder~~~~~~~
Sub UnifiedSentbox()
Dim myOlApp As New Outlook.Application
txtSearch = “folder: (Sent Mail) sent: (this week)”
myOlApp.ActiveExplorer.Search txtSearch, olSearchScopeAllFolders
Set myOlApp = Nothing
End Sub
~~~~~~~~~~~~~~

[How to View Multiple Inboxes at Once in Outlook 365 - YouTube](https://youtu.be/NpFSsovHgVo)
#code/vba