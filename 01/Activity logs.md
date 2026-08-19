
```dataview
    TABLE Date AS "Date", Type , Attachment FROM -"templates"
    SORT file.mtime DESC
    WHERE file.mtime >= date(today) - dur(1 week)
```
