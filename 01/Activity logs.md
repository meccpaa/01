
```dataview
    TABLE dateformat(file.mtime, "dd-MM-yy HH:mm") as "Last modified", Type FROM -"templates"
    SORT file.mtime DESC
    WHERE file.mtime >= date(today) - dur(1 week)
```
