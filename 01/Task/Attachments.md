
```dataview
    TABLE Attachment, Link FROM [[Email]] and -"templates"
    SORT file.mtime DESC
    WHERE Date >= date(today) - dur(3 months)
```
